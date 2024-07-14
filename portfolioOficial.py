import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(layout="wide")

# Barra lateral
with st.sidebar:
    st.markdown('<h1>Meu Portfólio</h1>', unsafe_allow_html=True)
    st.markdown('<a href="#inicio">Início</a>', unsafe_allow_html=True)
    st.markdown('<a href="#sobre">Sobre</a>', unsafe_allow_html=True)
    st.markdown('<a href="#projetos">Projetos</a>', unsafe_allow_html=True)
    st.markdown('<a href="#contato">Contato</a>', unsafe_allow_html=True)

# HTML para incluir Bootstrap Icons CSS
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Função auxiliar para criar títulos de abas com ícones
def conteiner_with_icon(icon, label):
    return f'<div class="tab-title"><i class="bi bi-{icon}"></i> {label}</div>'

# Seção Início
st.write('---')
with st.container():
    st.markdown('<a id="inicio"></a>', unsafe_allow_html=True)
    col1_inicio, col2_inicio = st.columns(2)

    with col1_inicio:
        st.markdown(conteiner_with_icon('house', ' '), unsafe_allow_html=True)
        st.subheader("Olá! :wave:")
        st.title("Meu Site de Portfólio")
        st.subheader("Bem-vindo ao meu portfólio.")
        st.write("""
            \nSou Makaya Afonso, um profissional apaixonado por ciência de dados, automação, visualização de dados, gestão de negócios e acima de tudo resolver problemas.
            \nAqui você encontrará informações sobre minha formação, experiência profissional e projetos, se despertar interesses entre em contato comigo.
            \nTake Your Time:blush:!
        """)

    with col2_inicio:
        st.image("pc_image.gif", caption=" ", use_column_width=True)

st.write('---')

# Seção Sobre
with st.container():
    st.markdown('<a id="sobre"></a>', unsafe_allow_html=True)
    st.markdown(conteiner_with_icon('person', 'Sobre'), unsafe_allow_html=True)

    col1_sobre, col2_sobre, col3_sobre = st.columns(3)

    with col1_sobre:
        st.subheader("Formação Acadêmica")
        st.markdown("""
            - Universidade Cruzeiro do Sul            
                - **Curso:** Ciência da Computação         
                - **Grade**: 4°Semestre
                - **Previsão de Término:** 2026
        """)

    with col2_sobre:
        st.subheader("Experiência Profissional")
        st.markdown("""
        - **Empresa:** American Tower
          - **Duração:** (5/2023 - Emprego atual)
          - **Área:** IT Business Partner
          - **Cargo:** Estagiário
          - **Detalhes:**
            - Gestão de Negócio.
            - Tratamento de Dados com Oracle Analytics, ODV e Excel.
            - Elaboração de Relatórios com Power BI.
            - Automação de Processos com Python.
        """)

    with col3_sobre:
        st.write("### Habilidades e Ferramentas")
        st.write("""
            - **Linguagens e Bibliotecas:** Python, Pandas, Flask, NumPy, SciPy, Matplotlib, Scikit-learn, TensorFlow, Keras, BeautifulSoup, Requests, PyTorch, Seaborn, Plotly, Dash, Jupyter, OpenCV, NLTK, Spacy, XGBoost, LightGBM, Bokeh, Altair, Django, Apache Spark, CustomTkinter, FFmpeg, OpenAI.
            - **Ferramentas de Visualização:** Power BI, Oracle Data Visualization, Excel, Python.
            - **Gestão de Dados:** MySQL, Oracle.
            - **Metodologias Ágeis:** Scrum.
            - **Outras Habilidades:** Trabalho em equipe, proatividade, aprendizado contínuo, IA e ML, comunicação eficaz, gerenciamento de projetos.
        """)

    # Gráfico de Barras
    skills = ['Python', 'Power BI', 'SQL', 'Machine Learning', 'Oracle Data Visualization', 'Power Automate', 'Power App']
    skill_levels = [95, 85, 80, 75, 70, 90, 90]

    fig = go.Figure(data=[go.Bar(x=skills, y=skill_levels, marker_color='royalblue')])
    fig.update_layout(title_text='Minhas Habilidades em %', xaxis_title='Habilidade', yaxis_title='Nível')
    st.plotly_chart(fig)

st.write('---')

