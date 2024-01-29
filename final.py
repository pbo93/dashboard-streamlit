import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="FIAP LUB")

#nesse container vão ter esses 4 objetos de texto no site
with st.container():
  st.title('Sobre :blue[nós] :loudspeaker::')
  st.image('https://hexxlub.com.br/wp-content/uploads/2021/10/hexxlub-empresa-5.png', caption='Sede FIAP LUB', width=200, use_column_width=True)
  st.write("A FIAP OIL Óleo Lubrificante  prioriza uma abordagem tecnológica e sustentável, buscando eficiência máxima e qualidade. A constante supervisão dos processos visa otimizar a produção, melhorar o produto e reduzir perdas. O Controle de Qualidade assegura eficácia nos recursos, padronização e minimização de riscos no ambiente de trabalho.")
  st.write("---")
  st.title("Processo :blue[Produtivo]")
  st.subheader("Fornecimento", divider='rainbow') 
  #st.markdown("*Streamlit* is **really** ***cool***.")
  st.write("Matéria prima advinda dos líderes mundiais")
  st.subheader("Produção",divider='rainbow')
  st.write("Aditivação específica e controle de viscosidade seguindo os padrões exigidos pela ANP")
  st.subheader("Laboratório", divider='rainbow')
  st.write("Laboratório próprio para análise de óleos lubrificantes")
  st.subheader("Armazenamento" , divider='rainbow')
  st.write("Laboratório próprio para análise de óleos lubrificantes")
  st.subheader("Atendimento", divider='rainbow') 
  st.write("Canais  de venda e SAC FIAP OIL")
  st.write("---")
  st.title('Estrutura :house_buildings::')
  st.write("A FIAP OIL conta com um parque industrial próprio de mais de 7000 m², com ampla área destinada à produção, armazenamento e administração. Modernizada recentemente para acompanhar as exigências dos órgãos reguladores, a FIAP OIL atrela seu comprometimento na melhoria constante para se adequar às exigências dos avanços tecnológicos e das necessidades dos clientes.")
  st.write("---")
  st.title("Linha de :blue[produtos]:  Óleo de motor para carros :oil_drum:")
  st.write("Mantenha o foco em seu destino, enquanto os produtos da FIAP OIL cuidam da performance, economia de combustível e longa vida útil do motor de seu veículo. A marca FIAP OIL apresenta um portfólio para seu veículo: Oleos para motor de carros: sintéticos, semissintéticos e minerais.")

