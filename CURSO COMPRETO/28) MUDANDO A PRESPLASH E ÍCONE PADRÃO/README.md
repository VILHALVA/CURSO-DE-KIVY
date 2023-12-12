# MUDANDO A PRESPLASH E ÍCONE PADRÃO
Para mudar a imagem de *presplash* (tela de inicialização) e o ícone padrão de um aplicativo Kivy, você precisa fornecer os arquivos de imagem apropriados e ajustar o arquivo de especificação de construção (geralmente chamado `build.spec`) se estiver usando o Buildozer para compilar seu aplicativo.

Vamos abordar cada um desses aspectos:

### Mudando a *Presplash*:

1. **Substituir a imagem:**
   - Substitua a imagem padrão de *presplash* (`images/icon.png`) por sua própria imagem personalizada.
   - A imagem deve ser nomeada exatamente como `presplash.png` e deve ter as dimensões adequadas.

2. **Adicionar ao Buildozer (se aplicável):**
   - Se você estiver usando o Buildozer para empacotar seu aplicativo, certifique-se de incluir a imagem personalizada no arquivo de especificação de construção (`build.spec`).

   ```ini
   # build.spec
   source.include_exts = py,png,jpg,kv,atlas
   source.include_patterns = images/*.png
   ```

### Mudando o Ícone Padrão:

1. **Substituir o ícone:**
   - Substitua o ícone padrão (`images/icon.png`) por sua própria imagem personalizada.
   - A imagem deve ser nomeada exatamente como `icon.png` e deve ter as dimensões adequadas.

2. **Adicionar ao Buildozer (se aplicável):**
   - Se você estiver usando o Buildozer, certifique-se de incluir o ícone personalizado no arquivo de especificação de construção (`build.spec`).

   ```ini
   # build.spec
   source.include_exts = py,png,jpg,kv,atlas
   source.include_patterns = images/*.png
   ```

3. **Definir Ícone no Manifesto (para Android):**
   - Se você estiver construindo para Android, você também precisará definir o ícone no manifesto. Adicione o seguinte ao arquivo `build.spec`:

   ```ini
   # build.spec
   android.icon = images/icon.png
   ```

   Certifique-se de que o caminho para o ícone está correto.

### Exemplo de Estrutura de Diretório:

```
- YourApp/
  - main.py
  - images/
    - presplash.png
    - icon.png
  - build.spec
```

Lembre-se de substituir `YourApp` pelo nome do seu próprio aplicativo. Certifique-se de seguir as convenções de nomeação corretas para a imagem de *presplash* e o ícone. Depois de fazer essas alterações, você deve ver a imagem de *presplash* e o ícone personalizado quando construir e executar seu aplicativo.