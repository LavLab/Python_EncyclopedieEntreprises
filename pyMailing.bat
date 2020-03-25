@echo off
title Python:Execute pyMailing
color 0a
echo.
:loop
cls
echo Generation UI ...
for /r .\ui %%X in (*.*) do (
	for /f "tokens=5 delims=\" %%a in ("%%X") do (
		for /f "tokens=1 delims=." %%b in ("%%a") do (
			echo %%b.ui -x} %%b.py
			pyuic5 .\ui\%%b.ui -o .\%%b.py
		)
	)
)
echo.
pause
goto loop
echo Execution pyMailing.py ...
python Main.py
pause
goto loop