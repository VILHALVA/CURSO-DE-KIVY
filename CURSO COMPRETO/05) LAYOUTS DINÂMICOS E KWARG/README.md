# LAYOUTS DINÂMICOS E KWARG
Em Kivy, você pode criar layouts dinâmicos usando contêineres como `BoxLayout`, `GridLayout`, ou `FloatLayout`. Além disso, os layouts dinâmicos frequentemente envolvem a manipulação de propriedades e argumentos keyword (KWARG) no código Python.

Aqui, vou mostrar um exemplo de como criar um aplicativo Kivy com um layout dinâmico usando `BoxLayout` e também como passar argumentos keyword (KWARG) para personalizar o comportamento de widgets.

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class DynamicBoxLayoutApp(App):
    def build(self):
        # Cria um layout de caixa vertical
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Adiciona botões ao layout usando um loop
        for i in range(5):
            # Cria um botão com um texto e um argumento keyword (KWARG)
            button = Button(
                text=f'Botão {i}',
                on_press=self.on_button_click,  # Associa a função ao evento on_press
                custom_value=i  # Argumento keyword (KWARG) personalizado
            )
            layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # Função chamada quando um botão é pressionado
        button_number = instance.custom_value
        print(f"Botão {button_number} clicado!")

if __name__ == '__main__':
    DynamicBoxLayoutApp().run()
```

Neste exemplo, estamos criando uma classe de aplicativo Kivy chamada `DynamicBoxLayoutApp`. O método `build` cria um layout de caixa vertical (`BoxLayout`) e adiciona cinco botões a ele usando um loop. Cada botão tem um texto indicando seu número e um argumento keyword personalizado chamado `custom_value`.

Quando um botão é pressionado, a função `on_button_click` é chamada, e ela imprime o número do botão no console com base no valor do `custom_value`. Isso demonstra como você pode personalizar o comportamento de widgets usando argumentos keyword.

