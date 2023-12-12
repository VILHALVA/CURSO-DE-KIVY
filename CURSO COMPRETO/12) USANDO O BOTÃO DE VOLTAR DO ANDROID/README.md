# USANDO O BOTÃO DE VOLTAR DO ANDROID
Para capturar o evento de pressionar o botão de voltar no Android em um aplicativo Kivy, você precisa usar a classe `on_keyboard` do Kivy e, em seguida, verificar se o evento corresponde ao código da tecla de retorno (`27`). Aqui está um exemplo de como você pode fazer isso:

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BackButtonApp(App):
    def build(self):
        # Cria um layout de caixa vertical
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Adiciona um botão ao layout
        button = Button(text='Pressione o botão de voltar do Android')
        button.bind(on_press=self.on_button_press)

        # Adiciona o botão ao layout
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        print("Botão pressionado!")

    def on_keyboard(self, window, key, *args):
        # Captura o evento de pressionar o botão de voltar no Android (código da tecla 27)
        if key == 27:
            print("Botão de voltar pressionado!")
            return True  # Indica que o evento foi tratado

        return False

    def on_start(self):
        # Adiciona o manipulador de teclado ao iniciar o aplicativo
        self._keyboard = self.window.request_keyboard(self.on_keyboard, self)
        self._keyboard.bind(on_key_down=self.on_keyboard)

if __name__ == '__main__':
    BackButtonApp().run()
```

Neste exemplo:

- Utilizamos a classe `BoxLayout` para criar um layout simples com um botão.
- O método `on_button_press` é chamado quando o botão é pressionado.
- O método `on_keyboard` é utilizado para capturar o evento de pressionar o botão de voltar do Android.
- No método `on_start`, adicionamos o manipulador de teclado ao iniciar o aplicativo.

Certifique-se de testar este código em um dispositivo Android real, pois alguns emuladores podem ter comportamentos diferentes em relação ao botão de voltar.

Esse exemplo fornece uma maneira de lidar com o evento de pressionar o botão de voltar no Android em um aplicativo Kivy. Personalize conforme necessário para atender às suas necessidades específicas. 