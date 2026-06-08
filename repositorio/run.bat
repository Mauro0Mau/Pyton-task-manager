@echo off

cd /d D:\estudos_de programacao\Pyton-task-maneger\repositorio

..\.venv\Scripts\python.exe -m pip install -r requirements.txt >nul 2>&1
cls

..\.venv\Scripts\python.exe main.py

pause