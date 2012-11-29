@echo off
set PATH=%PATH%;"C:\Program Files\BitNami DjangoStack\python"
python.exe server_tests.py
if ERRORLEVEL 0 python.exe webserver.py
rem pause