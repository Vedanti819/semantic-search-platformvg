# Windows Fix / Clean Setup

The most reliable fix for errors such as `Permission denied: myaienv\\Scripts\\python.exe`, broken `pip._internal`, `click.Choice`, or `google.protobuf` import errors is to recreate the virtual environment.

## Important
Run all commands below from this folder:

`C:\\Users\\hp\\Downloads\\semantic-search-platform`

Do **not** run `cd semantic-search-platform` when your prompt already shows that folder.

## Clean setup

1. Close any old terminals running Python, Uvicorn, or Streamlit for this project.
2. Open a new PowerShell terminal in the project folder.
3. Check Python:

```powershell
py -3.12 --version
```

Python 3.12 is recommended for this project on Windows.

4. Remove the broken environment:

```powershell
Remove-Item -Recurse -Force .\\myaienv
```

5. Create a fresh environment:

```powershell
py -3.12 -m venv myaienv
```

6. Upgrade packaging tools using the environment's Python directly:

```powershell
.\\myaienv\\Scripts\\python.exe -m ensurepip --upgrade
.\\myaienv\\Scripts\\python.exe -m pip install --upgrade pip setuptools wheel
```

7. Install dependencies:

```powershell
.\\myaienv\\Scripts\\python.exe -m pip install -r requirements.txt
```

8. Create `.env`:

```powershell
Copy-Item .env.example .env
```

9. Build the index:

```powershell
.\\myaienv\\Scripts\\python.exe scripts\\ingest.py
```

10. Start FastAPI in Terminal 1:

```powershell
.\\myaienv\\Scripts\\python.exe -m uvicorn app.api:app --reload --host 127.0.0.1 --port 8000
```

11. Start Streamlit in Terminal 2:

```powershell
.\\myaienv\\Scripts\\python.exe -m streamlit run frontend\\streamlit_app.py
```

## Verification

FastAPI:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

Streamlit:
- http://localhost:8501

## If `Remove-Item` says the file is in use

Close VS Code completely, make sure no project terminal is running Python/Streamlit/Uvicorn, reopen PowerShell, and run the clean setup again.

## Quick package check

```powershell
.\\myaienv\\Scripts\\python.exe -c "from click import Choice; from google.protobuf import descriptor; import uvicorn, streamlit, faiss; print('OK: Python packages are healthy')"
```
