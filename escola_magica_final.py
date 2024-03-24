import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# CSS para alterar a cor de fundo da página

fundo_laranja = """
<style>
    .stApp {
        background-color: #FFA500;
    }
</style>
"""

st.markdown(fundo_laranja, unsafe_allow_html=True) 

#imagem header
from PIL import Image
import streamlit as st

# Carregar a imagem

# Carregar a primeira imagem
path1 = 'Escola sem fundo.png'
image1 = Image.open(path1)
largura_desejada = 240
altura_desejada = 180
image_resized1 = image1.resize((largura_desejada, altura_desejada))

# Carregar a segunda imagem
path2 = 'Bolsa de estudo.png'
image2 = Image.open(path2)
largura_desejada = 200
altura_desejada = 180
image_resized2 = image2.resize((largura_desejada, altura_desejada))

# Exibir as imagens lado a lado
col1, col2 = st.columns(2)
with col1:
    st.image(image_resized1, use_column_width='always')
with col2:
    st.image(image_resized2, use_column_width='always')


#header
texto = "<span style='color: #FFFFFF;'>Venha para a </span><span style='color: #196ABD;'>Escola Mágica</span> <span style='color: #FFFFFF;'> e acelere sua carreira na área Tech!</span>"
styled_text = f"<h1 style='text-align: center;'>{texto}</h1>"
st.markdown(styled_text, unsafe_allow_html=True)

#Imagens tabela
col1, col2, col3, col4 = st.columns(4)

with col1:
      st.image("Chapeu.png")

with col2:
      st.image("Mãos.png")

with col3:
   st.image("Teclado.png")
   
with col4:
    st.image("Trofeu.png")


#tabela
html_table = """
  <tr>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>Transforme o seu futuro</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>Muito além do Tech</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>Aprenda na prática</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>Chance de emprego estável</b></td>
  </tr>
  <tr>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Aprimore seus conhecimentos e desenvolva as habilidades técnicas necessárias para trabalhar com mecânica e funilaria!</td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Saiba construir melhores relacionamentos profissionais!</td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Vá além do papel e caneta e pratique seus conhecimentos diretamente na Escola Mágica!</td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Quem tiver um alto desempenho durante o curso, poderá se tornar funcionário de um dos nossos parceiros</td>
  </tr>
</table>
"""
st.markdown(html_table, unsafe_allow_html=True)

st.write("")
st.write("")

texto = "Faça a sua inscrição"
styled_text = f"<h1 style='text-align: center; color: white;'>{texto}</h1>"
st.markdown(styled_text, unsafe_allow_html=True)

#Botão de inscrição

if st.button('Quero me inscrever', key='inscrever'):
   
    st.markdown('[Clique aqui para ir para a página de inscrição](https://docs.google.com/forms/d/e/1FAIpQLScioGTE9mB7G1zhm8OWrx-QUGVJAB_JDpHOnaGlGQy9aHBbGw/viewform)')

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 200px !important;
        height: 80px !important;
        color: white !important;
        background-color: #196ABD !important;
        margin: 0 auto !important;
        display: block !important;
        font-size: 50px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# Processo seletivo
