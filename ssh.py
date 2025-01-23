import paramiko
import getpass
import msvcrt

def interactive_shell(channel):
    """
    Função para criar um shell interativo simples usando SSH.
    """
    print("Shell interativo iniciado. Pressione CTRL + C para encerrar.")
    
    try:
        while True:
            # Recebe a saída do servidor
            if channel.recv_ready():
                data = channel.recv(1024)
                if data:
                    print(data.decode("utf-8", errors="ignore"), end="")  # Exibe a saída recebida

            # Lê a entrada do usuário e envia para o servidor
            if msvcrt.kbhit():
                input_char = msvcrt.getch()
                if input_char == b'\x03':  # CTRL + C
                    print("\nEncerrando conexão...")
                    break
                channel.send(input_char.decode("utf-8"))
    except Exception as e:
        print(f"Erro: {e}")

def ssh_persistent_client(server_ip, username, password):
    """
    Cliente SSH persistente com funcionalidade de terminal interativo real.
    """
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print(f"Conectando ao servidor {server_ip}...")
        client.connect(hostname=server_ip, username=username, password=password)
        print("Conexão estabelecida com sucesso! Use CTRL + C para encerrar a conexão.")
        
        # Cria um canal interativo
        channel = client.invoke_shell()
        print(channel.recv(4096).decode("utf-8"), end="")  # Exibe o banner inicial
        
        # Inicia o shell interativo
        interactive_shell(channel)
        
        # Fecha o canal e a conexão
        channel.close()
        client.close()
        print("Conexão encerrada com sucesso.")
    
    except paramiko.AuthenticationException:
        print("Falha na autenticação. Verifique o usuário e senha.")
    except paramiko.SSHException as e:
        print(f"Erro no SSH: {e}")
    except Exception as e:
        print(f"Erro geral: {e}")

if __name__ == "__main__":
    try:
        server_ip = input("Digite o IP do servidor: ")
        username = input("Digite o nome de usuário: ")
        password = getpass.getpass("Digite a senha: ")
        ssh_persistent_client(server_ip, username, password)
    except KeyboardInterrupt:
        print("\nEncerrando o programa.")
