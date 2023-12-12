# CRIANDO UM MENU COM IMAGEM
Para criar um menu com imagem no Kivy, você pode utilizar um `BoxLayout` horizontal ou vertical para organizar os botões do menu. Cada botão pode conter um `Image` e/ou um `Label`. Vou criar um exemplo simples de um menu horizontal com botões contendo imagens.

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class MenuApp(App):
    def build(self):
        # Cria um layout de caixa horizontal para o menu
        menu_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        # Adiciona botões ao menu
        button1 = self.create_menu_button('Botão 1', 'image1.png')
        button2 = self.create_menu_button('Botão 2', 'image2.png')
        button3 = self.create_menu_button('Botão 3', 'image3.png')

        # Adiciona os botões ao layout do menu
        menu_layout.add_widget(button1)
        menu_layout.add_widget(button2)
        menu_layout.add_widget(button3)

        return menu_layout

    def create_menu_button(self, text, image_source):
        # Cria um botão para o menu com uma imagem e um rótulo
        button = Button(size_hint=(None, 1), width=100, height=100)

        # Adiciona uma imagem ao botão
        image = Image(source=image_source, size=(50, 50), size_hint=(None, None))
        button.add_widget(image)

        # Adiciona um rótulo ao botão
        label = Button(text=text, background_color=(0, 0, 0, 0), size_hint=(None, None))
        button.add_widget(label)

        return button

if __name__ == '__main__':
    MenuApp().run()
```

Neste exemplo:

- Criamos uma classe `MenuApp` que herda de `App`.
- No método `build`, criamos um `BoxLayout` horizontal para organizar os botões do menu.
- Para cada botão, usamos o método `create_menu_button` que cria um botão com uma imagem e um rótulo.
- O método `create_menu_button` recebe o texto do rótulo e o caminho da imagem como parâmetros.

Certifique-se de substituir `'image1.png'`, `'image2.png'`, e `'image3.png'` pelos caminhos reais das suas imagens. Essas imagens devem estar no mesmo diretório do seu script Python ou você deve fornecer o caminho completo.

