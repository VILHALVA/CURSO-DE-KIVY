# SINTAXE
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