texto = "Como funciona o processo seletivo"
styled_text = f"<h1 style='text-align: center; color: white;'>{texto}</h1>"
st.markdown(styled_text, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
      st.image("Ckeck.png")

with col2:
      st.image("Ckeck.png")

with col3:
   st.image("Ckeck.png")

html_table = """
  <tr>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 30px; color: white;"><b>Pelo menos 18 anos de idade</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 30px; color: white;"><b>Ensino médio completo</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 30px; color: white;"><b>Conhecimentos prévios em informática</b></td>
  </tr>
 
</table>
"""
st.markdown(html_table, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# Etapas
texto = "Quais são as etapas?"
styled_text = f"<h1 style='text-align: center; color: white;'>{texto}</h1>"
st.markdown(styled_text, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
      st.image("seta.png")

with col2:
      st.image("seta.png")

with col3:
   st.image("seta.png")
   
with col4:
    st.image("seta.png")

html_table = """
  <tr>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>1.Inscrição</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>2.Teste online</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>3.Prova prática</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>4. Avaliação RH</b></td>
  </tr>
  <tr>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Preencha o formulário e candidate-se ao processo seletivo</td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Faça o teste de língua portuguesa e o  teste teórico tech</td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Quem for aprovado na prova online, fará um teste prático</td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Por fim, o candidato será avaliado pelo RH. Se aprovado, fará parte da próxima turma da Escola Mágica!</td>
  </tr>
</table>
"""
st.markdown(html_table, unsafe_allow_html=True)

#Botão de inscrição

if st.button('Quero me candidatar', key='inscrever2'):
   
    st.markdown('[Clique aqui para ir para a página de inscrição](https://docs.google.com/forms/d/e/1FAIpQLScioGTE9mB7G1zhm8OWrx-QUGVJAB_JDpHOnaGlGQy9aHBbGw/viewform)')

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 400px !important;
        height: 80px !important;
        margin: 0 auto !important;
        display: block !important;
        font-size: 50px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# Quem somos?
texto = "Quem somos?"
styled_text = f"<h1 style='text-align: center; color: white;'>{texto}</h1>"
st.markdown(styled_text, unsafe_allow_html=True)

#Imagem
path = 'jovens.jpg'
image = Image.open(path)
largura_desejada = 50  # Defina a largura desejada em pixels
st.image(image, width=largura_desejada, use_column_width='always')

html_table = """
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">A Associação Passos Mágicos tem uma trajetória de 31 anos de atuação, trabalhando na transformação da vida de crianças e jovens baixa renda os levando a melhores oportunidades de vida.
A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.
Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.
nos de idade</td>
  </tr>
</table>
"""
st.markdown(html_table, unsafe_allow_html=True)

st.write("")
st.write("")


# Opiniões?
texto = "Veja a opinião dos nossos alunos?"
styled_text = f"<h1 style='text-align: center; color: white;'>{texto}</h1>"
st.markdown(styled_text, unsafe_allow_html=True)

html_table = """
  <tr>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>João Silva</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;">“A Escola Mágica mudou os meus princípios e reforçou ainda mais os meus valores como ser humano, e como colaborador. Com ela conseguir aprimorar e usar todo conhecimento dado. Sou muito grato por tais ensinamentos, e sou grato por estarem mudando vidas! Obrigado, Escola Mágica.”</td>
  </tr>
  <tr>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;"><b>Maria Oliveira</b></td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 22px; color: white;">“Entrar para a Escola Mágica foi um objetivo alcançado, pois eu tinha desejo de trabalhar na área, mas é um mercado mais difícil de ingressar por ser mulher. Mas a Passos Mágicos abriu as portas para mim. Sou grata pela oportunidade, pela ajuda e suporte dos meus professores, que são maravilhosos!”</td>
  </tr>
</table>
"""
st.markdown(html_table, unsafe_allow_html=True)

st.write("")
st.write("")


#Botão de inscrição

if st.button('Quero fazer parte', key='inscrever3'):
   
    st.markdown('[Clique aqui para ir para a página de inscrição](https://docs.google.com/forms/d/e/1FAIpQLScioGTE9mB7G1zhm8OWrx-QUGVJAB_JDpHOnaGlGQy9aHBbGw/viewform)')

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 400px !important;
        height: 80px !important;
        margin: 0 auto !important;
        display: block !important;
        font-size: 50px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Opiniões?
texto = "A escola mágica vai criar oportunidades para que você possa mergulhar em um mundo de inovação e criatividade, explorando os segredos da programação, da inteligência artificial e muito mais."
styled_text = f"<h1 style='text-align: center; color: white;'>{texto}</h1>"
st.markdown(styled_text, unsafe_allow_html=True)

st.write("")
st.write("")


#Botão de inscrição

if st.button('Quero fazer a inscrição', key='inscrever4'):
   
    st.markdown('[Clique aqui para ir para a página de inscrição](https://docs.google.com/forms/d/e/1FAIpQLScioGTE9mB7G1zhm8OWrx-QUGVJAB_JDpHOnaGlGQy9aHBbGw/viewform)')

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 400px !important;
        height: 80px !important;
        margin: 0 auto !important;
        display: block !important;
        font-size: 50px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Footer
texto = "Conheça nossos parceiros"
styled_text = f"<h1 style='text-align: center; color: white;'>{texto}</h1>"
st.markdown(styled_text, unsafe_allow_html=True)

#Imagens tabela
col1, col2, col3, col4 = st.columns(4)

with col1:
      st.image("Fiap.png")

with col2:
      st.image("ESPM.png")

with col3:
   st.image("Origem.png")
   
with col4:
    st.image("Mattos.png")
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
#tabela
html_table = """
  <tr>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">Associação Passos Mágivos
(11) 98208-3282
passosmagicos@passosmagicos.org.br</td>
    <td style="border: none; background-color: transparent; text-align: center; font-size: 18px; color: white;">CNPJ:26.616.356/0001-48
Rua Francisco Volante, 13
Jd.Brasil, Embu-Guaçu - SP | CEP:06.900-530</td>
  </tr>
</table>
"""
st.markdown(html_table, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
      st.image("Selo 1.png")

with col2:
      st.image("Selo 2.png")

with col3:
      st.image("Selo 3.png")
   
with col4:
      st.image("Selo 4.png")
