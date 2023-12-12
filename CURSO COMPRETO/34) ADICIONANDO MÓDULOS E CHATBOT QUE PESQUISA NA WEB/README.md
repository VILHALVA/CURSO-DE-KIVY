# ADICIONANDO MÓDULOS E CHATBOT QUE PESQUISA NA WEB
Para criar um chatbot em Kivy que pesquisa na web, você pode seguir alguns passos gerais. Primeiro, você precisará de um módulo para o chatbot e, em seguida, integrar uma funcionalidade de pesquisa na web. Vamos dar uma visão geral simples desses passos:

### 1. **Chatbot em Kivy:**

Vamos usar uma biblioteca simples de chatbot chamada `ChatterBot`. Certifique-se de instalá-la primeiro:

```bash
pip install chatterbot
```

Aqui está um exemplo básico de como você pode criar um chatbot em Kivy:

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class ChatBotApp(App):
    def build(self):
        self.bot = ChatBot('Meu ChatBot')

        # Use um treinador para treinar o chatbot com o corpus em inglês
        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train('chatterbot.corpus.english')

        layout = BoxLayout(orientation='vertical')
        self.input_box = TextInput()
        send_button = Button(text='Enviar', on_press=self.send_message)
        self.output_box = TextInput(readonly=True)

        layout.add_widget(self.output_box)
        layout.add_widget(self.input_box)
        layout.add_widget(send_button)

        return layout

    def send_message(self, instance):
        user_input = self.input_box.text
        self.input_box.text = ''

        bot_response = self.bot.get_response(user_input)
        self.output_box.text += f'\nVocê: {user_input}\nBot: {bot_response}'

if __name__ == '__main__':
    ChatBotApp().run()
```

### 2. **Adicionando Pesquisa na Web:**

Para adicionar uma funcionalidade de pesquisa na web, você pode usar a biblioteca `googlesearch-python`. Certifique-se de instalá-la primeiro:

```bash
pip install googlesearch-python
```

Aqui está um exemplo simples de como você pode integrar a pesquisa na web ao seu chatbot:

```python
from googlesearch import search

# Dentro da classe ChatBotApp, adicione este método
def search_web(self, query):
    search_results = search(query, num=5, stop=5, pause=2)
    results_str = '\n'.join(search_results)
    return f'Resultados da Pesquisa:\n{results_str}'
```

Altere o método `send_message` para chamar a função `search_web` quando o usuário faz uma pergunta que inicia com um comando especial, como "pesquisar":

```python
def send_message(self, instance):
    user_input = self.input_box.text
    self.input_box.text = ''

    if user_input.lower().startswith('pesquisar'):
        query = user_input[9:]  # Remove o comando de pesquisa
        bot_response = self.search_web(query)
    else:
        bot_response = self.bot.get_response(user_input)

    self.output_box.text += f'\nVocê: {user_input}\nBot: {bot_response}'
```

Esses são exemplos básicos, e você pode expandir essas funcionalidades de acordo com suas necessidades específicas. Lembre-se de que a pesquisa na web deve ser usada de acordo com os termos de serviço do mecanismo de pesquisa. Além disso, a segurança é uma consideração importante ao lidar com entrada do usuário e dados da web.