# Local setup for the improved Llama and OpenAI notebooks.
# Run from the project folder:  powershell -ExecutionPolicy Bypass -File .\setup_local.ps1

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

# Cursor / some SSL-intercepting tools set this; Python then fails with PermissionError 13.
Remove-Item Env:SSLKEYLOGFILE -ErrorAction SilentlyContinue

$cudaBin = "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v13.1\bin\x64"
if (Test-Path $cudaBin) {
    $env:PATH = "$cudaBin;$env:PATH"
}

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

Write-Host "Installing Python packages..."
& $python -m pip install --upgrade pip wheel
& $python -m pip install -r (Join-Path $PSScriptRoot "requirements.txt")

# Prebuilt CPU wheel. A CUDA Blackwell wheel exists, but it uses AVX-512 code paths
# that crash this Arrow Lake CPU (Core Ultra 9 275HX) with 0xC000001D.
Write-Host "Installing llama-cpp-python (CPU AVX2 wheel)..."
& $python -m pip install --prefer-binary --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu llama-cpp-python

Write-Host "Registering Jupyter kernel..."
& $python -m ipykernel install --user --name medical-assistant --display-name "Python (Medical Assistant)"

Write-Host "Done. In Cursor, select kernel: Python (Medical Assistant)"
Write-Host "Place medical_diagnosis_manual.pdf in this folder before the RAG section."