#with st.container():
  #coloca uma linha divisória no site
  #st.write("---")
  #st.subheader("1 Desafio")
  #st.title("Desafio")
  #st.write("A FIAP OIL  solicitou a Consultoria KPNG que desenvolve uma dashboard interativa e com alguns insight para tomada de decisão do preço do frasco do óleo. Além disso, um modelo de Marching Learning para fazer o forecasting do preço do petróleo.")
  #st.subheader("2 Análise do setor de petróleo")
  #st.title("CARACTERÍSTICAS DO PETRÓLEO")
  #st.write("O petróleo bruto exibe variações em sua composição química e aparência, influenciadas pelas características geológicas da região de extração. Algumas fontes apresentam elevado teor de enxofre, enquanto outras destacam-se pela concentração significativa de metais. Em relação à sua fluidez, existem petróleos viscosos e outros mais leves, determinados pela quantidade de átomos de carbono em sua composição. Além disso, a coloração do petróleo abrange uma ampla gama, desde tons de amarelo claro, semelhantes à gasolina, até nuances de verde, marrom e preto.")
  #st.write("Existem várias maneiras de classificar uma amostra de petróleo, e isso depende dos critérios adotados. Destacam-se, entre eles, o grau de densidade API (ºAPI) conforme o American Petroleum Institute, o teor de enxofre e a proporção dos diversos componentes químicos presentes, como parafínicos, naftênicos e asfálticos. Petróleos mais leves geram uma maior proporção de produtos leves, como gasolina, GLP e naftas. Em contraste, petróleos mais pesados produzem volumes significativos de óleos combustíveis e asfaltos. No ponto intermediário da cadeia, encontram-se os derivados médios, como o óleo diesel e o querosene.")
  #st.write("Fonte: [FGV - Petróleo, qualidade físico-químicas, preços e mercado, 2021](https://repositorio.fgv.br/server/api/core/bitstreams/57495871-ed00-4f15-b3e1-7b5bf032bb74/content)")
  #st.title("Relação de qualidade e preço")
  #st.write("Diversos tipos de petróleo bruto são extraídos globalmente, e o valor de mercado está diretamente relacionado à qualidade, refletida principalmente pela densidade e teor de enxofre. O gráfico apresenta uma variedade de óleos brutos negociados internacionalmente. Os preços refletem não apenas oferta e demanda, mas também a qualidade intrínseca, sendo que óleos leves e com baixo teor de enxofre geralmente possuem valores mais altos, enquanto os mais pesados e contaminados tendem a ter preços mais baixos, devido à necessidade de maior esforço de refino.")
  #st.write("Fonte: [FGV - Petróleo, qualidade físico-químicas, preços e mercado, 2021](https://repositorio.fgv.br/server/api/core/bitstreams/57495871-ed00-4f15-b3e1-7b5bf032bb74/content)")
  #st.title("Tipos de petróleo bruto")
  #st.write("Três das principais influências nos mercados mundiais de petróleo bruto são o Brent, o West Texas Intermediate (WTI) e o Dubai Fateh.")
  #st.title("Petróleo tipo brent X wti")
  #st.write("O campo de Brent, situado no Mar do Norte, foi descoberto em 1971, começando a produzir em 1976, durante as crises globais do petróleo. Contribuiu significativamente para suprir a escassez energética e transformar o Reino Unido em exportador de petróleo. Tornou-se uma referência mundial na precificação do petróleo, derivando seu nome de uma tradição da Shell de batizar campos com nomes de aves. As iniciais Brent também representam as rochas jurássicas que compõem o campo.")
  #st.write("O campo de Brent, com mais de 40 anos de produção, está próximo do encerramento de suas atividades. Das quatro plataformas originais (Brent Alfa, Beta, Celta e Delta), apenas a plataforma Brent Celta permanece em operação, mas seu descomissionamento está planejado pela Shell nos próximos anos. Atualmente, o preço do petróleo Brent é referenciado por uma cesta de diferentes óleos do Mar do Norte, incluindo Forties, Ekofish, Oseberg, Troll, entre outros.")
  #st.subheader("3 Dados: tipo do petróleo x preço (últimos 23 anos) Power BI")
  #st.title("Fonte de dados")
  #st.write("Os dados que que serão analisados no primeiro momento, serão o preço do óleo Brent e WTI a partir de 2000 até 2023.")
  #st.write("As bases foram extraídas no formato cvs do site da IPEA (Instituto de Pesquisa Econômica Aplicada).")
  #st.write("Fonte: [IPEA Data, 2023](http://www.ipeadata.gov.br/Default.aspx)")
  
with st.container():
  #coloca uma linha divisória no site
  st.write("---")
  #st.subheader("Dados: Tipo do petróleo x preço (últimos 23 anos) Power BI")
  st.title("Visualização histórica do preço do petróleo bruto WTI e BRENT")
  st.write("Preço do óleo Brent e WTI a partir de 2000 até 2023.Fonte: IPEA Data, 2023")
  st.link_button("Acessar aqui", "https://app.powerbi.com/view?r=eyJrIjoiMGRhM2FkMDYtY2M0NS00ZjhhLTk3YWMtNWU0ZGI1NWIzYTUzIiwidCI6IjAxYzI0ZmI1LWQxMTYtNDhiNS04ZmQ2LTJmMzdlMzYxM2YxMiJ9")
  #st.write("Os dados que que serão analisados no primeiro momento, serão o preço do óleo Brent e WTI a partir de 2000 até 2023.")
  #st.write("As bases foram extraídas no formato cvs do site da IPEA (Instituto de Pesquisa Econômica Aplicada).")
  #st.write("Fonte: [IPEA Data, 2023](http://www.ipeadata.gov.br/Default.aspx)")
  #st.title("Dashboard Power BI")
  #st.write("Link para o dashboard criado [clique aqui](https://app.powerbi.com/view?r=eyJrIjoiMGRhM2FkMDYtY2M0NS00ZjhhLTk3YWMtNWU0ZGI1NWIzYTUzIiwidCI6IjAxYzI0ZmI1LWQxMTYtNDhiNS04ZmQ2LTJmMzdlMzYxM2YxMiJ9)")
  st.write("---")

  st.title('Calculadora de preço :blue[petróleo]:')
