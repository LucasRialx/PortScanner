import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"Erro ao obter IP local: {e}")
        return None

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except socket.error as e:
        print(f"Erro: {e}")
        return False

def main():
    local_ip = get_local_ip()
    if local_ip:
        print(f"Seu IP local é: {local_ip}")
    else:
        print("Não foi possível obter o IP local.")
        return

    print("Escolha uma opção:")
    print("1. Verificar uma porta específica")
    print("2. Verificar portas comuns")
    choice = input("Digite 1 ou 2: ")

    if choice == '1':
        port = int(input("Digite o número da porta a ser verificada: "))
        if scan_port(local_ip, port):
            print(f"Porta {port} aberta")
        else:
            print(f"Porta {port} fechada")

    elif choice == '2':
        common_ports = {
            80: "HTTP",
            443: "HTTPS",
            21: "FTP",
            22: "SSH",
            25: "SMTP",
            53: "DNS",
            161: "SNMP",
            139: "NetBIOS",
            445: "SMB",
            3389: "RDP",
            25565: "Minecraft",
            9987: "TeamSpeak",
            27015: "Steam",
            1194: "OpenVPN",
            1723: "PPTP",
            500: "IKE"
        }

        print("Portas comuns disponíveis:")
        for port, service in common_ports.items():
            print(f"Porta {port}: {service}")

        ports_to_check = list(common_ports.keys())
        open_ports = []

        for port in ports_to_check:
            if scan_port(local_ip, port):
                print(f"Porta {port} ({common_ports[port]}) aberta")
                open_ports.append(port)
            else:
                print(f"Porta {port} ({common_ports[port]}) fechada")

        print(f"\nPortas abertas: {open_ports}")

    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
