$ErrorActionPreference = 'Stop'

Write-Host 'Creating Python virtual environment...'
python -m venv myaienv

Write-Host 'Activating virtual environment...'
& .\myaienv\Scripts\Activate.ps1

Write-Host 'Upgrading pip...'
python -m pip install --upgrade pip

Write-Host 'Installing project dependencies...'
pip install -r requirements.txt

if (-not (Test-Path '.env')) {
    Copy-Item '.env.example' '.env'
}

Write-Host ''
Write-Host 'Setup complete.'
Write-Host 'Next: python scripts\ingest.py'
Write-Host 'Then: python -m uvicorn app.api:app --reload --host 127.0.0.1 --port 8000'
Write-Host 'In a second terminal: python -m streamlit run frontend\streamlit_app.py'