#funçao para carregar os dados
#ele armazena no navegador as informações que estamos usando
@st.cache_data
def carregar_dados():
  #aqui precisa exportar o df_out2 versão final para um arquivo CSV para termos a base tratada e poder plotar os gráficos no streamlit
  tabela = pd.read_csv("df_out2.csv")
  return tabela

with st.container():
  dados = carregar_dados()
  #para plotar o gráfico de linhas
  st.line_chart(dados, x="Data", y="preco_petroleo_WTI")

with st.conteiner():
  st.write("---")
  st.subheader("4 Situações que ocasionaram a variação do preço do petróleo")
  st.title("1º 2008")
  st.write("Tensões geopolíticas no Irã, na Nigéria e no Paquistão; de um complexo equilíbrio entre uma oferta em declínio e uma demanda em alta, devido aos países emergentes e à China; e de uma forte especulação em torno de todas as commodities. Valor $134,00 barril (aproximado)")
  st.write("Fonte: [G1, 2008](https://g1.globo.com/Noticias/Economia_Negocios/0,,MUL940136-9356,00-O+ANO+EM+QUE+O+PETROLEO+ENLOUQUECEU+O+MERCADO.html)")
  st.title("2º 2012")
  st.write("Sanções econômicas impostas ao Irã, suspeito de usar seu programa nuclear civil para desenvolver armas nucleares. Em represália, o Irã ameaça interromper suas entregas de petróleo para a Europa, levantando preocupações sobre a oferta mundial de petróleo bruto. Valor $125,00 barril")
  st.write("Fonte: [Uol, 2022](https://economia.uol.com.br/noticias/afp/2022/02/24/datas-em-que-o-preco-do-petroleo-passou-de-us-100.htm)")
  st.title("3º 2018")
  st.write("Redução da Venezuela na produção de petróleo e sanção americana ao Irã (redução do fornecimento de barris de petróleo) Valor $70,00 barril (aproximado)")
  st.write("Fonte: [Uol, 2018](https://economia.uol.com.br/noticias/estadao-conteudo/2018/05/22/alta-do-petroleo-esta-ligada-a-questoes-geopoliticas.htm)")
  st.title("4º 2022")
  st.write("Guerra da Ucrânia, União Européia (UE)  corta cerca de 90%  de sua importação de petróleo russo e a compra de  fornecedores de petróleo mais distantantes pela UE aumentou o custo do frete; são alguns fatores que fizeram o petróleo bruto encarecer Valor $80,00 brarril (aproximado)")
  st.write("Fonte: [CNN, 2022](https://www.cnnbrasil.com.br/economia/3-razoes-pelas-quais-o-preco-do-petroleo-deve-seguir-alto-segundo-especialistas/)")

with st.conteiner():
  st.write("---")
  st.subheader("5 Modelos de Machine Learning")
  st.title("Teste 01")
  st.write("Método: Rede Neurais Recorrentes [clique aqui para acessar o notebook](https://colab.research.google.com/drive/1L0wGHaLSx-aghZPgAoJjSC_SOo8DNsd8?usp=sharing)")
  st.title("Teste 02")
  st.write("Método ARIMA [clique aqui para acessar o notebook](https://colab.research.google.com/drive/1E0LWv68qrmLoUM8Jtzj5QNSkvqW7ZqPh#scrollTo=dvgr-RlRWeIc)")

"""No terminal do pycharm ou outra IDE e executar -> streamlit run "nome do arquivo".py"""