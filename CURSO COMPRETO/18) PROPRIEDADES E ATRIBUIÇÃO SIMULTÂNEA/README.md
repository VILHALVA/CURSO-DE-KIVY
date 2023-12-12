# PROPRIEDADES E ATRIBUIÇÃO SIMULTÂNEA
Em Kivy, as propriedades são utilizadas para definir e controlar os atributos de widgets. É possível realizar atribuições simultâneas de propriedades utilizando a sintaxe do Python. Vou fornecer um exemplo para ilustrar isso:

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class PropertyAssignmentApp(App):
    def build(self):
        # Criando uma instância de BoxLayout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Criando botões com atribuições simultâneas de propriedades
        button1, button2 = Button(text='Botão 1', size_hint=(None, None), size=(100, 50)), Button(text='Botão 2', size_hint=(None, None), size=(100, 50))

        # Atribuição simultânea de propriedades usando a sintaxe do Python
        button1.background_color, button2.background_color = (1, 0, 0, 1), (0, 1, 0, 1)
        button1.font_size, button2.font_size = 20, 24

        # Adicionando os botões ao layout
        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout

if __name__ == '__main__':
    PropertyAssignmentApp().run()
```

Neste exemplo:

- Dois botões (`button1` e `button2`) são criados simultaneamente, utilizando a sintaxe do Python para atribuição múltipla.
- Propriedades como `background_color` e `font_size` são atribuídas simultaneamente a ambos os botões.

Essa técnica de atribuição simultânea pode ser útil para simplificar o código, especialmente quando você está configurando várias propriedades em um conjunto de objetos semelhantes.

Lembre-se de que a escolha de usar ou não atribuições simultâneas depende do contexto e da legibilidade do código. Use-a quando achar que isso melhora a clareza e a concisão do código.