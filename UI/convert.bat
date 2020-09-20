set /p name="File name: "
echo %name%
pyuic5 %name%.ui -o %name%UI.py