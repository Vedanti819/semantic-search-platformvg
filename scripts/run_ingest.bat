@echo off
cd /d %~dp0..
call myaienv\Scripts\activate.bat
python scripts\ingest.py
pause
