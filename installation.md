# 설치

이 책에서 "파이썬 3"이라고 하는 것은 [Python 3.6.0](https://www.python.org/downloads/) 이상 버전을 뜻합니다.

## 윈도우에서 설치하기

https://www.python.org/downloads/ 에 접속해서 최신 버전의 설치 프로그램을 내려받아 설치하세요. 이 글이 번역되는 2017년 5월 현재 최신 버전은 Python 3.6.1 입니다. 설치 방법은 일반적인 윈도우 기반 소프트웨어를 설치 하는 것과 같습니다.

만약 Windows Vista 이전 버전(Windows XP 등 - 역자 주)를 사용한다면 [Python 3.4](https://www.python.org/downloads/windows/) 이하를 설치해야 합니다. 

주의: 설치할 때 `Add Python 3.6 to Path`에 반드시 체크를 해야 합니다.

설치 위치를 변경하기 위해서 `Customize installation`를 선택하고 `Next` 버튼을 누른 후 `Customize install location`에 `C:\python36`을 입력합니다.

만약 `Add Python to environment variables`에 체크가 되어 있지 않다면 체크합니다. 이 옵션은 처음 설치 화면에 나왔던 `Add Python 3.6 to PATH`과 같은 것입니다.

`Install For all users` 옵션을 통해 모든 사용자가 런처(Launcher)를 사용할 수 있도록 설정할 수 있지만 여러명이 서로 다른 계정으로 동시에 사용하는 컴퓨터가 아닌 이상 체크하지 않아도 괜찮습니다. 런처는 컴퓨터에 설치된 서로 다른 파이썬 버전을 사용하기 위해 사용합니다.

만약 경로가 제대로 설정되지 않았다면 문제 해결을 위해 다음 단계를 따르세요. 문제가 없다면 `Running Python prompt on Windows`으로 이동합니다.

NOTE: 프로그래밍에 대해 이미 잘 알고 있고 Docker에 익숙하다면 [Python in Docker(영문)](https://hub.docker.com/_/python/)와 [Docker on Windows(영문)](https://docs.docker.com/windows/)를 확인해 보세요.


### DOS Prompt {#dos-prompt}

If you want to be able to use Python from the Windows command line i.e. the DOS prompt, then you need to set the PATH variable appropriately.

For Windows 2000, XP, 2003 , click on `Control Panel` -> `System` -> `Advanced` -> `Environment Variables`. Click on the variable named `PATH` in the _System Variables_ section, then select `Edit` and add `;C:\Python35` (please verify that this folder exists, it will be different for newer versions of Python) to the end of what is already there. Of course, use the appropriate directory name.

<!-- The directory should match pythonVersion variable in book.json -->
For older versions of Windows, open the file `C:\AUTOEXEC.BAT` and add the line `PATH=%PATH%;C:\Python35` and restart the system. For Windows NT, use the `AUTOEXEC.NT` file.

For Windows Vista:

- Click Start and choose `Control Panel`
- Click System, on the right you'll see "View basic information about your computer"
- On the left is a list of tasks, the last of which is `Advanced system settings`. Click that.
- The `Advanced` tab of the `System Properties` dialog box is shown. Click the `Environment Variables` button on the bottom right.
- In the lower box titled `System Variables` scroll down to Path and click the `Edit` button.
- Change your path as need be.
- Restart your system. Vista didn't pick up the system path environment variable change until I restarted.

For Windows 7 and 8:

- Right click on Computer from your desktop and select `Properties` or click `Start` and choose `Control Panel` -> `System and Security` -> `System`. Click on `Advanced system settings` on the left and then click on the `Advanced` tab. At the bottom click on `Environment Variables` and under `System variables`, look for the `PATH` variable, select and then press `Edit`.
- Go to the end of the line under Variable value and append `;C:\Python35` (please verify that this folder exists, it will be different for newer versions of Python) to the end of what is already there. Of course, use the appropriate folder name.
- If the value was `%SystemRoot%\system32;` It will now become `%SystemRoot%\system32;C:\Python36` <!-- The directory should match pythonVersion variable in book.json -->
- Click `OK` and you are done. No restart is required, however you may have to close and reopen the command line.

### Running Python prompt on Windows

For Windows users, you can run the interpreter in the command line if you have [set the `PATH` variable appropriately](#dos-prompt).

To open the terminal in Windows, click the start button and click `Run`. In the dialog box, type `cmd` and press `[enter]` key.

Then, type `python` and ensure there are no errors.

## Installation on Mac OS X

For Mac OS X users, use [Homebrew](http://brew.sh): `brew install python3`.

To verify, open the terminal by pressing `[Command + Space]` keys (to open Spotlight search), type `Terminal` and press `[enter]` key. Now, run `python3` and ensure there are no errors.

## Installation on GNU/Linux

For GNU/Linux users, use your distribution's package manager to install Python 3, e.g. on Debian & Ubuntu: `sudo apt-get update && sudo apt-get install python3`.

To verify, open the terminal by opening the `Terminal` application or by pressing `Alt + F2` and entering `gnome-terminal`. If that doesn't work, please refer the documentation of your particular GNU/Linux distribution. Now, run `python3` and ensure there are no errors.

You can see the version of Python on the screen by running:

<!-- The output should match pythonVersion variable in book.json -->
```
$ python3 -V
Python 3.6.0
```

NOTE: `$` is the prompt of the shell. It will be different for you depending on the settings of the operating system on your computer, hence I will indicate the prompt by just the `$` symbol.

CAUTION: Output may be different on your computer, depending on the version of Python software installed on your computer.

## Summary

From now on, we will assume that you have Python installed on your system.

Next, we will write our first Python program.
