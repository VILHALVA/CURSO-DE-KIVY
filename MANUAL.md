# MANUAL
## INSTALAÇÃO E CONFIGURAÇÃO DO KIVY:
### 1. INSTALAÇÃO DO KIVY:
Para instalar o Kivy, você precisará do Python 3.6 ou superior e do `pip`. Siga os passos abaixo para instalar o Kivy:

**Windows, macOS e Linux:**

```bash
pip install kivy
pip install kivy[base] kivy[gui] kivy[dev]
```

### 2. INSTALAÇÃO DO BUILDOZER PARA ANDROID:
Para compilar seu aplicativo Kivy para Android, você precisa do Buildozer. Isso é feito em um sistema Linux, então, se você estiver no Windows, considere usar o WSL (Windows Subsystem for Linux) ou uma máquina virtual.

**Instalando Buildozer:**

```bash
sudo apt update
sudo apt install -y python3-pip
pip install --user buildozer
```

Você também precisará de algumas dependências:

```bash
sudo apt install -y git zip unzip openjdk-8-jdk
```

## PRIMEIRO PROJETO KIVY:
Vamos criar um projeto simples com Kivy.

### 1. CRIE UM DIRETÓRIO PARA SEU PROJETO:
```bash
mkdir MyKivyApp
cd MyKivyApp
```

### 2. CRIE O ARQUIVO PRINCIPAL `MAIN.PY`:
```python
from kivy.app import App
from kivy.uix.label import Label

class MyKivyApp(App):
    def build(self):
        return Label(text='Hello, Kivy!')

if __name__ == '__main__':
    MyKivyApp().run()
```

### 3. EXECUTE O APLICATIVO:
```bash
python main.py
```

Você deve ver uma janela com a mensagem "Hello, Kivy!".

## COMPILANDO PARA ANDROID:
### 1. INICIALIZE O BUILDOZER:
No diretório do seu projeto, execute:

```bash
buildozer init
```

Isso criará um arquivo `buildozer.spec`.

### 2. EDITE O ARQUIVO `BUILDOZER.SPEC`:
Abra o arquivo `buildozer.spec` e edite os seguintes campos:

```ini
[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
# (Deixe as outras configurações como estão)

[buildozer]
# (Deixe as outras configurações como estão)
```

### 3. COMPILE O APLICATIVO PARA ANDROID:
```bash
buildozer -v android debug
```

O processo pode demorar um pouco. Uma vez concluído, você encontrará o APK em `bin/mykivyapp-0.1-arm64-v8a-debug.apk`.

## COMPILANDO PARA WINDOWS:
Para compilar um aplicativo Kivy para Windows, você pode usar o PyInstaller.

### 1. INSTALE O PYINSTALLER:
```bash
pip install pyinstaller
```

### 2. COMPILE O APLICATIVO:
No diretório do seu projeto, execute:

```bash
pyinstaller --onefile main.py
```

Isso criará um executável na pasta `dist`.

## COMPILANDO PARA LINUX:
A maneira mais simples de distribuir seu aplicativo Kivy no Linux é empacotá-lo como um arquivo standalone usando o PyInstaller.

### 1. COMPILE O APLICATIVO:
No diretório do seu projeto, execute:

```bash
pyinstaller --onefile main.py
```

Isso criará um executável na pasta `dist`.

