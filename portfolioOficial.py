import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import smtplib
from email.mime.text import MIMEText



# Configuração da página
st.set_page_config(layout="wide")

# Barra lateral
with st.sidebar:
    st.markdown('<h1 style="color: gray;">Meu Portfólio</h1>', unsafe_allow_html=True)
    st.markdown('<a href="#inicio" style="color: #BFC5D3; text-decoration: none;"><i class="bi bi-house"></i> Início</a>', unsafe_allow_html=True)
    st.markdown('<a href="#sobre" style="color: #BFC5D3; text-decoration: none;"><i class="bi bi-person"></i> Sobre</a>', unsafe_allow_html=True)
    st.markdown('<a href="#projetos" style="color: #BFC5D3; text-decoration: none;"><i class="bi bi-code-slash"></i> Projetos</a>', unsafe_allow_html=True)
    st.markdown('<a href="#contato" style="color: #BFC5D3; text-decoration: none;"><i class="bi bi-chat-left-text-fill"></i> Contato</a>', unsafe_allow_html=True)

# HTML para incluir Bootstrap Icons CSS
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Função auxiliar para criar títulos de abas com ícones
def conteiner_with_icon(icon, label):
    return f'<div class="tab-title"><i class="bi bi-{icon}"></i> {label}</div>'

# Seção Início
st.markdown("<hr style='border: 1px solid #FF4B4B;'>", unsafe_allow_html=True)

with st.container():
    st.markdown('<a id="inicio"></a>', unsafe_allow_html=True)
    col1_inicio, col2_inicio = st.columns(2)

    with col1_inicio:
        st.markdown(conteiner_with_icon('house', ' '), unsafe_allow_html=True)
        st.subheader("Olá! :wave:")
        st.markdown("<h1 style='color: #FF4B4B;'>Meu Site de Portfólio</h1>", unsafe_allow_html=True)
        st.subheader("Bem-vindo ao meu portfólio.")
        st.write("""
            \nSou Makaya Afonso, um profissional apaixonado por ciência de dados, automação, visualização de dados, gestão de negócios e acima de tudo resolver problemas.
            \nAqui você encontrará informações sobre minha formação, experiência profissional e projetos, se despertar interesses entre em contato comigo.
            \nTake Your Time:blush:!
        """)

    with col2_inicio:
        st.image("pc_image.gif", caption=" ", use_column_width=True)

st.markdown("<hr style='border: 1px solid #FF4B4B;'>", unsafe_allow_html=True)


