# Port Scanner

Este é um simples script em Python que realiza a verificação de portas em um endereço IP local. Ele permite que você escolha entre verificar uma porta específica ou realizar a verificação em portas comuns.

## Funcionalidades

- Obtém o IP local da máquina.
- Permite verificar se uma porta específica está aberta.
- Verifica as portas comuns e informa quais estão abertas.

## Portas Comuns Verificadas

O script verifica as seguintes portas comuns:

- **HTTP** (Porta 80)
- **HTTPS** (Porta 443)
- **FTP** (Porta 21)
- **SSH** (Porta 22)
- **SMTP** (Porta 25)
- **DNS** (Porta 53)
- **SNMP** (Porta 161)
- **NetBIOS** (Porta 139)
- **SMB** (Porta 445)
- **RDP** (Porta 3389)
- **Minecraft** (Porta 25565)
- **TeamSpeak** (Porta 9987)
- **Steam** (Porta 27015)
- **OpenVPN** (Porta 1194)
- **PPTP** (Porta 1723)
- **IKE** (Porta 500)

## Como Usar

1. **Clone o repositório:**
````
git clone https://github.com/LucasRialx/PortScanner.git
````
2. **Navegue até o diretório do projeto:**
```
cd nome-do-repositorio
```

3. **Execute o script:**
```
python port_scanner.py
```
4. **Escolha uma das opções:**

Verificar uma porta específica.
Verificar as portas comuns.
Exemplo de Uso
Ao executar o script, você verá algo assim:

```
Seu IP local é: 192.168.1.10
Escolha uma opção:
1. Verificar uma porta específica
2. Verificar portas comuns
Digite 1 ou 2: 1
Digite o número da porta a ser verificada: 80
Porta 80 aberta
```

## Requisitos
Python 3.x

## Licença
Este projeto está licenciado sob a MIT License.
