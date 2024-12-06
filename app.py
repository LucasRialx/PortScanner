from flask import Flask, jsonify, request, render_template
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

@app.route('/get_ip')
def get_ip():
    return jsonify({"ip": get_local_ip()})

@app.route('/check_port')
def check_port():
    port = int(request.args.get('port'))
    ip = get_local_ip()
    return jsonify({"open": scan_port(ip, port)})

@app.route('/check_common_ports')
def check_common_ports():
    common_ports = {
        80: {"description": "HTTP", "risk": "Permite acesso ao site sem criptografia. Pode ser vulnerável a ataques como Man-in-the-Middle (MITM)."},
        443: {"description": "HTTPS", "risk": "Garante a criptografia do tráfego da web, essencial para segurança. Manter aberto é geralmente seguro, mas precisa de manutenção adequada."},
        21: {"description": "FTP", "risk": "Protocólo antigo e inseguro para transferência de arquivos. Deixar aberto pode permitir acesso não autorizado e vazamento de dados."},
        22: {"description": "SSH", "risk": "Usado para login remoto seguro, mas se mal configurado ou exposto na internet, pode ser alvo de ataques de força bruta."},
        25: {"description": "SMTP", "risk": "Usado para envio de e-mails. Pode ser explorado por spammers se não for adequadamente protegido."},
        53: {"description": "DNS", "risk": "Pode ser alvo de ataques de DDoS (negação de serviço) e manipulação de tráfego DNS, o que pode resultar em phishing ou outros ataques."},
        161: {"description": "SNMP", "risk": "Protocólo de gerenciamento de rede. Deixar aberto pode permitir a obtenção de informações sensíveis e controle remoto da rede."},
        139: {"description": "NetBIOS", "risk": "Vulnerável a ataques de invasão em redes Windows, especialmente quando exposto na internet."},
        445: {"description": "SMB", "risk": "Usado para compartilhamento de arquivos. Vulnerável a ataques como o WannaCry (ransomware) se mal configurado."},
        3389: {"description": "RDP", "risk": "Protocólo de desktop remoto. Se exposto na internet, pode ser alvo de ataques de força bruta e exploração de falhas."},
        25565: {"description": "Minecraft", "risk": "Porta usada por servidores de Minecraft. Deixar aberta pode resultar em ataques DDoS ou exploração de vulnerabilidades no servidor."},
        9987: {"description": "TeamSpeak", "risk": "Usado para comunicação de voz em grupo. Pode ser explorado para ataques de negação de serviço (DoS)."},
        27015: {"description": "Steam", "risk": "Usado para jogos online, pode ser alvo de DDoS ou exploração de falhas de segurança no servidor."},
        1194: {"description": "OpenVPN", "risk": "Protocólo de VPN. Deixar aberta sem criptografia adequada pode comprometer a segurança da rede."},
        1723: {"description": "PPTP", "risk": "Protocólo de VPN antigo e vulnerável. Deixar aberto pode expor a rede a ataques."},
        500: {"description": "IKE", "risk": "Parte de uma implementação de VPN. Se mal configurado, pode ser alvo de ataques de quebra de segurança."}
    }

    ip = get_local_ip()
    results = [
        {
            "port": port,
            "description": data["description"],
            "status": "aberta" if scan_port(ip, port) else "fechada",
            "risk": data["risk"]
        }
        for port, data in common_ports.items()
    ]
    return jsonify({"open_ports": results})


if __name__ == "__main__":
    app.run(debug=True)
