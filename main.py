import streamlit as st
from summarization import resumir_texto
from generation import gerar_texto

def main():
    st.header("Chatbot Simples", divider = True, text_alignment = "center")
    st.markdown("Selecione a IA que mais vai te ajudar, envie seu prompt e seja feliz!")

    opcoes = ["Gerar Texto", "Resumir Texto", "Abrir Chat"]
    opcao_selecionada = st.selectbox("Selecione a ferramenta desejada: ", options = opcoes)

    if opcao_selecionada:
        prompt_usuario = st.chat_input("Digite seu prompt aqui: ")
        
        if prompt_usuario:
          st.write(f"Prompt do usuário: {prompt_usuario}")

          if opcao_selecionada == opcoes[0]:
              texto = gerar_texto(prompt_usuario)
              st.write(texto)
          elif opcao_selecionada == opcoes[1] and prompt_usuario:
              resumo = resumir_texto(prompt_usuario)
              st.write(resumo)
          elif opcao_selecionada == opcoes[2] and prompt_usuario:
              pass
        
if __name__ == "__main__":
    main()