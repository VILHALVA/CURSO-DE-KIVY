# LINGUAGEM KIVY
A linguagem Kivy (KV) é uma linguagem de marcação utilizada para definir interfaces de usuário no framework Kivy. Ela permite que você descreva a estrutura e o comportamento da interface de maneira declarativa, separando a lógica de apresentação do código Python subjacente. Aqui estão alguns conceitos básicos da linguagem KV:

1. **Declaração de Widgets:**
   - Você pode declarar widgets diretamente na linguagem KV, sem a necessidade de criar instâncias de widgets no código Python.
   - O nome do widget na linguagem KV deve coincidir com o nome da classe do widget em Python.

   Exemplo:
   ```yaml
   # No código Python, a classe é 'Label', então aqui também é 'Label'
   Label:
       text: 'Olá, Kivy!'
   ```

2. **Propriedades e Vinculação de Propriedades:**
   - Você pode definir propriedades e vincular expressões a elas.
   - A vinculação de propriedades é feita usando a sintaxe `property: value`.

   Exemplo:
   ```yaml
   Label:
       text: 'Olá, ' + root.nome
   ```

   No exemplo acima, assumindo que a classe Python tem uma propriedade chamada `nome`, a expressão `root.nome` vincula o texto do rótulo à propriedade `nome` da instância pai (raiz).

3. **Referências e IDs:**
   - Você pode atribuir um ID a um widget para referenciá-lo posteriormente no código Python.
   - A sintaxe é `id: nome_do_id`.

   Exemplo:
   ```yaml
   BoxLayout:
       Button:
           id: meu_botao
           text: 'Clique em mim!'
   ```

   Você pode então referenciar esse botão no código Python usando `self.ids.meu_botao`.

4. **Triggers e Estados:**
   - Triggers são usados para definir ações a serem realizadas quando um evento ocorre.
   - Estados podem ser usados para definir diferentes aparências ou comportamentos com base nas condições do aplicativo.

   Exemplo:
   ```yaml
   Button:
       text: 'Clique em mim!'
       on_press: root.funcao_no_python()
   ```

   Isso chama a função `funcao_no_python()` quando o botão é pressionado.

5. **Comentários:**
   - Comentários em KV começam com `#`.

   Exemplo:
   ```yaml
   # Isto é um comentário
   Label:
       text: 'Conteúdo do rótulo'
   ```

Esses são apenas conceitos básicos. A linguagem KV oferece muito mais, incluindo animações, transições, e a capacidade de criar layouts complexos de maneira mais concisa do que seria possível apenas com código Python. Para aprender mais, consulte a documentação oficial do Kivy sobre a linguagem KV: https://kivy.org/doc/stable/guide/lang.html