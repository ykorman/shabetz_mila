@echo off
set PATH=%PATH%;"C:\Program Files\BitNami DjangoStack\python"
python.exe server_tests.py
if ERRORLEVEL 0 start python.exe webserver.py
rem echo Press any key to stop server
rem pause
rem taskkill /IM python.exe