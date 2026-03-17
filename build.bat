@echo off
color 0a

title Build - evilBrowser
mode con:cols=100 lines=50
cls
pyinstaller -w -i icon.png --collect-all selenium --clean -F evilBrowser.py
pause
