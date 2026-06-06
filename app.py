import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="J.A.R.V.I.S",
    page_icon="🤖",
    layout="centered"
)

st.title("🦾 J.A.R.V.I.S")
st.caption("Assistente futurista - Sempre ao seu dispor, senhor")

respostas = {
    "oi": "Olá! Como posso ajudar você hoje?",
    "olá": "Olá! Como posso ajudar você hoje?",
    "bom dia": "Bom dia! Pronto para mais um dia incrível?",
    "boa tarde": "Boa tarde! Em que posso ser útil?",
    "boa noite": "Boa noite! Como vai?",
    "nome": "Meu nome é J.A.R.V.I.S, ao seu dispor!",
    "como você está": "Estou funcionando a 100% de capacidade!",
    "quem criou você": "Fui criado por um desenvolvedor foda!",
    "obrigado": "Disponha! Sempre aqui pra ajudar.",
    "tchau": "Até mais! Foi um prazer servir.",
}

if "historico" not in st.session_state:
    st.session_state.historico = []

for msg in st.session_state.historico:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.historico.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    texto = prompt.lower().strip()
    resposta = None

    for chave, resp in respostas.items():
        if chave in texto:
            resposta = resp
            break

    if "hora" in texto:
        resposta = f"Agora são **{datetime.now().strftime('%H:%M')}**."
    elif "data" in texto or "hoje" in texto:
        resposta = f"Hoje é **{datetime.now().strftime('%d/%m/%Y')}**."

    if resposta is None:
        resposta = "Ainda não sei responder isso... Mas você pode me ensinar adicionando no código!"

    with st.chat_message("assistant"):
        st.markdown(resposta)
    
    st.session_state.historico.append({"role": "assistant", "content": resposta})
