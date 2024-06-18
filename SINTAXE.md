# SINTAXE
## ESTRUTURA BÁSICA DE UM PROGRAMA KIVY:
Aqui está um exemplo simples de um aplicativo Kivy:

```python
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello, Kivy!')

if __name__ == '__main__':
    MyApp().run()
```

## COMPONENTES BÁSICOS:
### LAYOUTS:
Layouts são fundamentais para organizar widgets na tela. Alguns dos layouts mais usados são `BoxLayout`, `GridLayout` e `FloatLayout`.

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Button 1'))
        layout.add_widget(Button(text='Button 2'))
        layout.add_widget(Button(text='Button 3'))
        return layout

if __name__ == '__main__':
    MyApp().run()
```

### WIDGETS:
Widgets são os componentes visuais que compõem a interface do usuário.

```python
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Click Me')

if __name__ == '__main__':
    MyApp().run()
```

## ARQUIVO KV:
Kivy permite separar a lógica da interface utilizando arquivos `.kv`. Aqui está um exemplo:

### MYAPP.KV:
```kv
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'Button 1'
    Button:
        text: 'Button 2'
    Button:
        text: 'Button 3'
```

### MAIN.PY:
```python
from kivy.app import App

class MyApp(App):
    pass

if __name__ == '__main__':
    MyApp().run()
```

## MANIPULAÇÃO DE EVENTOS:
Eventos são cruciais para interatividade. Você pode adicionar eventos a widgets de forma simples:

```python
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        button = Button(text='Click Me')
        button.bind(on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        print('Button clicked!')

if __name__ == '__main__':
    MyApp().run()
```



