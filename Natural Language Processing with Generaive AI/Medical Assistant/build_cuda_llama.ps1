# Rebuild llama-cpp-python with CUDA for RTX 5090, AVX-512 disabled (Arrow Lake).
# Requires:
#   - Visual Studio 2022 Build Tools (C++ workload). CUDA 13.1 nvcc does NOT
#     support VS 2026 / MSVC 19.51 (cudafe++ crashes even with
#     -allow-unsupported-compiler).
#   - CUDA Toolkit 13.1
#
# Run from the project folder after VS 2022 Build Tools are installed:
#   powershell -ExecutionPolicy Bypass -File .\build_cuda_llama.ps1

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot
Remove-Item Env:SSLKEYLOGFILE -ErrorAction SilentlyContinue

$vsDevCandidates = @(
    "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\Launch-VsDevShell.ps1",
    "C:\Program Files\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\Launch-VsDevShell.ps1",
    "C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools\Common7\Tools\Launch-VsDevShell.ps1"
)
$vsDev = $vsDevCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $vsDev) {
    throw "VS Build Tools C++ workload not found. Install Visual Studio 2022 Build Tools with the C++ workload (CUDA 13.1 does not support VS 2026)."
}
if ($vsDev -match '\\18\\') {
    Write-Warning "Using VS 2026. CUDA 13.1 nvcc will likely fail; install VS 2022 Build Tools instead."
}
& $vsDev -Arch amd64 -SkipAutomaticLocation

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$venvScripts = Join-Path $PSScriptRoot ".venv\Scripts"
$env:PATH = "$venvScripts;$env:PATH"

$env:CUDA_PATH = "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1"
$env:CUDACXX = "$env:CUDA_PATH\bin\nvcc.exe"
$env:PATH = "$env:CUDA_PATH\bin\x64;$env:CUDA_PATH\bin;$env:PATH"

$env:FORCE_CMAKE = "1"
$env:CMAKE_GENERATOR = "Ninja"
$env:NVCC_PREPEND_FLAGS = "-allow-unsupported-compiler"
$env:CMAKE_CUDA_FLAGS = "-allow-unsupported-compiler"
$env:CMAKE_ARGS = "-DGGML_CUDA=ON -DGGML_NATIVE=OFF -DGGML_AVX2=ON -DGGML_AVX512=OFF -DCMAKE_CUDA_ARCHITECTURES=120 -DCMAKE_CUDA_COMPILER=`"$env:CUDACXX`" -DCMAKE_CUDA_FLAGS=-allow-unsupported-compiler"

# Windows MAX_PATH: extract the sdist under a short temp dir.
$shortTemp = "C:\t"
New-Item -ItemType Directory -Force -Path $shortTemp | Out-Null
$env:TEMP = $shortTemp
$env:TMP = $shortTemp
$env:TMPDIR = $shortTemp

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
& $python -m pip install ninja cmake
Write-Host "Compiling llama-cpp-python with CUDA (this takes several minutes)..."
& $python -m pip install llama-cpp-python==0.3.35 --force-reinstall --no-cache-dir --no-binary llama-cpp-python
if ($LASTEXITCODE -ne 0) { throw "llama-cpp-python CUDA build failed (exit $LASTEXITCODE)" }
Write-Host "CUDA llama-cpp-python install finished."
