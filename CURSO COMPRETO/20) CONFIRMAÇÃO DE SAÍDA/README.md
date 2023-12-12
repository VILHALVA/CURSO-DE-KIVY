# CONFIRMAÇÃO DE SAÍDA
Para criar uma confirmação de saída em Kivy, você pode usar um pop-up com dois botões: um para confirmar a saída e outro para cancelar a ação. Aqui está um exemplo:

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class ExitConfirmationApp(App):
    def build(self):
        # Cria um botão que exibirá a confirmação de saída quando pressionado
        button = Button(text='Sair', on_press=self.show_exit_confirmation)

        return button

    def show_exit_confirmation(self, instance):
        # Cria uma instância do pop-up de confirmação de saída
        exit_popup = Popup(title='Confirmação de Saída',
                           content=Label(text='Deseja realmente sair?'),
                           size_hint=(None, None), size=(300, 200))

        # Adiciona botões ao pop-up
        confirm_button = Button(text='Sim', size_hint=(None, None), size=(150, 50))
        cancel_button = Button(text='Cancelar', size_hint=(None, None), size=(150, 50))

        # Vincula os eventos de pressionar aos botões
        confirm_button.bind(on_press=self.confirm_exit)
        cancel_button.bind(on_press=exit_popup.dismiss)

        # Adiciona os botões ao conteúdo do pop-up
        exit_popup.content.add_widget(confirm_button)
        exit_popup.content.add_widget(cancel_button)

        # Exibe o pop-up
        exit_popup.open()

    def confirm_exit(self, instance):
        print("Saindo do aplicativo.")
        App.get_running_app().stop()  # Encerra o aplicativo

if __name__ == '__main__':
    ExitConfirmationApp().run()
```

Neste exemplo, quando o botão "Sair" é pressionado, um pop-up de confirmação é exibido com os botões "Sim" e "Cancelar". Se o botão "Sim" for pressionado, a função `confirm_exit` é chamada, que encerra o aplicativo.

