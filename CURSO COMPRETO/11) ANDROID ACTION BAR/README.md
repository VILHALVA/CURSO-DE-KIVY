# ANDROID ACTION BAR
A Action Bar é uma parte essencial da interface do usuário em aplicativos Android. Ela fornece um local para ações comuns, como navegação, pesquisa e operações de aplicativos. No Kivy, você pode criar uma interface semelhante à Action Bar usando layouts e widgets específicos. Vou mostrar um exemplo básico de como você pode criar um layout que se assemelha a uma Action Bar no Kivy.

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ActionBarApp(App):
    def build(self):
        # Cria um layout de caixa horizontal para a Action Bar
        action_bar_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10, size_hint_y=None, height=50)

        # Adiciona widgets à Action Bar
        button1 = Button(text='Ação 1', on_press=self.action1)
        button2 = Button(text='Ação 2', on_press=self.action2)
        label = Label(text='Título da Aplicação', size_hint_x=None, width=200)

        # Adiciona os widgets ao layout da Action Bar
        action_bar_layout.add_widget(button1)
        action_bar_layout.add_widget(button2)
        action_bar_layout.add_widget(label)

        # Cria o layout principal da aplicação
        main_layout = BoxLayout(orientation='vertical')

        # Adiciona a Action Bar ao layout principal
        main_layout.add_widget(action_bar_layout)

        return main_layout

    def action1(self, instance):
        print("Ação 1 executada!")

    def action2(self, instance):
        print("Ação 2 executada!")

if __name__ == '__main__':
    ActionBarApp().run()
```

Neste exemplo:

- Criamos um layout de caixa horizontal (`action_bar_layout`) para representar a Action Bar.
- Adicionamos botões (`button1` e `button2`) e um rótulo (`label`) à Action Bar.
- Criamos um layout principal (`main_layout`) de caixa vertical para incluir a Action Bar.

Os métodos `action1` e `action2` são associados aos eventos de pressionar dos botões, e eles imprimem mensagens no console quando os botões são pressionados. Você pode personalizar esses métodos para executar as ações desejadas.

