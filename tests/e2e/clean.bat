@echo off
rem clean.bat - apaga os artefatos GERADOS do SDK python (exemplos + logs)
del /f /q "D:\ProjetoFalaAI\FalaAI\FalaAI_api\sdks\python\examples\*.py" 2>nul
del /f /q "D:\ProjetoFalaAI\FalaAI\FalaAI_api\sdks\python\examples\README.md" 2>nul
del /f /q "D:\ProjetoFalaAI\FalaAI\FalaAI_api\sdks\python\tests\e2e\logs\python_*.json" 2>nul
del /f /q "D:\ProjetoFalaAI\FalaAI\FalaAI_api\sdks\python\tests\e2e\logs\python_*.html" 2>nul
echo done
pause