# CURSO DE KIVY
👨‍⚖️KIVY É UM FRAMEWORK PYTHON DE CÓDIGO ABERTO USADO PARA DESENVOLVIMENTO DE APLICATIVOS MULTIPLATAFORMA, INCLUINDO ANDROID, IOS, WINDOWS, LINUX E OUTROS. ELE PERMITE CRIAR INTERFACES DE USUÁRIO INTERATIVAS E ATRATIVAS USANDO A LINGUAGEM PYTHON. 

[![GitHub Repo stars](https://img.shields.io/badge/VILHALVA-GITHUB-03A9F4?logo=github)](https://github.com/VILHALVA) 
[![GitHub Repo stars](https://img.shields.io/badge/VEJA%20OS-VIDEOS-03A9F4?logo=youtube)](https://www.youtube.com/@vilhalva100/search?query=KIVY)

[![GitHub Repo stars](https://img.shields.io/badge/VEJA-DOCUMENTAÇÃO-03A9F4?logo=google)](https://kivy.org/doc/stable/) 
[![GitHub Repo stars](https://img.shields.io/badge/LINGUAGEM%20DE-PROGRAMAÇÃO-03A9F4?logo=google)](https://github.com/VILHALVA/CURSO-DE-PYTHON)
<br>

[![GitHub Repo stars](https://img.shields.io/badge/-PLAYLIST%20DO%20YOUTUBE-blueviolet)](https://youtube.com/playlist?list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&si=s_Ry13XMexk6nFdS)

<img src="https://upload.wikimedia.org/wikipedia/commons/5/58/Kivy_logo.png" align="center" width="280"> <br>

![](https://i.imgur.com/waxVImv.png)

# CONCEITO:
Kivy é um framework de código aberto em Python para o desenvolvimento de aplicativos multi-touch. Ele é projetado para ser multiplataforma, o que significa que você pode criar aplicativos que funcionam em dispositivos com diferentes sistemas operacionais, como Android, iOS, Windows, Linux e macOS.

A principal característica do Kivy é a sua capacidade de criar interfaces de usuário interativas e agradáveis, especialmente em dispositivos com telas sensíveis ao toque. Ele oferece uma abstração eficiente para lidar com entrada multi-touch, gestos e outros recursos específicos de dispositivos móveis.

Principais conceitos do Kivy:

1. **Widgets:** Kivy usa uma hierarquia de widgets para construir interfaces de usuário. Widgets são componentes gráficos, como botões, caixas de texto, rótulos, etc. Eles são organizados em uma árvore de widgets para criar a estrutura da interface.

2. **Propriedades e Eventos:** Os widgets no Kivy têm propriedades que podem ser vinculadas a expressões e eventos que podem ser manipulados. Isso permite que você crie interfaces dinâmicas e responsivas.

3. **Layouts:** Kivy oferece vários layouts para organizar e posicionar widgets de maneira eficiente. Alguns exemplos incluem BoxLayout, GridLayout e FloatLayout.

4. **Kv Language:** Além de criar interfaces em Python, o Kivy oferece uma linguagem de marcação chamada KV, que permite definir a interface de usuário de forma declarativa, separando a lógica de apresentação do código Python.

5. **Event Handling:** Kivy permite lidar com eventos de entrada, como toques, cliques e gestos, para criar interações intuitivas.

Aqui está um exemplo simples de código Kivy para criar uma aplicação com um botão:

```python
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Olá, Kivy!')

if __name__ == '__main__':
    MyApp().run()
```

Este código cria um aplicativo Kivy com uma janela contendo um único botão que exibe o texto "Olá, Kivy!". Você pode expandir esse exemplo para construir interfaces mais complexas e interativas. 