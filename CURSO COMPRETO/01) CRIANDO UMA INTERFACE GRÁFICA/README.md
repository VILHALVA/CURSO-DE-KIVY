# CRIANDO UMA INTERFACE GRÁFICA
Para criar uma interface gráfica com o Kivy, você precisará entender alguns conceitos básicos, como widgets, layouts e a linguagem de marcação KV. Vou fornecer um exemplo simples de um aplicativo Kivy que possui uma interface gráfica básica.

1. **Widget Raiz e Layout:**

Vamos criar um aplicativo com um layout básico. Neste exemplo, usaremos um `BoxLayout` para organizar os widgets na horizontal. O widget raiz será um `BoxLayout`, e dentro dele, adicionaremos um `Label` e um `Button`.

```python
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
```

2. **Linguagem KV:**

Você também pode definir a interface gráfica usando a linguagem de marcação KV, que é uma maneira declarativa de descrever a interface sem precisar programar em Python. O arquivo KV deve ter o mesmo nome que o aplicativo Python (no caso, `myapp.py` e `myapp.kv`).

```python
# Conteúdo do arquivo myapp.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        return BoxLayout()

if __name__ == '__main__':
    MyApp().run()
```

```yaml
# Conteúdo do arquivo myapp.kv
<BoxLayout>:
    orientation: 'horizontal'
    spacing: 10
    padding: 10

    Label:
        text: 'Olá, Kivy!'

    Button:
        text: 'Clique em mim!'
```

3. **Executando o Aplicativo:**

Certifique-se de salvar os arquivos no mesmo diretório. Execute o arquivo Python (`myapp.py`) para iniciar o aplicativo:

```bash
python myapp.py
```

Este exemplo cria uma interface com um rótulo e um botão organizados horizontalmente. Você pode explorar outros widgets, layouts e propriedades para criar interfaces mais complexas e interativas.