'''
Disciplina:     HUMAN-BASED DATA
Professor:      NILTON KAZUYUKI UEDA

Descrição:  Olá, tudo bem?

        Trabalho tem que ser desenvolvido considerando os cenários que foram apresentados durante as aulas:

        - LLM: aplicação de GPT + storytelling + explicação + documentação
        - Geo Maps: Tableau ou Power BI  + storytelling + explicação + documentação
        - Natural Language Process: assistente virtual/análise de NPS/analise de feedbacks  + storytelling + explicação + documentação
        - Computer Vision: detecção de objetos em imagens/análise de camadas + storytelling + explicação + documentação

        As bases de dados precisam ter acima de 500 mil registros.
        Precisam ser de acesso fácil.
        ATENÇÃO QUANDO FOR ENVIAR O TRABALHO PARA ENVIAR TUDO QUE SEJA RELACIONADO.
        Se atentar aos requisitos solicitados para evitar perder pontos desnecessariamente pela ausencia de entrega.

Desenvolvedores:    SAULO NOBRE MADRUGA
                    MARCUS VINICIUS PIRES OLIVEIRA
                    CLARA SOUZA DE OLIVEIRA

Versão:             v1.0

Data:               15/09/2023
'''

# Importando as bibliotecas do projeto
import streamlit as st
from streamlit_chat import message
from streamlit import chat_message
import os
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from api_key import API_KEY


# Global Variables Configuration
ICON =      "./files/icon.png"
LOGO =      "./files/logo.png"
APP_NAME =  "ChatCSV Assistant | FIAP | 3DTS"
TITLE =     "Chat:red[CSV] Assistent"
SUBTITLE =  "Seu assistente de consultas!"
ABOUT =     "Aplicativo desenvolvido para a disciplina de Human-Based Data do curso de MBA em DataScience da FIAP/Paulista."
INFO =      "3DTS - MBA em DataScience"



# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = API_KEY

@st.cache(show_spinner=False)

def btn_limpa_historico():
    del st.session_state.messages


# Criando a classe do aplicativo
def ChatCSV_APP():
    # Configurações gerais
    st.set_page_config(
        page_title=APP_NAME,
        page_icon=ICON,
        initial_sidebar_state="auto",
        layout="wide",
        menu_items={'About': ABOUT}
    )

    # Layout da Página
    with st.container():
        pg_col1, pg_col2 = st.columns([1, 3])
        with pg_col1:
            st.image(LOGO, use_column_width='auto')
            original_title = f"""<p style="text-align: center;
                                font-family:Verdana;
                                color:rgb(236,20,92); 
                                font-size: 18px;
                                ">{INFO}</p>"""
            st.markdown(original_title, unsafe_allow_html=True)
    
        with pg_col2:
            st.title(TITLE)
            pg_col2.subheader(SUBTITLE)
    st.markdown("""---""")

    # Upload do arquivo CSV
    file =  st.file_uploader("Faça o Upload do arquivo CSV:",type=["csv"])
    if not file:
        st.stop()

    data = pd.read_csv(file)

    if file:
        st.success("Arquivo CSV carregado com sucesso!")
        def load_data():
            agent = create_pandas_dataframe_agent(OpenAI(temperature=0),data,verbose=True)
            return agent

        agent = load_data()

    # Visualização prévia dos dados
    with st.expander("Visualização prévia dos dados:", expanded=True):
        st.dataframe(data.sample(5))

    st.markdown("""---""")

    # Inicializa o Chat com a mensagem do assistente
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant",
             "content": "Olá! Seja bem vindo(a)! Faça a sua pergunta sobre o dataset."}]

    # Cria o ambiente do chat
    chat_placeholder = st.empty()
    with chat_placeholder.container():    
        if prompt := st.chat_input("Faça sua pergunta:"): # Prompt for user input and save to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

        for message in st.session_state.messages: # Display the prior chat messages
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # If last message is not from assistant, generate a new response
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Pensando..."):
                    answer = agent.run(prompt)
                    st.write(answer)
                    message = {"role": "assistant", "content": answer}
                    # Adiciona a resposta ao histórico
                    st.session_state.messages.append(message)
        st.markdown("""---""")
        st.button("Limpar histórico", on_click=btn_limpa_historico)
          


if __name__ == '__main__':
    ChatCSV_APP()
