import streamlit as st
import os

# Configuração de página em modo "wide"
st.set_page_config(page_title="Portfólio - Denis Mancini", page_icon="👨‍💻", layout="wide")

# ==========================================
# INJEÇÃO DE CSS (ESTILO MINIMALISTA + FONT AWESOME)
# ==========================================
estilo_css = """
<!-- Importação da biblioteca de ícones Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
/* Força a fonte monospace (estilo máquina de escrever) e fundo branco */
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Courier Prime', 'Courier New', Courier, monospace !important;
    background-color: #ffffff;
    color: #555555;
}

/* Oculta elementos padrão do Streamlit */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Container principal ajustado para centralizar o conteúdo */
.main .block-container {
    padding-top: 2rem;
    max-width: 1000px; 
    margin: 0 auto;
}

/* ========================================== */
/* ESTILOS DO NOVO MENU COM ÍCONES            */
/* ========================================== */
.nav-menu {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 35px; /* Espaço entre cada rede social */
    margin-bottom: 80px;
    margin-top: 10px;
}
.nav-link {
    display: flex;
    align-items: center;
    gap: 8px; /* Espaço entre o ícone e o texto */
    color: #888888; /* Cor cinza azulada do texto */
    text-decoration: none;
    font-size: 1rem;
    transition: all 0.3s ease;
}
.nav-link i {
    font-size: 1.6rem; /* Tamanho do ícone */
    color: #666666; /* Cor cinza mais escura para o ícone dar contraste */
    transition: all 0.3s ease;
}
.nav-link:hover, .nav-link:hover i {
    color: #000000; /* Fica preto ao passar o mouse */
}

/* ========================================== */
/* RESTANTE DOS ESTILOS                       */
/* ========================================== */
.hero-pre {
    text-align: center;
    font-size: 1.1rem;
    color: #888888;
    margin-bottom: 5px;
}
.hero-title {
    text-align: center;
    font-size: 4.5rem;
    font-weight: bold;
    color: #666666; 
    margin: -10px 0 20px 0;
    line-height: 1.1;
}
.hero-subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: #888888;
    line-height: 1.6;
}
.highlight {
    color: #ff6b6b;
}
.btn-email {
    display: block;
    width: 250px;
    margin: 40px auto 80px auto;
    background-color: #000000;
    color: #ffffff !important;
    text-align: center;
    padding: 15px 0;
    text-decoration: none;
    font-weight: bold;
    font-size: 0.95rem;
    transition: background-color 0.3s;
}
.btn-email:hover { background-color: #333333; }
.tab-container {
    margin-bottom: 30px;
}
.tab-active {
    background-color: #000000;
    color: #ffffff;
    padding: 12px 20px;
    display: inline-block;
    font-weight: bold;
    border-left: 3px solid #ff6b6b;
}
.tab-inactive {
    color: #888888;
    padding: 12px 20px;
    display: inline-block;
    font-weight: bold;
}
.about-text {
    font-size: 0.95rem;
    line-height: 1.8;
    color: #777777;
    margin-bottom: 20px;
    text-align: left;
}
[data-testid="stImage"] img {
    object-fit: cover;
    aspect-ratio: 1 / 1;
    border-radius: 2px;
}
</style>
"""
st.markdown(estilo_css, unsafe_allow_html=True)

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# ==========================================
# 1. MENU DE NAVEGAÇÃO (ATUALIZADO)
# ==========================================
# Inseri o YouTube para ficar idêntico ao seu print. Se não tiver um canal, basta apagar a linha dele.
st.markdown("""
<div class='nav-menu'>
    <a href='https://www.linkedin.com/in/denis-mancini/' target='_blank' class='nav-link'>
        <i class="fab fa-linkedin"></i> LinkedIn
    </a>
    <a href='#' target='_blank' class='nav-link'>
        <i class="fab fa-youtube"></i> YouTube
    </a>
    <a href='https://www.instagram.com/denismancini/' target='_blank' class='nav-link'>
        <i class="fab fa-instagram"></i> Instagram
    </a>
    <a href='https://github.com/denismancini' target='_blank' class='nav-link'>
        <i class="fab fa-github"></i> GitHub
    </a>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 2. HERO SECTION (CENTRALIZADO)
# ==========================================
st.markdown("""
<div class='hero-pre'>Oi, tudo bem? Eu sou o</div>
<div class='hero-title'>Denis Mancini</div>
<div class='hero-subtitle'>
    Eu sou um engenheiro de dados e desenvolvedor <br>
    focado em <span class='highlight'>modernização de plataformas</span> e tecnologia.
</div>
<a href='mailto:dmancini.07@gmail.com' class='btn-email'>Me envie um e-mail!</a>
""", unsafe_allow_html=True)

# ==========================================
# 3. SEÇÃO SOBRE (TEXTO + IMAGEM)
# ==========================================
st.markdown("""
<div class='tab-container'>
    <span class='tab-active'>| Resumo</span>
    <span class='tab-inactive'>Minhas Habilidades</span>
</div>
""", unsafe_allow_html=True)

col_texto, col_foto = st.columns([1.5, 1], gap="large")

with col_texto:
    st.markdown("""
    <p class='about-text'>Sou pós-graduado em Engenharia de Dados e em Inteligência Artificial, Machine Learning e Data Science, com formação em Análise e Desenvolvimento de Sistemas e Engenharia Civil.</p>
    
    <p class='about-text'>Com vasta experiência na área, dedico minha carreira ao desenvolvimento de pipelines de dados e aplicações de alto desempenho utilizando <span class='highlight'>Python, PySpark, SQL, Azure e Databricks</span>.</p>
    
    <p class='about-text'>Minha experiência abrange desde a arquitetura de sistemas escaláveis e desenvolvimento de processos ETL/ELT até a implementação de boas práticas de engenharia, sempre buscando entregar código limpo, performance e qualidade de dados alinhados com as melhores práticas do mercado.</p>
    
    <p class='about-text'>Tenho interesse contínuo em inovação inteligência artificial, aplicando conhecimentos em Machine Learning e Large Language Models (LLMs) para desenvolver soluções preparadas para aplicações inteligentes.</p>
    """, unsafe_allow_html=True)

with col_foto:
    arquivos_na_pasta = os.listdir(diretorio_atual)
    imagens_encontradas = [arquivo for arquivo in arquivos_na_pasta if arquivo.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if imagens_encontradas:
        nome_da_foto = imagens_encontradas[0]
        caminho_foto = os.path.join(diretorio_atual, nome_da_foto)
        st.image(caminho_foto, use_container_width=True)
    else:
        st.error("Imagem de perfil não encontrada na pasta.")