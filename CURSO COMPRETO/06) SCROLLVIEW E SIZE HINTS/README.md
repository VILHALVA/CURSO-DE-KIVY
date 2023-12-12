# SCROLLVIEW E SIZE HINTS
`ScrollView` é um widget no Kivy que permite a criação de áreas roláveis, úteis quando o conteúdo de uma interface excede o tamanho da tela. `Size Hints` (dicas de tamanho) referem-se às propriedades que ajudam o Kivy a decidir como alocar espaço para os widgets em um layout. Vou criar um exemplo combinando `ScrollView` e `Size Hints`.

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
        scroll_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=500)

        # Adiciona muitos botões ao layout dentro da ScrollView
        for i in range(50):
            button = Button(text=f'Botão {i}', size_hint_y=None, height=40)
            scroll_layout.add_widget(button)

        # Adiciona o layout da ScrollView à ScrollView
        scroll_view.add_widget(scroll_layout)

        # Adiciona a ScrollView ao layout principal
        layout.add_widget(scroll_view)

        return layout

if __name__ == '__main__':
    ScrollApp().run()
```

Neste exemplo:

- Um `BoxLayout` vertical (`layout`) é criado como o layout principal do aplicativo.
- Um `ScrollView` é criado e adicionado ao layout principal.
- Um segundo `BoxLayout` vertical (`scroll_layout`) é criado dentro da `ScrollView`.
- Muitos botões são adicionados ao `scroll_layout`.
- `size_hint_y=None` e `height` são usados para definir a altura fixa do `scroll_layout` na direção y.
- Cada botão dentro do `scroll_layout` tem uma altura fixa de 40 pixels.

A combinação de `ScrollView` e `size_hint` é poderosa para criar interfaces que podem acomodar conteúdo variável e permitir a rolagem quando o espaço não é suficiente.
