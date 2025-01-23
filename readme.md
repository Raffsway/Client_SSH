# README - SSH Client

## Descrição

Este script Python cria um cliente SSH persistente com um terminal interativo, permitindo a comunicação com um servidor remoto via SSH. O terminal permite enviar e receber comandos de forma interativa e segura, utilizando o `paramiko` para a conexão SSH e `msvcrt` para leitura interativa do teclado.

## Funcionalidades

- Conexão SSH segura com o servidor remoto.
- Abertura de um shell interativo para execução de comandos.
- Leitura da saída do servidor e envio de comandos do usuário.
- Uso de `CTRL + C` para encerrar a sessão.

## Requisitos

- Python 3.x
- Biblioteca `paramiko` para SSH (instalar via `pip install paramiko`).
- Sistema operacional que suporte `msvcrt` (geralmente Windows).

## Como Usar

1. Execute o script Python no terminal.
2. Informe o IP do servidor, o nome de usuário e a senha quando solicitado.
3. Após a conexão bem-sucedida, você será redirecionado para um shell interativo.
4. Digite comandos para serem executados no servidor remoto.
5. Pressione `CTRL + C` para encerrar a sessão e desconectar.

## Exemplo de Uso

```bash
python ssh.py
```

### Exemplo de interação:
```
Digite o IP do servidor: 192.168.1.10
Digite o nome de usuário: admin
Digite a senha: ********
Conectando ao servidor 192.168.1.10...
Conexão estabelecida com sucesso! Use CTRL + C para encerrar a conexão.
Shell interativo iniciado. Pressione CTRL + C para encerrar.
$ ls
...
$ exit
Encerrando conexão...
Conexão encerrada com sucesso.
```

## Funções

### `interactive_shell(channel)`

Cria um shell interativo, recebendo e enviando dados entre o servidor e o cliente.

### `ssh_persistent_client(server_ip, username, password)`

Estabelece uma conexão SSH persistente com o servidor e inicia o shell interativo.

## Notas

- Certifique-se de que o servidor esteja configurado para aceitar conexões SSH.
- O script utiliza autenticação por senha.