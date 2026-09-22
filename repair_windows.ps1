$ErrorActionPreference = 'Stop'

Write-Host 'Semantic Search Platform - Windows clean setup' -ForegroundColor Cyan
Write-Host 'Project folder:' (Get-Location)

if (-not (Test-Path '.\app\api.py')) {
    throw 'Run this script from the semantic-search-platform project root.'
}

$python = 'py -3.12'
& py -3.12 --version

if (Test-Path '.\myaienv') {
    Write-Host 'Removing broken myaienv...'
    Remove-Item -Recurse -Force '.\myaienv'
}

Write-Host 'Creating fresh Python 3.12 environment...'
& py -3.12 -m venv myaienv

Write-Host 'Bootstrapping pip...'
& .\myaienv\Scripts\python.exe -m ensurepip --upgrade
& .\myaienv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel

Write-Host 'Installing dependencies...'
& .\myaienv\Scripts\python.exe -m pip install -r requirements.txt

if (-not (Test-Path '.\.env')) {
    Copy-Item '.env.example' '.env'
}

Write-Host 'Checking imports...'
& .\myaienv\Scripts\python.exe -c "from click import Choice; from google.protobuf import descriptor; import uvicorn, streamlit, faiss; print('OK: package imports are healthy')"

Write-Host ''
Write-Host 'Setup complete.' -ForegroundColor Green
Write-Host 'Next: .\myaienv\Scripts\python.exe scripts\ingest.py'
Write-Host 'Then: .\myaienv\Scripts\python.exe -m uvicorn app.api:app --reload --host 127.0.0.1 --port 8000'
Write-Host 'Second terminal: .\myaienv\Scripts\python.exe -m streamlit run frontend\streamlit_app.py'
