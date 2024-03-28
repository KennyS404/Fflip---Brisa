let chat = document.querySelector('#chat');
let input = document.querySelector('#input');
let botaoEnviar = document.querySelector('#botao-enviar');

async function enviarMensagem() {
    // Verifica se a entrada está vazia para evitar enviar mensagens vazias.
    if(input.value.trim() === "") return;

    let mensagem = input.value;
    input.value = "";

    // Cria e adiciona a bolha de mensagem do usuário ao chat.
    let novaBolha = criaBolhaUsuario();
    novaBolha.innerHTML = mensagem; // Insere o texto do usuário na bolha.
    chat.appendChild(novaBolha);

    // Cria e adiciona uma bolha temporária para o bot, indicando que está processando.
    let novaBolhaBot = criaBolhaBot();
    novaBolhaBot.innerHTML = "Analisando ...";
    chat.appendChild(novaBolhaBot);
    vaiParaFinalDoChat();

    // Envia a mensagem do usuário para a API do chatbot e aguarda a resposta.
    const resposta = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({'msg': mensagem}),
    });

    // Assumindo que a resposta é um texto direto, como ajustado no backend.
    const textoDaResposta = await resposta.text();

    // Atualiza a bolha do bot com a resposta recebida.
    novaBolhaBot.innerHTML = textoDaResposta.replace(/\n/g, '<br>');
    vaiParaFinalDoChat();
}

function criaBolhaUsuario() {
    let bolha = document.createElement('p');
    bolha.className = 'chat__bolha chat__bolha--usuario'; // Ajuste para className.
    return bolha;
}

function criaBolhaBot() {
    let bolha = document.createElement('p');
    bolha.className = 'chat__bolha chat__bolha--bot'; // Ajuste para className.
    return bolha;
}

function vaiParaFinalDoChat() {
    chat.scrollTop = chat.scrollHeight; // Auto-scroll para a mensagem mais recente.
}

botaoEnviar.addEventListener('click', enviarMensagem);

// Adiciona um evento para permitir o envio da mensagem com a tecla Enter.
input.addEventListener("keyup", function(event) {
    if (event.key === "Enter") { // Ajuste para "Enter" ao invés de verificar keyCode.
        event.preventDefault();
        botaoEnviar.click();
    }
});
