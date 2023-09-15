![logo](https://github.com/SauloMadruga/ChatCSV_App/assets/41789667/03498a6c-ddb0-40e3-8510-453ecf3fd312)

# FIAP - Faculdade de Informática e Administração Paulista

# **HUMAN BASED DATA - TRABALHO FINAL**

# Enunciado

Olá, tudo bem?

Trabalho tem que ser desenvolvido considerando os cenários que foram apresentados durante as aulas:

- LLM: aplicação de GPT + storytelling + explicação + documentação

- Geo Maps: Tableau ou Power BI + storytelling + explicação + documentação

- Natural Language Process: assistente virtual/análise de NPS/analise de feedbacks + storytelling + explicação + documentação

- Computer Vision: detecção de objetos em imagens/análise de camadas + storytelling + explicação + documentação

As bases de dados precisam ter acima de 500 mil registros.

Precisam ser de acesso fácil.

ATENÇÃO QUANDO FOR ENVIAR O TRABALHO PARA ENVIAR TUDO QUE SEJA RELACIONADO.

Se atentar aos requisitos solicitados para evitar perder pontos desnecessariamente pela ausência de entrega.

# Tema escolhido: 
<h1>LLM Aplicação de GPT</h1>

O desafio foi desenvolver um aplicativo utilizando Large Language Model (LLM) que possibilite um usuário importar um arquivo CSV de qualquer tamanho e através de um Chatbot interagir com o documento extraindo informações deste conjunto de dados.

O aplicativo foi denominado ChatCSV_App, desenvolvido em Python e utiliza o Streamlit como interface com o usuário.

# Tecnologias utilizadas
***Streamlit*** é uma biblioteca de código aberto para Python que torna a criação de aplicativos da web interativos e visualizações de dados em Python mais fácil e rápida. É projetado para cientistas de dados, engenheiros de aprendizado de máquina e desenvolvedores que desejam criar aplicativos de análise de dados interativos em um ambiente Python familiar.

Acesse a documentação completa do ***Streamlit*** em: <a  href="https://streamlit.io/"> Clique aqui </a>

Os ***Large Language Models (LLMs)*** são modelos de aprendizado de máquina (*Machine Learning*) que usam algoritmos de aprendizado profundo (*Deep Learning*) para processar e entender a linguagem natural.

Esses modelos são treinados em grandes quantidades de dados de texto para aprender padrões e relacionamentos entre entidades no idioma. Os LLMs podem realizar muitos tipos de tarefas de linguagem, como tradução de idiomas, análise de sentimentos, conversas de chatbot e muito mais. Eles podem entender dados textuais complexos, identificar entidades e relacionamentos entre eles e gerar um novo texto coerente e gramaticalmente preciso.

Os LLMs têm visto uma série de avanços significativos nos últimos anos. Por exemplo, o GPT-3 da OpenAI, lançado em 2020, tem 175 bilhões de parâmetros e ficou famoso ao gerar texto preciso a partir de entradas feitas no ChatGPT. Outras melhorias incluem avanços na compreensão de contexto de longo alcance, a capacidade de gerar respostas mais coerentes e relevantes e a capacidade de entender e responder a uma variedade maior de entradas de texto.

Acesse a documentação completa do ***LLMs OpenAI*** em: <a  href="https://platform.openai.com/docs/models"> Clique aqui </a>

Junto com os LLMs é possível utilizar alguns frameworks dentre eles o ***LangChain***, lançado em outubro de 2022 por [Harrison Chase](https://www.linkedin.com/in/harrison-chase-961287118), tornou-se um dos [frameworks de código aberto mais bem avaliados](https://github.com/langchain-ai/langchain) no GitHub em 2023. Ele oferece uma interface simplificada e padronizada para incorporar modelos de linguagem grande (LLMs) em aplicativos. Ele também fornece uma interface rica em recursos para engenharia imediata, permitindo que os desenvolvedores experimentem diferentes estratégias e avaliem seus resultados.

Acesse a documentação completa do ***LangChain*** em: <a  href="https://python.langchain.com/docs/integrations/llms/openai"> Clique aqui </a>

Com o objetivo de tornar a utilização dos recursos dos modelos LLMs de forma aberta, a OpenAI disponibiliza uma API que tem por objetivo promover o acesso aos recursos que os modelos LLMs oferecem.

Para utilizar a ***API ChatGPT***, é necessário primeiro obter uma chave de acesso (***API key***) que permita o acesso aos recursos da API. Essa chave pode ser obtida através do site oficial da OpenAI.

Gere a sua ***API Key da OpenAI*** aqui: <a  href="https://platform.openai.com/account/api-keys"> Click Here </a>

<br>
<h2> Como rodar a aplicação? </h2>

Se você estiver executando o aplicativo localmente, você poderá configurar a API Key no arquivo api_key.py. <br>

No arquivo ***api_key.py***, linha 1, insira sua chave: <br>

```
API_KEY  =  "sk-##############################"

#Insira a API Key como string
```

A partir de agora, será necessário efetuar o clone do projeto disponível no Github, execute os seguintes comandos:
```
git clone https://github.com/SauloMadruga/ChatCSV_App.git
```
Após o clone do projeto, é necessário ativar o ambiente virtual ***venv*** que foi desenvolvido utilizando o VS Code:
```
cd ChatCSV_App

.\Scripts\Activate.ps1
```
***Obs:*** o comando de ativação pode variar se estiver utilizando o prompt de comando pelo ***CMD*** ou ***PowerShell***.

Após a ativação do ambiente virtual todas a bibliotecas necessárias para rodar o projeto estão contidos no documento *requirements.txt*, execute o código abaixo para a instalação das bibliotecas.
```
pip install -r requirements.txt
```

Com todas as bibliotecas instaladas, basta executar o serviço do Streamlit através do código:
```
streamlit run App.py
```
