# BOTAO COM IMAGEM
Se você deseja adicionar um botão com uma imagem em Kivy, pode usar a classe `Button` e adicionar um widget de imagem a ele. Aqui está um exemplo básico:

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image

class ImageButtonExampleApp(App):
    def build(self):
        # Cria um botão com uma imagem
        button = Button(
            background_normal='',  # Remove o fundo padrão do botão
            background_down='',    # Remove o fundo quando pressionado
            on_press=self.on_button_press  # Função chamada quando o botão é pressionado
        )

        # Adiciona uma imagem ao botão
        image = Image(source='caminho/para/sua/imagem.png')
        button.add_widget(image)

        return button

    def on_button_press(self, instance):
        print("Botão pressionado!")

if __name__ == '__main__':
    ImageButtonExampleApp().run()
```

Certifique-se de substituir `'caminho/para/sua/imagem.png'` pelo caminho real para sua própria imagem.

Neste exemplo, `background_normal` e `background_down` são definidos como cadeias vazias para que o botão não tenha uma aparência padrão e, em vez disso, mostre apenas a imagem.

Lembre-se de ajustar o tamanho, a posição e outros atributos conforme necessário para atender às suas preferências de design e requisitos do aplicativo.