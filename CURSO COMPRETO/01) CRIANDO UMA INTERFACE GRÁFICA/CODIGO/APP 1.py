from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Cria um layout de caixa horizontal
        layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        # Adiciona um rótulo (Label) ao layout
        label = Label(text='Olá, Kivy!')
        layout.add_widget(label)

        # Adiciona um botão (Button) ao layout
        button = Button(text='Clique em mim!')
        layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()
