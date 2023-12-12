# CRIANDO UM POPUP
Em Kivy, você pode criar pop-ups utilizando a classe `Popup`. Os pop-ups são janelas modais que aparecem sobre o conteúdo principal da aplicação. Aqui está um exemplo básico de como criar um pop-up em Kivy:

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class PopupExampleApp(App):
    def build(self):
        # Cria um botão que exibirá o pop-up quando pressionado
        button = Button(text='Abrir Pop-up', on_press=self.show_popup)

        return button

    def show_popup(self, instance):
        # Cria uma instância do pop-up
        popup = Popup(title='Exemplo de Pop-up',
                      content=Label(text='Isso é um pop-up!'),
                      size_hint=(None, None), size=(300, 200))

        # Adiciona um botão ao pop-up
        close_button = Button(text='Fechar Pop-up', size_hint=(None, None), size=(150, 50))
        close_button.bind(on_press=popup.dismiss)
        popup.content.add_widget(close_button)

        # Exibe o pop-up
        popup.open()

if __name__ == '__main__':
    PopupExampleApp().run()
```

Neste exemplo:

- `PopupExampleApp` é a classe principal do aplicativo.
- Um botão é criado no método `build`, e o método `show_popup` é associado ao evento `on_press` do botão.
- No método `show_popup`, uma instância de `Popup` é criada com um título e conteúdo definidos.
- Um botão "Fechar Pop-up" é adicionado ao conteúdo do pop-up, e o método `dismiss` do pop-up é vinculado ao evento `on_press` do botão para fechar o pop-up.
- Finalmente, o pop-up é exibido usando o método `open()`.

Este é um exemplo simples, e você pode personalizar o conteúdo, o tamanho e o comportamento do pop-up conforme necessário para o seu aplicativo. 