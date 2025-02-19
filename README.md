# Web Scraping Campeonato Carioca 

Projeto criado para coletar dados dos campeonatos de futebol do Brasil de um time especifico, inicialmente fiz para coletar do campeonato carioca, mas serve para qualquer campoeonato que esteja no site da ESPN. 

Exemplo: Preciso coletar dados do time do Flamengo. 


Primeiro você vai precisar entrar no link abaixo e selecionar o time que deseja coletar os dados:
https://www.espn.com.br/futebol/times





Logo depois precisamos ir na aba de resultados conforme foto abaixo:


<img src="/img/1.png">



Depois vamos precisar selecionar o campeonato e a temporada desejada, estou fazendo com o campeonato carioca mas ele serve para todos os campeonatos listados nesses filtros: 


<img src="/img/3.png">

Depois de selecionar copie a url da pagina e guarde que vamos utilizar no codigo para extrar os dados dessa pagina. 


<img src="/img/4.png">



## Baixe o repositorio com o git clone 

```javascript
https://github.com/thiagoengdados/carioca-collect.git
```

## Abra a pasta do projeto no seu editor favorito. 

Conforme a imagem abaixo insira a url do time que escolhemos na variavel 'url'

<img src="/img/5.png">

<br>

Agora só executar o comando 

```javascript
python app.py
```
<br>

Aqui teremos o retorno dos dados:  

<img src="/img/6.png">

<br>

A partir de agora você tem o resultado campeonato e time desejado Placar e Data do jogo.
