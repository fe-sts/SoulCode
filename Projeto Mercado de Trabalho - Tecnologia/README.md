## Equipe
- [Daiane Silva de Abreu Benedito](https://www.linkedin.com/in/daiane-silva-de-abreu-benedito-01b41b13a/)
- [Felipe Rinaldini Santos](https://www.linkedin.com/in/felipe-rinaldini-santos/)
- [José Teles](https://www.linkedin.com/in/jose-henrique-teles/)
- [Talita Dwyer](https://www.linkedin.com/in/talitadwyer/)

## Apresentação
[Link para Apresentação completa do Projeto](https://github.com/fe-sts/SoulCode/blob/main/Projeto%20Mercado%20de%20Trabalho%20-%20Tecnologia/Apresenta%C3%A7%C3%A3o_Slides_Canva_Projetos_Final_Mercado_de_Trabalho.pdf)

## Tabela de conteudo
1. [Problemática inicial](#prob)
2. [Pesquisas: Datasets escolhidos](#datasets)
3. [Armazenamento: GCP Storage](#gcp)
4. [Armazenamento: MongoDB](#mongo)
5. [Armazenamento: MySQL](#mysql)
6. [Leitura, Limpeza e Transformação: Pandas , PySpark, SparkSQL](#etl)
7. [Big Query](#big)
8. [Síntese de Indicadores Sociais](#sintese)
9. [Resultados e Conclusões: DataStudio](#datastudio)

<div id='prob'/>

## Problemática inicial

### **Tema**: Mercado de Trabalho

 ### Qual o perfil dos profissionais que atuam profissionalmente ou não, em tecnologia da informação, no Brasil e no mundo?
- Escolaridade, empregabilidade, gênero, etnia, acessibilidade.
- Principais áreas de atuação de programadores e ferramentas mais utilizadas.

### Qual a relação entre os cursos de graduação em tecnologia disponíveis no Brasil, e sua demanda?
 - Cursos relacionados a tecnologia da informação são os mais procurados?
 - Qual a demanda de cada região brasileira por estes cursos?
----
<div id='datasets'/>

## Pesquisas: Datasets escolhidos
 - [Stack Overflow](https://insights.stackoverflow.com/survey/)
	- Área de Atuação
	- Situação Empregatícia
	- País
	- Escolaridade
	- Ferramentas de Trabalho mais Utilizadas
 - [Dados Abertos - SiSU](https://dados.gov.br/dataset/ensino-superior-sisu-sistema-de-selecao-unificada)
	- Nome e Estado da Instituição de Ensino
	-   Nome do Curso
	-   1ª ou 2ª Opção
	-   Aprovação
	-   Situação da Matrícula
 - [Google Trends](https://trends.google.com.br/trends/?geo=BR)
	- Profissões: Cientista de Dados, Dev Full Stack, Dev Front End, Dev Back End
	- Bancos de Dados: Microsoft SQL Server, MongoDB, Postgre SQL, SQLite, MySQL
	- Plataformas em Nuvem: AWS, Google Cloud Platform, Microsoft Azure, Heroku
	
	
<div id='etl'/>

## Processos de ETL
- [Stack Overflow: análise e plotagens](https://github.com/fe-sts/SoulCode/blob/main/Projeto%20Mercado%20de%20Trabalho%20-%20Tecnologia/1PF_Pandas_analise_plotagem_stack_overflow_2021.ipynb)
- [Stack Overflow: pandas, mongodb](https://github.com/fe-sts/SoulCode/blob/main/Projeto%20Mercado%20de%20Trabalho%20-%20Tecnologia/PF_Pandas_Mongo_stack_overflow_2021.ipynb)
- [Stack Overflow: pyspark, sparksql](https://github.com/fe-sts/SoulCode/blob/main/Projeto%20Mercado%20de%20Trabalho%20-%20Tecnologia/PF_Pyspark_stack_overflow_2021.ipynb)
- [SiSU](https://github.com/fe-sts/SoulCode/blob/main/Projeto%20Mercado%20de%20Trabalho%20-%20Tecnologia/PF_sisu_final_pynb.ipynb)
<div id='gcp'/>

## Armazenamento: GCP Storage
<div id='mongo'/>

## Armazenamento: MongoDB
<div id='mysql'/>

## Armazenamento: MySQL
<div id='etl'/>

## Leitura, Limpeza e Transformação: Pandas , PySpark, SparkSQL
<div id='big'/>

## Big Query
<div id='sintese'/>

## Síntese de Indicadores Sociais
<div id='datastudio'/>

## Resultados e Conclusões: DataStudio
- [Apresentação de resultados no Google DataStudio](https://github.com/fe-sts/SoulCode/blob/main/Projeto%20Mercado%20de%20Trabalho%20-%20Tecnologia/Apresenta%C3%A7%C3%A3o_DataStudio_Projeto_Final_Mercado_de_TrabalhoT.pdf)

**Resultados:**
- De acordo com o perfil da pesquisa, Estados Unidos, Índia, Alemanha, Reino Unido tiveram os maiores números de respondentes. Demonstra a demanda e desenvolvimento de cada mercado.
- A proporção de graduados (geral) que atuam profissionalmente é de 80% e 94% desdes estavam empregados. Este cenário é semelhante no Brasil.
- Grande desproporção entre de homens e mulheres. Predominancia de auto declarados brancos.
- Tipos de desenvolvedor: Predominância de Fullstack, seguido por Cientista de Dados.
- Google Trends Brasil: Predominância por pesquisas por Cientista de Dados.
- Banco de Dados: Maior uitlização de MySQL, seguido por SQL Server e PostgreSQL.
- Google Trends Brasil: Predominância por pesquisas por MySQL.
- Serviços de Nuvem: Maior uitlização de AWS, seguido por Azure e Google Cloud Platform
- Google Trends Brasil: Predominância por pesquisas por AWS.

**SiSU**
- Maior número de inscritos (geral), região sudeste - MG, RJ e SP seguido por BA.
- Os cursos ligados diretamente a tecnologia da informação / desenvolvimentos de sistemas não figuram entre os mais procurados.
- Maior número de inscritos (tecnologia), SP, RN, MG e RJ.
- Os cursos mais buscados são:
	- Análise e Desenvolvimento de Sistemas
	- Ciência da Computação
	- Eng. da Computação

