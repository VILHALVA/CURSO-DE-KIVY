# MÚLTIPLAS TELAS COM SCREENMANAGER
O `ScreenManager` no Kivy é um gerenciador de tela que permite criar aplicativos com várias telas. Cada tela (`Screen`) contém seu próprio conteúdo e pode ser alternada de forma programática ou interativa pelo usuário. Vamos criar um exemplo básico com duas telas usando o `ScreenManager`.

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text='Tela Principal')
        button = Button(text='Ir para a Segunda Tela', on_press=self.change_screen)

        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)

    def change_screen(self, *args):
        # Muda para a segunda tela
        self.manager.current = 'second'

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text='Segunda Tela')
        button = Button(text='Voltar para a Primeira Tela', on_press=self.change_screen)

        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)

    def change_screen(self, *args):
        # Muda para a primeira tela
        self.manager.current = 'main'

class MultiScreenApp(App):
    def build(self):
        # Cria o gerenciador de telas
        sm = ScreenManager()

        # Adiciona as telas ao gerenciador de telas
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))

        return sm

if __name__ == '__main__':
    MultiScreenApp().run()
```

Neste exemplo:

- Criamos duas classes de tela (`MainScreen` e `SecondScreen`) que herdam de `Screen`.
- Cada classe de tela contém um layout com um rótulo e um botão.
- O método `change_screen` em cada classe altera a tela atual usando `self.manager.current`.
- O `ScreenManager` é usado para gerenciar as telas. Adicionamos instâncias de `MainScreen` e `SecondScreen` ao `ScreenManager`.

Ao executar este exemplo, você verá uma tela principal com um botão. Quando você clica no botão, a tela muda para a segunda tela, e vice-versa.

Este é um exemplo básico de como criar um aplicativo com várias telas usando o `ScreenManager`. Você pode expandir isso adicionando mais telas, personalizando o conteúdo de cada tela e associando ações específicas a eventos de botões. 