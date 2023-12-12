# Conteúdo do arquivo myapp.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        return BoxLayout()

if __name__ == '__main__':
    MyApp().run()