# Seção Projetos
with st.container():
    st.markdown('<a id="projetos"></a>', unsafe_allow_html=True)
    st.markdown(conteiner_with_icon('code-slash', 'Projetos'), unsafe_allow_html=True)
    st.write("""
        Aqui estão alguns dos meus projetos mais recentes:

        - **Relatórios Interativos com Power BI:** Desenvolvimento de dashboards que apresentam insights e análises de dados relevantes para o negócio.
        - **Automação de Processos com Python:** Projetos de automação que aumentam a eficiência operacional.
        - **Análise de Dados com Oracle Analytics e Excel:** Tratamento e transformação de dados para análises precisas.

        **Escolha uma categoria para saber mais:**
    """)
    with st.container():
        selected = option_menu(menu_title=None, options=['BI', 'Apps', 'Automações', 'Meus Vídeos'], icons=['graph-up', 'app', 'robot', 'youtube'], orientation='horizontal')

        if selected == 'BI':
            st.markdown("### 3 Relatórios")
            col1, col2, col3 = st.columns(3)

            # Primeiro lugar
            with col1:
                st.markdown("### Power BI")
                st.image("dash1.png", use_column_width=True)
                st.write("Segmenteção de Clientes Para Área de Marketing.")

            # Segundo lugar
            with col2:
                st.markdown("### Power BI")
                st.image("dash2.png", use_column_width=True)
                st.write("Prevendo a Produção Industrial ao Longo do Tempo.")

            # Terceiro lugar
            with col3:
                st.markdown("### Python")
                st.image("dash3.png", use_column_width=True)
                st.write("Visão Geral de Vendas.")

        elif selected == 'Apps':
            st.markdown("### 3 Aplicativos")
            col1, col2, col3 = st.columns(3)

            # Primeiro lugar
            with col1:
                st.markdown("### Python")
                st.image("appinvite.png", use_column_width=True)
                st.write("Um aplicavo para agendar reuniões com vários pessoas em horários diferentes.")

            # Segundo lugar
            with col2:
                st.markdown("### Power App")
                st.image("powerapp.png", use_column_width=True)
                st.write("Um aplicativo para emprestivo de acessórios da empresa.")

            # Terceiro lugar
            with col3:
                st.markdown("### Python")
                st.image("appregistro.png", use_column_width=True)
                st.write("Aplicativo para gerenciar e registrar as vendas.")

        elif selected == 'Automações':
            st.markdown("### 3 Automações")
            col1, col2, col3 = st.columns(3)

            # Primeiro lugar
            with col1:
                st.markdown("### Power Automate")
                st.image("powerautomate.png", use_column_width=True)
                st.write("Fluxo de Aprovação.")

            # Segundo lugar
            with col2:
                st.markdown("### Python")
                st.image("auto (1).jpeg", use_column_width=True)
                st.write("Automatizador de Tarefas Manuais.")

            # Terceiro lugar
            with col3:
                st.markdown("### Python")
                st.image("auto (2).jpeg", use_column_width=True)
                st.write("Robot Integrado no Ahatsapp como Assistente Virtual.")

        elif selected == 'Meus Vídeos':
            st.markdown("### Meus Vídeos")
            col1, col2, col3 = st.columns(3)

            # Primeiro vídeo
            with col1:
                st.markdown("### Vídeo 1")
                st.video("https://youtu.be/NjbR0fz4UQs?si=AjDiXutG5A_nqyTZ")
                st.write("Curso Completo de como criar interface gráficas no Python.")

            # Segundo vídeo
            with col2:
                st.markdown("### Vídeo 2")
                st.video("https://youtu.be/5mWU5Mq2zSA?si=wsHGMFx_JnOu-HlX")
                st.write("Aprenda como criar uma tela de Login no Python.")

            # Terceiro vídeo
            with col3:
                st.markdown("### Vídeo 3")
                st.video("https://youtu.be/Se96OW5Gwmw?si=Z7trN8tV9OyD7UAg")
                st.write("Aprenda como gerar QR code no Python.")

st.write('---')

# Seção Contato
with st.container():
    st.markdown('<a id="contato"></a>', unsafe_allow_html=True)
    st.markdown(conteiner_with_icon('chat-left-text-fill', 'Contato'), unsafe_allow_html=True)
    st.write("""
    <div class="contact-info">
        <p><i class="bi bi-envelope"></i> Email: makaya.afs@gmail.com</p>
        <p><i class="bi bi-telephone"></i> Telefone: +55 11 97743-0688</p>
        <p><i class="bi bi-linkedin"></i> LinkedIn: <a href="https://www.linkedin.com/in/makaya-afonso-41897425a" target="_blank">Makaya Afonso</a></p>
    </div>
""", unsafe_allow_html=True)
