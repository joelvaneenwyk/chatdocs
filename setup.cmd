@echo off
goto:$Main

:$Main
setlocal EnableDelayedExpansion
    set "_python=C:\Windows\py.exe"
    if not exist "!_python!" set "_python="
    if not exist "!_python!" goto:$MainDone

    set "_docs_path=%~1"
    if not exist "!_docs_path!" set "_docs_path=%~dp0\%~1"
    if not exist "!_docs_path!" set "_docs_path=%~dp0\examples\documents\state_of_the_union.txt"
    if not exist "!_docs_path!" set "_docs_path="

    cd /d "%~dp0"
    "!_python!" -3 -m pip install -r "%~dp0requirements.txt"
    "!_python!" -3 -m pip install .[gptq]
    "!_python!" -3 -m chatdocs download
    if exist "!_docs_path!" (
        "!_python!" -3 -m chatdocs add "!_docs_path!"
    )
    goto:$MainDone

    :$MainError
    goto:$MainDone

    :$MainDone
endlocal & exit /b %ERRORLEVEL%
