# ADICIONANDO WIDGETS DINAMICAMENTE E TEXTINPUT
Vamos expandir ainda mais o exemplo para adicionar widgets dinamicamente e incluir `TextInput`. Vou mostrar como adicionar `TextInput` junto com botões dinamicamente e como obter os valores inseridos no `TextInput`.

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

class ScrollApp(App):
    def build(self):
        # Cria um layout de caixa vertical
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Cria uma área rolável (ScrollView)
        scroll_view = ScrollView()

        # Cria um layout de caixa vertical dentro da ScrollView
        self.scroll_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=500)

        # Adiciona muitos botões e TextInput ao layout dentro da ScrollView
        for i in range(5):
            button = Button(text=f'Botão {i}', size_hint_y=None, height=40)
            self.scroll_layout.add_widget(button)

            text_input = TextInput(text=f'Texto {i}', multiline=False, height=40)
            self.scroll_layout.add_widget(text_input)

        # Adiciona o layout da ScrollView à ScrollView
        scroll_view.add_widget(self.scroll_layout)

        # Adiciona um botão "Adicionar" para adicionar dinamicamente
        add_button = Button(text='Adicionar', on_press=self.add_widgets)
        layout.add_widget(add_button)

        return layout

    def add_widgets(self, instance):
        # Adiciona dinamicamente um botão e um TextInput à ScrollView
        new_button = Button(text=f'Botão Novo', size_hint_y=None, height=40)
        self.scroll_layout.add_widget(new_button)

        new_text_input = TextInput(text=f'Texto Novo', multiline=False, height=40)
        self.scroll_layout.add_widget(new_text_input)

    def on_text_input_change(self, instance, value):
        # Função chamada quando o texto em um TextInput é alterado
        print(f'Texto alterado: {value}')

if __name__ == '__main__':
    ScrollApp().run()
```

Neste exemplo:

- Adicionamos `TextInput` para cada conjunto de botão e `TextInput` existente.
- Adicionamos um botão "Adicionar" que chama a função `add_widgets` quando pressionado.
- A função `add_widgets` adiciona dinamicamente um novo botão e um novo `TextInput` à `ScrollView`.

Você pode observar que a função `on_text_input_change` está configurada para ser chamada quando o texto em um `TextInput` é alterado. Essa função pode ser associada ao evento `on_text` do `TextInput` para realizar ações adicionais quando o texto é alterado.

