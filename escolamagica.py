import streamlit as st

# Configurações iniciais da página
st.set_page_config(page_title="Escola Mágica", page_icon=":school:", layout="wide")

# Título da Homepage
st.title("Bem-vindo à Escola Mágica 🎓")

# Subtítulo e logo
col1, col2 = st.columns([1, 3])
with col1:
    st.image("logo_escola_magica.png", width=100) 
with col2:
    st.markdown("<h2 style='color: #2E86C1; text-align: center;'>Acelere sua carreira na área Tech com a Escola Mágica</h2>", unsafe_allow_html=True)

# Seção "Sobre"
st.markdown("## **Sobre a Escola Mágica**")
st.markdown("""
Transforme seu futuro com a **Escola Mágica**! Aprenda na prática e desenvolva as habilidades técnicas necessárias para trabalhar com tecnologia. Com chances de emprego estável, aqui você vai além do papel e caneta e pratica seus conhecimentos em um ambiente inovador.
""")

# Inserção de imagem representativa
st.image("img_representativa.png", caption="Transforme seu futuro com a Escola Mágica", use_column_width=True)  # Substitua com o caminho correto

# Seção "Processo Seletivo"
st.markdown("<h2 style='color: #D35400;'>Processo Seletivo</h2>", unsafe_allow_html=True)
st.write("""
1. **Inscrição**: Preencha o formulário e candidate-se.
2. **Teste Online**: Teste de língua portuguesa e conhecimentos técnicos.
3. **Prova Prática**: Para quem passar nos testes online.
4. **Avaliação de RH**: Última etapa antes da possível admissão.
""")

# Botão de Inscrição
if st.button("Inscreva-se Agora!"):
    st.success("Você será redirecionado para o formulário de inscrição.")  # Aqui você pode inserir um link de redirecionamento

# Seção "Depoimentos"
st.markdown("<h2 style='color: #28B463;'>Depoimentos</h2>", unsafe_allow_html=True)
st.info("""
"A Escola Mágica mudou meus princípios e reforçou meus valores. Sou muito grato por isso!" - João S.
""")
st.success("""
"Entrar para a Escola Mágica foi um objetivo alcançado. Sou grata pela oportunidade!" - Maria L.
""")

# Seção "Contato e Redes Sociais"
st.markdown("## **Contato e Redes Sociais**")
st.write("Associação Passos Mágicos")
st.write("[passosmagicos@passosmagicos.org.br](mailto:passosmagicos@passosmagicos.org.br)")
st.write("[Nos siga na rede social](#)")

# Footer
st.markdown("---")
st.markdown("Escola Mágica | CNPJ: 26.616.356/0001-48 | Rua Francisco Volante, 13, Jd. Brasil, Embu-Guaçu - SP | CEP: 06900-530")