# Seção Sobre
with st.container():
    st.markdown('<a id="sobre"></a>', unsafe_allow_html=True)
    st.markdown(conteiner_with_icon('person', 'Sobre'), unsafe_allow_html=True)
    
    col1_sobre, col2_sobre, col3_sobre = st.columns(3, gap="large")

    with col1_sobre:
      
        st.markdown("<h3 style='color: #FF4B4B;'>Formação Acadêmica</h3>", unsafe_allow_html=True)
        with st.expander('Show/Hide', expanded=True):
            st.subheader('Bacharelado', divider='gray')
            st.markdown("""
                - __Universidade Cruzeiro do Sul__
                    - __Curso__: Ciência da Computação
                    - __Grade__: 4°Semestre
                    - __Previsão de Término:__: 2026
                """)




    with col2_sobre:
        st.markdown("<h3 style='color: #FF4B4B;'>Experiência Profissional</h3>", unsafe_allow_html=True)
        with st.expander('Show/Hide', expanded=True):
            st.subheader('Estágio', divider='gray')
            st.markdown("""
                - __Empresa__: American Tower
                    - __Duração__: (05/2023-Emprego atual)
                    - __Área__: Business Partner
                - __Detalhes__
                    - Gestão de Negócio.
                    - Tratamento de Dados com Oracle Analytics, ODV e Excel.
                    - Elaboração de Relatórios com Power BI.
                    - Automação de Processos com Python.
                """)

    with col3_sobre:
        st.markdown("<h3 style='color: #FF4B4B;'>Habilidades</h3>", unsafe_allow_html=True)
        with st.expander('Show/Hide', expanded=True):
            st.subheader('Programação e Ferramentas', divider='gray')
            st.markdown("""
                - __Python__
                    - __Numérico__: NumPy, Statsmodels, SciPy 
                    - __Dados__: Pandas,requests, SQLAlchemy, FastAPI
                    - __Machine Learning__: PyTorch, Scikit-Learn,Hyperopt, TensorFlow
                    - __Computação distribuída__: PySpark
                    - __Visualizations__: Streamlit, Matplotlib, Seaborn, Jupyter
                - __SQL__: MySQL, SQLite, Oracle
                __Power BI__
                __Oracle Data Visualization__
                - __Other__:
                    - __Metodologias Ágeis__: Scrum 
                    - __Soft Skill__: Trabalho em equipe, proatividade, aprendizado contínuo, comunicação eficaz.
                """)
            
        # Gráfico de Barras
    skills = ['Python', 'Power BI', 'SQL', 'Machine Learning', 'Oracle Data Visualization', 'Power Automate', 'Power App']
    skill_levels = [95, 85, 80, 75, 70, 90, 90]        
    with st.expander('Show/Hide', expanded=True):
        st.subheader('Minhas Habilidades em %', divider='gray')
        fig = go.Figure(data=[go.Bar(x=skills, y=skill_levels, marker_color='royalblue')])
        fig.update_layout(title_text='', xaxis_title='Habilidade', yaxis_title='Nível')
        st.plotly_chart(fig)

st.markdown("<hr style='border: 1px solid #FF4B4B;'>", unsafe_allow_html=True)


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

st.markdown("<hr style='border: 1px solid #FF4B4B;'>", unsafe_allow_html=True)

# Função para enviar email
def send_email(nome, email, mensagem):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'makaya.afs@gmail.com'
        password = 'pbtp nihn rjun ebaa'  # Use senha de aplicativo se a verificação em duas etapas estiver ativada

        msg = MIMEText(f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}')
        msg['Subject'] = 'Formulário de Contato'
        msg['From'] = sender_email
        msg['To'] = sender_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, sender_email, msg.as_string())

        return "Mensagem enviada com sucesso!"

    except Exception as e:
        return f"Erro ao enviar mensagem: {e}"

# Seção Contato
with st.container():
    st.markdown('<a id="contato"></a>', unsafe_allow_html=True)
    st.markdown(conteiner_with_icon('chat-left-text-fill', 'Contato'), unsafe_allow_html=True)
    
    col1_contato, col2_contato = st.columns(2, gap="large")

    with col1_contato:
        st.markdown("<h3 style='color: #FF4B4B;'>Envie uma Mensagem</h3>", unsafe_allow_html=True)
        nome = st.text_input("Seu Nome:")
        email = st.text_input("Seu Email:")
        mensagem = st.text_area("Mensagem:")
        
        if st.button("Enviar"):
            resultado = send_email(nome, email, mensagem)
            st.success(resultado)

    # Coluna 2: Informações de Contato
    with col2_contato:
        st.markdown("<h3 style='color: #FF4B4B;'>Informações de Contato</h3>", unsafe_allow_html=True)
        st.write("""
        <div class="contact-info">
            <p><i class="bi bi-envelope"></i> Email: makaya.afs@gmail.com</p>
            <p><i class="bi bi-telephone"></i> Telefone: +55 11 97743-0688</p>
            <p><i class="bi bi-linkedin"></i> LinkedIn: <a href="https://www.linkedin.com/in/makaya-afonso-41897425a" target="_blank">Makaya Afonso</a></p>
            <p><i class="bi bi-tiktok"></i> TikTok: <a href="https://www.tiktok.com/@makayaafonso" target="_blank">Makaya Afonso</a></p>
        </div>
        """, unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #FF4B4B;'>", unsafe_allow_html=True)
