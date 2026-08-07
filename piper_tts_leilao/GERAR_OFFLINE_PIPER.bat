@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ==============================================
echo  NARRACAO OFFLINE - PIPER / SHERPA-ONNX
echo ==============================================
echo.

where py >nul 2>nul
if not errorlevel 1 (
  set "PY=py -3"
) else (
  set "PY=python"
)

%PY% -m pip install --upgrade piper-tts==1.6.0 sherpa-onnx soundfile numpy
if errorlevel 1 goto ERRO

echo.
echo Os modelos precisam estar extraidos dentro da pasta modelos.
echo Execute: %PY% gerar_piper_sherpa.py
%PY% gerar_piper_sherpa.py
if errorlevel 1 goto ERRO

echo.
echo Concluido. Confira a pasta saida.
pause
exit /b 0

:ERRO
echo.
echo Falha durante a instalacao ou geracao.
pause
exit /b 1
