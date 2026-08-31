# Replace CPU PyTorch with the CUDA 13 build so sentence-transformers embeddings
# run on the RTX 5090 (Blackwell / sm_120). ~3 GB download.
#
# Run with the notebook kernel STOPPED (torch DLLs are locked while in use):
#   powershell -ExecutionPolicy Bypass -File .\install_gpu_torch.ps1

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot
Remove-Item Env:SSLKEYLOGFILE -ErrorAction SilentlyContinue

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

Write-Host "Installing torch cu130 (Blackwell sm_120 kernels)..."
& $python -m pip install --force-reinstall torch --index-url https://download.pytorch.org/whl/cu130
if ($LASTEXITCODE -ne 0) { throw "torch cu130 install failed (exit $LASTEXITCODE)" }

& $python -c "import torch; print('torch', torch.__version__); print('cuda', torch.version.cuda); print('available', torch.cuda.is_available()); print('device', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'n/a')"
