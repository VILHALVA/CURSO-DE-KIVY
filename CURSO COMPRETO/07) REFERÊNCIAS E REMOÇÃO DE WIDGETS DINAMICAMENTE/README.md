# REFERÊNCIAS E REMOÇÃO DE WIDGETS DINAMICAMENTE
Quando você está trabalhando com widgets dinâmicos em Kivy, pode ser útil ter referências a esses widgets para posterior manipulação ou remoção. Vou demonstrar como adicionar referências e como remover widgets dinamicamente do exemplo anterior.

Vamos adicionar um botão "Remover" que, quando clicado, remove o último botão adicionado à `ScrollView`.

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ScrollApp(App):
    def build(self):
        # Cria um layout de caixa vertical
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Cria uma área rolável (ScrollView)
        scroll_view = ScrollView()

        # Cria um layout de caixa vertical dentro da ScrollView
        self.scroll_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=500)

        # Adiciona muitos botões ao layout dentro da ScrollView
        for i in range(50):
            button = Button(text=f'Botão {i}', size_hint_y=None, height=40)
            self.scroll_layout.add_widget(button)

        # Adiciona o layout da ScrollView à ScrollView
        scroll_view.add_widget(self.scroll_layout)

        # Adiciona a ScrollView ao layout principal
        layout.add_widget(scroll_view)

        # Adiciona um botão "Remover"
        remove_button = Button(text='Remover Último', on_press=self.remove_last_button)
        layout.add_widget(remove_button)

        return layout

    def remove_last_button(self, instance):
        # Remove o último botão da ScrollView
        if self.scroll_layout.children:
            self.scroll_layout.remove_widget(self.scroll_layout.children[-1])

if __name__ == '__main__':
    ScrollApp().run()
```

Neste exemplo:

- `self.scroll_layout` é definido como uma variável de instância para que possamos referenciá-la posteriormente.
- O método `remove_last_button` é associado ao evento `on_press` do botão "Remover".
- Dentro do método `remove_last_button`, verificamos se há botões filhos no `scroll_layout` e, se houver, removemos o último botão.

Esse é um exemplo simples, mas você pode aplicar conceitos semelhantes a situações mais complexas. Lembre-se de que, ao remover widgets, é importante garantir que a manipulação do layout seja feita de maneira segura, evitando erros de referência ou lógica incorreta.

