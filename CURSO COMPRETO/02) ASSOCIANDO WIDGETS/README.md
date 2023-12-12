# ASSOCIANDO WIDGETS
Associar widgets no Kivy é uma parte essencial para tornar sua interface gráfica interativa. Você pode associar ações a eventos, como cliques em botões. Vou mostrar como associar a função de impressão a um botão como exemplo.

Vamos expandir o exemplo anterior para incluir um botão que, quando clicado, imprimirá uma mensagem no console.

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
        # Associa a função on_button_click ao evento on_press do botão
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # Função chamada quando o botão é pressionado
        print("Botão clicado!")

if __name__ == '__main__':
    MyApp().run()
```

Neste exemplo, a função `on_button_click` é associada ao evento `on_press` do botão usando o método `bind`. A função recebe um parâmetro `instance`, que é uma referência ao próprio botão. Dentro da função, estamos simplesmente imprimindo uma mensagem no console.

Ao executar este código, você verá que cada vez que o botão é pressionado, a mensagem "Botão clicado!" é exibida no console.

Você pode associar diferentes funções a diferentes eventos (`on_touch_down`, `on_touch_up`, etc.) e também pode passar parâmetros adicionais se necessário. Essa associação é uma maneira poderosa de criar interfaces reativas e responsivas. Experimente adaptar este exemplo para atender às suas necessidades específicas!