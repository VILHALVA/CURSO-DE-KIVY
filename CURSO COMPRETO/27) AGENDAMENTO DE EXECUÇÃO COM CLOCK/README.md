# AGENDAMENTO DE EXECUÇÃO COM CLOCK
Em Kivy, você pode agendar a execução de funções periodicamente usando a classe `Clock`. O `Clock` permite que você crie eventos agendados e execute funções em intervalos específicos. Aqui está um exemplo básico de como usar o `Clock` para agendar a execução de uma função a cada segundo:

```python
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class ClockExampleApp(App):
    def build(self):
        # Cria um rótulo para exibir a contagem
        self.label = Label(text="0")
        
        # Agenda a execução da função update_label a cada segundo
        Clock.schedule_interval(self.update_label, 1)

        return self.label

    def update_label(self, dt):
        # Função chamada a cada segundo
        current_count = int(self.label.text)
        new_count = current_count + 1
        self.label.text = str(new_count)

if __name__ == '__main__':
    ClockExampleApp().run()
```

Neste exemplo:

- `ClockExampleApp` é a classe principal do aplicativo.
- Um rótulo (`Label`) é criado para exibir a contagem.
- A função `update_label` é definida para ser chamada a cada segundo.
- `Clock.schedule_interval(self.update_label, 1)` agenda a execução da função a cada segundo.

Quando você executa este aplicativo, o rótulo será atualizado a cada segundo com a contagem incrementada.

Além do `Clock.schedule_interval`, você também pode usar outros métodos do `Clock` como `Clock.schedule_once` para agendar uma única execução após um determinado tempo.

Lembre-se de que, ao usar o `Clock`, é importante lidar com a parada adequada dos eventos agendados, especialmente quando o aplicativo é fechado. Isso pode ser feito usando `Clock.unschedule` para cancelar a execução agendada.

```python
def on_stop(self):
    # Cancela todos os eventos agendados quando o aplicativo é fechado
    Clock.unschedule(self.update_label)
```

Isso garante que os eventos do `Clock` sejam tratados de forma adequada ao fechar o aplicativo.