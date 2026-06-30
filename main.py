import streamlit as st

def main():
    st.header("Chatbot Simples", divider = True, text_alignment = "center")
    st.markdown("Selecione a IA que mais vai te ajudar, envie seu prompt e seja feliz!")

    opcoes = ["Gerar Texto", "Resumir Texto", "Abrir Chat"]
    opcao_selecionada = st.selectbox("Selecione a ferramenta desejada: ", options = opcoes)

    if opcao_selecionada:
        prompt_usuario = st.chat_input("Digite seu prompt aqui: ")

        if opcao_selecionada == opcoes[0]:
            pass
        elif opcao_selecionada == opcoes[1]:
            pass
        elif opcao_selecionada == opcoes[2]:
            pass
        
if __name__ == "__main__":
    main()