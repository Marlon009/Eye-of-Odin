# Eye of Odin - Advanced OSINT Tool

![Eye of Odin Banner](<img width="840" height="895" alt="odinn3" src="https://github.com/user-attachments/assets/16c72eb4-8981-40fa-927e-4d84dad70eab" />
)

O Eye of Odin é uma ferramenta avançada de OSINT (Open Source Intelligence) inspirada no deus nórdico Odin, conhecido por seu conhecimento e visão. Esta ferramenta oferece uma variedade de módulos para coleta de informações de fontes públicas.

## Recursos Principais

- 🔍 **Rastreamento de IP**: Geolocalização precisa com coordenadas DMS e decimal
- 📞 **Rastreamento de Telefone**: Operadora, região e fuso horário
- 👤 **Busca de Usuário**: Verificação em 100+ redes sociais
- 🌐 **Informações de Domínio**: WHOIS completo e histórico DNS
- 📧 **Verificação de Email**: Checagem de vazamentos em bancos de dados públicos
- 🖼️ **Análise de Imagem**: Extração de metadados EXIF e pesquisa reversa
- 📄 **Análise de Documentos**: Metadados de PDF e DOCX
- ₿ **Rastreamento de Criptomoedas**: Saldo e transações de Bitcoin e Ethereum
- 🕵️ **Busca de Documentos Vazados**: Pesquisa em repositórios públicos
- 🔄 **Pesquisa em Lote**: Múltiplos usuários, emails ou IPs simultaneamente
- 🌐 **Análise de Redes**: IPs associados e subdomínios
- 🧅 **Suporte a Tor**: Conexão anônima opcional
- 📊 **Relatórios**: Geração de relatórios em texto

## Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas Python (listadas em `requirements.txt`)
- Tor (opcional, para uso com proxy)

## Instalação

1. Clone o repositório:
```
git clone https://github.com/Marlon009/eye-of-odin.git
cd eye-of-odin
```

 Instale as dependências:



pip install -r requirements.txt

    (Opcional) Para usar o Tor, instale e inicie o serviço Tor

Uso

Execute o script principal:
bash

python odin.py

