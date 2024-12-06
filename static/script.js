document.getElementById("get-ip-btn").addEventListener("click", () => {
    fetch('/get_ip')
        .then(response => response.json())
        .then(data => {
            document.getElementById("ip-result").innerText = `Seu IP Local: ${data.ip}`;
        })
        .catch(error => {
            console.error("Erro ao obter IP:", error);
        });
});

document.getElementById("check-specific-port").addEventListener("click", () => {
    const port = prompt("Digite o número da porta a ser verificada:");
    if (port) {
        fetch(`/check_port?port=${port}`)
            .then(response => response.json())
            .then(data => {
                const status = data.open ? "aberta" : "fechada";
                document.getElementById("result-output").innerText = `Porta ${port} está ${status}.`;
            })
            .catch(error => {
                console.error("Erro ao verificar porta:", error);
            });
    }
});

document.getElementById("check-common-ports").addEventListener("click", () => {
    fetch('/check_common_ports')
        .then(response => response.json())
        .then(data => {
            const output = data.open_ports.map(portData => {
                const riskInfo = portData.status === "aberta" 
                    ? `Risco: ${portData.risk}` 
                    : "Porta fechada.";
                return `Porta ${portData.port} (${portData.description}): ${portData.status}\n${riskInfo}`;
            }).join("\n");
            document.getElementById("result-output").innerText = `Portas comuns:\n${output}`;
        })
        .catch(error => {
            console.error("Erro ao verificar portas comuns:", error);
        });
});

