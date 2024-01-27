@echo off
setlocal
cd /d "%~dp0"
py -3 -m pip install .[gptq]
py -3 -m pip install ctransformers[cuda]
py -3 -m chatdocs download
if exist "%~1" (
    py -3 -m chatdocs add "%~1"
)