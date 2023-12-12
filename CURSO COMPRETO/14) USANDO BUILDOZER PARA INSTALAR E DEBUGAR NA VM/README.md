# USANDO BUILDOZER PARA INSTALAR E DEBUGAR NA VM
Se você está usando uma máquina virtual (VM) para desenvolvimento Kivy e deseja usar o buildozer para instalar e debugar o aplicativo em um dispositivo Android virtual, aqui estão os passos gerais a serem seguidos:

1. **Configuração da VM:**
   Certifique-se de que a VM está configurada corretamente para suportar a execução de aplicativos Android. Isso geralmente envolve a instalação do Android Studio ou de outro ambiente de desenvolvimento Android na VM.

2. **Instalação do Buildozer:**
   Certifique-se de ter o buildozer instalado na VM. Use o seguinte comando para instalá-lo:

   ```bash
   pip install buildozer
   ```

3. **Configuração do Projeto:**
   Certifique-se de que seu projeto Kivy esteja configurado corretamente na VM. O arquivo `buildozer.spec` deve ser configurado com as opções apropriadas para a plataforma Android. Certifique-se de especificar os requisitos corretos para as dependências do seu projeto.

4. **Configuração do Dispositivo Virtual:**
   Se você estiver usando um emulador Android na VM, inicie o emulador antes de executar os comandos do buildozer.

5. **Compilação e Instalação:**
   Execute o seguinte comando na pasta do seu projeto para compilar e instalar o aplicativo no dispositivo Android virtual:

   ```bash
   buildozer -v android debug deploy
   ```

   O parâmetro `debug` indica o modo de compilação, e `deploy` indica que você deseja instalar o aplicativo após a compilação.

6. **Execução em Modo Debug:**
   Para depurar o aplicativo no dispositivo virtual, use o seguinte comando:

   ```bash
   buildozer android adb -- logcat
   ```

   Isso iniciará o utilitário `adb` (Android Debug Bridge) em modo de logcat para visualizar mensagens de log do aplicativo.

Lembre-se de que os detalhes específicos podem variar dependendo da sua configuração e da VM que está usando. Certifique-se de consultar a documentação do Kivy e do Buildozer para obter informações mais detalhadas e ajustar as configurações conforme necessário.

Além disso, observe que a execução de emuladores Android em uma VM pode ser lenta dependendo das configurações e recursos disponíveis na VM. Considere usar um dispositivo físico para um desempenho mais rápido.