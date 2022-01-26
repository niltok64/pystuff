@echo off
echo building...
pip install --upgrade pip
pip install pyinstaller
cd ..
cd bestagon
pyinstaller hexagon.py --onefile
cd ..
cd pewpew
pyinstaller pew.py --onefile
cd ..
cd trianglehaha
pyinstaller main.py --onefile --add-data triangle.py
cd ..
cd twoturtles
pyinstaller two.py --onefile
cd ..
cd windowssquare
pyinstaller lol.py --onefile
echo done building all programs, check respective "dist/" folders for executable
pause
