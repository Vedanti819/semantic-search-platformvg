@echo off
cd /d %~dp0..
call myaienv\Scripts\activate.bat
python -m streamlit run frontend\streamlit_app.py