O menu principal será exibido:

                                                                            .......             
                                                                          ..............         
                                                                       .......*.....%%....       
                                                                      ...+...**::::::@.....      
                                                                     ....#.::%#::::::@......     
                                                                     ....%::##:.  :#:@*:....     
                                                                     .....***::*  *#:#@:....     
                                                                     .....:#*::*::+*::%*....     
                                           @@@@@@@                   .....:@@:#%*:%%:=@.....     
                                        @@@@@@@@@@@@@                 .....@@..####:#@@....      
                                       @@@@@@@@@@@@@@@                 ....@@..##@..@@@...       
                                     +@@@@@@@@@@@@@@@@%                 ....@@@##..@@@..         
                         %@@@        @@@@@@@@@@@@@@@@@@#                   ...%*#.*#%#           
                       -@@@@@@@@@-  @@@@@@@@@@@@@@@@@@@%                      @#*%##.            
                     @@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@                     #@@@@              
                    :--:-%@@@       @@@@=@@@@=@@@@@@@@%##                     %*%@@              
                  @++-%@:-@@@      @@@%@@###-%@@@@@##@@%#%                    @@*@@              
                 :--::@@@*:@@@     @@@--%=-=%@*@@+++#@@@@#                   @*#@#               
                @@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@                   @@@@               
               --:@++@@@=@@@@     @@@-#@@=--@@*@@@@@@@-@#**                   @*%@               
              --@:@@:@@@@@@@     @@@-@@*@@%@@-@@@@@@@@%@@***                  #@@%@              
             ==@:+#=@@+@@@@     @@@*@@*=-@@=@@@=+@=@%#%-@#**#                  #@#%              
            -:@@%@@@@+@@@@     @@@@@@@@#=+*@@-%@@@@@@%-+@@***+                 @#@@              
           @#@@#:@#=+=@@@      @@@@@@==-@*@@-@@@@@@@%@+@@@@#%%                 @@@@              
         =@@@@@@@@@@@@@@      = @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@              
        @ @#@@@@@@@@    @@ @@@@@@@@@@@@-@=--+@@@@@@@@%-@@**#@#%%%              @@@@              
         @@@@@@@    @+:@#@@@@@@@@%@@@-@@@@=-=+@=@@@@%@@%%@@%*@**#@%            @%@@              
        @@-@@@@:   @***@@%@@@@@@@@@**@@@*#@%%@@@@@@@@@@@%%*#@**@*##%#*      @@=--%@@@@@          
      @@ @@@@@@ #%##*%#**%@@@@@@@@@@-----@@@-+=@@@@@@@@@%#**@**@#*#%@%##+   :-@@=%@@@@@          
        @@@@@  =@%*#**@@@@@@@@@@@@@@:+@#%=:@@@@@@@@@@@@@@%@##%##%#@#%@@@@   @@-+%@@@@@%@         
       @@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#    @@@@@@@@@          
             @@@@@@@@@#***@@@@@@@%#@@-*%=@*@@*%%%@@@@@@@@@@@#***####*####@*: @=-=@@@@@@          
            *****@@@@@@@@@@@@@@@=@@@@@@@@@@@**#@@@@@@@@@%##@@@@###%%#**#%##*  @:#@@@@@@          
           %@@@@@#---@@=@@-@@@@@@-@@@@@@@-@@@@@@@@@@@@@@%@#*%@**#%@@@@@@@@*#@ @@@@@@@@           
           @@@@@@@@@@@@#@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**###*%##%%@ @@@@@@@@          
           @@=@@@-@-==@=@@+@@@@@@@-@@@@@@@@=@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@%%@@=@@#@@@:%%         
           @@@##%+--*---@@%-@@@@@@+-@@@@@@@@-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@%@@@@@@#-@          
          @@@@@@@@@@@@@@@@@%@@@@@@@-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-@=---*--=+@@@@%@@          
  
            ███████╗██╗   ██╗███████╗      ██████╗ ███████╗    ██████╗ ██████╗ ██╗███╗   ██╗
            ██╔════╝╚██╗ ██╔╝██╔════╝     ██╔═══██╗██╔════╝   ██╔═══██╗██╔══██╗██║████╗  ██║
            █████╗   ╚████╔╝ █████╗       ██║   ██║█████╗     ██║   ██║██║  ██║██║██╔██╗ ██║
            ██╔══╝    ╚██╔╝  ██╔══╝       ██║   ██║██╔══╝     ██║   ██║██║  ██║██║██║╚██╗██║
            ███████╗   ██║   ███████╗      ██████╔╝██╝        ╚██████╔╝██████╔╝██║██║ ╚████║
            ╚══════╝   ╚═╝   ╚══════╝      ╚═════╝ ╚═╝         ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                                                                OSINT TOOL
        

                                         github:Marlon009
        
     [SEM-TOR] [+] Menu Principal:
     [1] Rastrear IP
     [2] Rastrear Telefone
     [3] Buscar Usuário
     [4] Informações de Domínio
     [5] Verificar Email (vazamentos)
     [6] Analisando imagem...
     [7] Analisar Documento
     [8] Rastrear Criptomoeda
     [9] Buscar Documentos Vazados
     [10] Pesquisa em Lote
     [11] Analisando rede...
     [12] Alternar Tor
     [13] Gerar Relatório
     [0] Sair
     
     [?] Escolha uma opção: 

Contribuição

Contribuições são bem-vindas! Siga estes passos:

    Faça um fork do projeto

    Crie uma branch para sua feature (git checkout -b feature/incrivel)

    Faça commit das suas alterações (git commit -m 'Adiciona feature incrível')

    Faça push para a branch (git push origin feature/incrivel)

    Abra um Pull Request

Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
Contato

Desenvolvedor: Marlon


## Exemplos de Uso

### Rastrear um IP
```bash
Escolha uma opção: 1
[?] Digite o IP: 8.8.8.8

[i] Informação para 8.8.8.8:
- País: United States
- Cidade: Mountain View
- Provedor: Google LLC
- Mapa (Decimal): https://www.google.com/maps/@37.4056,-122.0785,8z
- Mapa (DMS): https://www.google.com/maps/place/37°24'20.2"N+122°4'42.6"W/
