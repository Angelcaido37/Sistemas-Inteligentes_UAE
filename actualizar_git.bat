@echo off
REM Script: actualizar_git.bat
REM Descripción: Actualiza el repositorio local y remoto de Git

echo ============================
echo  ACTUALIZANDO PROYECTO GIT
echo ============================

REM Paso 1: Mostrar estado actual
git status

REM Paso 2: Agregar todos los cambios
git add .
echo Cambios agregados al área de preparación.

REM Paso 3: Solicitar mensaje de commit
set /p mensaje=Escribe el mensaje para el commit: 
git commit -m "%mensaje%"
echo Commit realizado con mensaje: "%mensaje%"

REM Paso 4: Hacer pull con rebase para integrar cambios remotos
git pull --rebase origin main

REM Paso 5: Hacer push al repositorio remoto
git push

echo ============================
echo  ACTUALIZACIÓN COMPLETA
echo ============================
pause
