# CUSTOMIZAÇÃO DE WIDGETS PELO PYTHON
Em Kivy, você pode personalizar widgets através do Python, seja criando subclasses de widgets existentes ou manipulando propriedades e eventos diretamente. Vou mostrar alguns exemplos de como você pode fazer isso.

## Exemplo 1: Subclasse de Button

```python
from kivy.app import App
from kivy.uix.button import Button

class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        # Adicione personalizações aqui, por exemplo:
        self.font_size = 20
        self.background_color = (0.2, 0.6, 1, 1)

    def on_press(self):
        print("Botão personalizado pressionado!")

class CustomizationApp(App):
    def build(self):
        custom_button = CustomButton(text='Clique em mim!')
        return custom_button

if __name__ == '__main__':
    CustomizationApp().run()
```

Neste exemplo, a classe `CustomButton` é uma subclasse de `Button` que personaliza o tamanho da fonte e a cor de fundo. O método `on_press` é sobrescrito para fornecer um comportamento personalizado quando o botão é pressionado.

## Exemplo 2: Manipulação de Propriedades

```python
from kivy.app import App
from kivy.uix.button import Button

class PropertyManipulationApp(App):
    def build(self):
        button = Button(text='Clique em mim!', font_size=18, background_color=(0.2, 0.6, 1, 1))
        
        # Manipulando propriedades diretamente
        button.font_size = 24
        button.bind(on_press=self.custom_on_press)

        return button

    def custom_on_press(self, instance):
        print("Botão personalizado pressionado!")

if __name__ == '__main__':
    PropertyManipulationApp().run()
```

Neste exemplo, propriedades do botão são manipuladas diretamente no método `build`. Além disso, o método `custom_on_press` é vinculado ao evento `on_press` para fornecer um comportamento personalizado.

Esses são exemplos simples, e você pode personalizar widgets de várias maneiras, dependendo das suas necessidades. Além disso, você pode usar o Kivy Language (KV) para definir a aparência e o comportamento dos widgets de maneira mais declarativa.

Se você precisar de personalizações mais avançadas, considerando criar seu próprio widget personalizado, que pode ser útil para encapsular comportamentos específicos e reutilizáveis em seu aplicativo.