# 설치{#installation}

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


### 명령 프롬프트{#dos-prompt}

만약 파이썬을 명령 프롬프트 같은 윈도우 커맨드 라인툴에서 사용하고 싶다면 PATH 환경 변수를 알맞게 설정해야 합니다.

윈도우 2000, XP, 2003의 경우, `제어판` → `시스템` → `고급` → `환경 변수`로 들어가세요. 이제 \_시스템 변수\_ 목록에 있는 `PATH`를 선택한 뒤, `편집` 버튼을 누르고 `C:\Python36` (이 폴더가 실제로 존재하는지 다시 한번 확인하세요. 더 최신 버전의 파이썬을 설치한 경우 폴더 이름이 다를 수 있습니다)이라는 문자열을 이미 있던 문자열의 맨 뒤에 추가하세요. 당연한 이야기지만 올바른 경로를 입력해야 합니다.

그 이전 버전의 윈도우를 사용하시는 분들은 `C:\AUTOEXEC.BAT`를 열고 맨 뒷줄에 `PATH=%PATH%;C:\Python36`이라고 마지막에 한 줄 추가한 뒤 시스템을 재시작하세요. 윈도우 NT의 경우 `AUTOEXEC.NT` 파일을 편집하세요.

윈도우 비스타

- 시작 메뉴를 누르고 `제어판`을 클릭하세요.
- `시스템`을 클릭하면 오른쪽에 `컴퓨터에 대한 기본 정보 보기` 창이 보일 것입니다.
- 왼쪽에는 작업 항목 아래 여러 메뉴들이 있는데 이 중 `고급 시스템 설정`을 누릅니다.
- 그러면 `시스템 속성 대화상자`의 `고급` 탭이 보이게 됩니다. 오른쪽 아래에 있는 `환경 변수` 버튼을 클릭하세요.
- 아래쪽의 `시스템 변수`라고 적혀 있는 목록에 있는 PATH항목을 선택하고 `편집` 버튼을 클릭하세요.
- 경로를 수정하세요.
- 시스템을 재시작하세요. 윈도우 비스타는 컴퓨터가 재시작되기 전까지 새로 지정한 환경 변수가 적용되지 않습니다.

윈도우 7과 윈도우 8

- 바탕 화면에 있는 컴퓨터 아이콘에서 마우스 오른쪽 클릭하고 `속성`을 누르거나 `시작` 메뉴를 클릭하고 `제어판`을 선택한 뒤 `시스템 및 보안`의 `시스템`을 클릭하세요. 화면 왼쪽에 보이는 `고급 시스템 설정` 항목을 클릭한 뒤 `고급` 탭을 클릭하세요. 아래쪽에 보이는 `시스템 변수` 밑에 있는 여러 변수들 중 `PATH`라는 변수를 찾아 선택한 뒤, `편집` 버튼을 누르세요.
- 이미 있던 문자열의 맨 끝에 `C:\Python36`을 추가하세요(이 폴더가 실제로 존재하는지 다시 한번 확인하세요. 더 최신 버전의 파이썬을 설치한 경우 폴더 이름이 다를 수 있습니다).
- 만약 원래 있던 문자열이 `%SystemRoot%\system32;`였다고 한다면 변경된 문자열은 `%SystemRoot%\system32;C:\Python36`이어야 합니다.
- `확인` 버튼을 누르면 시스템을 재시작하지 않아도 변경 사항이 곧바로 적용됩니다만, 현재 실행중인 명령 프롬프트는 종료 후 다시 시작해주어야 합니다.

### 윈도우에서 파이썬 실행하기

[PATH 환경변수가 제대로 설정되어 있다면](#dos-prompt) 파이썬 인터프리터를 명령 프롬프트 상에서도 실행하실 수 있습니다.

윈도우에서 터미널 창을 열기 위해서는 시작 메뉴를 누르고 `실행` 버튼을 클릭하세요. 대화상자에 `cmd`를 입력하고 `엔터키`를 누르세요.

이제 `python`을 입력하고 파이썬 프롬프트가 잘 실행되는지 확인하세요.

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
