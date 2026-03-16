@echo off
setlocal enabledelayedexpansion
title 🧹 Conda System Purge - Robotgames
chcp 65001 > nul

:: Cores via PowerShell
set "PS_CMD=powershell -NoProfile -ExecutionPolicy Bypass -Command"

cls
%PS_CMD% "Write-Host '--------------------------------------------------' -ForegroundColor White -BackgroundColor Red"
%PS_CMD% "Write-Host '      ⚠️ AVISO: LIMPEZA TOTAL DE AMBIENTES       ' -ForegroundColor White -BackgroundColor Red"
%PS_CMD% "Write-Host '--------------------------------------------------' -ForegroundColor Red"
echo.
%PS_CMD% "Write-Host 'Este script irá remover TODOS os ambientes (exceto base)' -ForegroundColor Yellow"
%PS_CMD% "Write-Host 'e limpar o cache de downloads do Anaconda.' -ForegroundColor Yellow"
echo.
set /p CONFIRM="Deseja continuar? (S/N): "
if /i "%CONFIRM%" neq "S" exit

echo.
%PS_CMD% "Write-Host '🔍 [1/3] Listando e removendo ambientes personalizados...' -ForegroundColor Cyan"

:: Loop para remover ambientes (evita remover o 'base')
for /f "tokens=1" %%a in ('conda env list ^| findstr /v "base #"') do (
    if not "%%a"=="" (
        %PS_CMD% "Write-Host ' 🗑️ Removendo: %%a' -ForegroundColor Gray"
        call conda env remove -n %%a -y > nul
    )
)

echo.
%PS_CMD% "Write-Host '📦 [2/3] Limpando cache de pacotes e arquivos Tar (Index/Cache)...' -ForegroundColor Cyan"
call conda clean --all -y

echo.
%PS_CMD% "Write-Host '📁 [3/3] Removendo resíduos temporários do Python (__pycache__)...' -ForegroundColor Cyan"
del /s /q /f *.pyc > nul 2>&1
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" > nul 2>&1

echo.
%PS_CMD% "Write-Host '--------------------------------------------------' -ForegroundColor Green"
%PS_CMD% "Write-Host '       ✨ SISTEMA LIMPO E OTIMIZADO!            ' -ForegroundColor White -BackgroundColor DarkGreen"
%PS_CMD% "Write-Host '--------------------------------------------------' -ForegroundColor Green"
echo.
%PS_CMD% "Write-Host ' Agora você pode rodar o setup_vision.bat ' -NoNewline; Write-Host 'do zero.' -ForegroundColor Cyan"
echo.
pause