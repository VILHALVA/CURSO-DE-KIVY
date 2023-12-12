# EVENTOS VARIÁVEIS DA INSTÂNCIA
No Kivy, é possível acessar e manipular propriedades da instância dentro de uma função de evento. Isso é feito referenciando a instância do widget (`self`) dentro da função associada ao evento. Vou mostrar um exemplo simples em que alteramos o texto de um rótulo (Label) ao clicar em um botão, usando uma variável da instância.

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Cria um layout de caixa horizontal
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Adiciona um rótulo (Label) ao layout
        self.label = Label(text='Clique no botão para alterar o texto.')
        layout.add_widget(self.label)

        # Adiciona um botão (Button) ao layout
        button = Button(text='Clique em mim!')
        # Associa a função on_button_click ao evento on_press do botão
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # Altera o texto do rótulo usando uma variável da instância
        self.label.text = 'Texto alterado pelo clique no botão!'

if __name__ == '__main__':
    MyApp().run()
```

Neste exemplo, o rótulo inicializa com um texto padrão. Quando o botão é clicado, a função `on_button_click` é chamada, e dentro dessa função, a propriedade `text` do rótulo (`self.label.text`) é alterada para um novo valor.

Isso demonstra como você pode acessar e modificar propriedades da instância de widgets dentro das funções de evento. Essa abordagem é útil para atualizar dinamicamente a interface do usuário em resposta a eventos específicos.

Adapte esse exemplo conforme necessário para atender aos requisitos específicos do seu aplicativo. Se tiver mais perguntas ou precisar de mais ajuda, sinta-se à vontade para perguntar!