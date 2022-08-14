<h2> Um leitor de imagens para a calculadora Numworks! </h2>

Este programa foca-se em converter imagens png/jpg/webp/etc, em imagens que a calculadora <a href="https://www.numworks.com">Numworks</a> consegue abrir. O programa está atualmente na sua 3 versão, com as seguintes funcionalidades:
- Suporte de até 64 cores (limitando caso a imagem tenha mais que 64 cores);
- Suporte completo de imagens SD (Standard Definition), apresentando imagens de até 160x111px;
- Suporte parcial de imagens HD (High Definition), apresentando imagens de até 320x222px (a resolução total da calculadora), desde que a imagem não utilize mais de 60-70% da área total do ecrã, ou que tenha cores sólidas.
- Suporte de imagens LD (Low Definition), caso a imagem não precise de alta resolução, poupando em até 40% comparando ao SD;
- Suporte de imagens com resolução abaixo de LD, apesar de não recomendado, pois a imagem torna-se muito pouco legível;
- Suporte de quase todos tipos de ficheiros de imagem, desde png e jpg, a webp, jfif, etc.

<img src="https://www.numworks.com/pt/funcionalidades/functions-9cac5f63.jpg">

<h2> Como Usar? </h2>

A utilização do programa é focado em ser user-friendly, então não deixes que o CMD te intimide. Para utilizar o programa, segue estes passos:
- Baixar a build "Numworks Image Loader.exe", ou executar um dos scripts (pastas V2 e V3 recomendadas, visto que a V1 é muito menos otimizada);
- Caso uses a V2, escolhe entre o conversor HD e SD. 
- Copiar e colar o <a href="https://pt.wikipedia.org/wiki/Diretório_(computação)"> diretório </a> da imagem;
- Colocar o nome que será dado ao script;
- Caso uses a V3, escolhe a qualidade da imagem (quanto menor o número, melhor a qualidade);
- Abrir o site da Numworks, selecionar "My Scripts" ao colocar o cursor em cima do nome, no canto superior direito;
- Adicionar um novo script e copiar e colar o código para o mesmo;
- Clicar em "Load to Calculator" e seguir os passos.

<img src= "https://cdn.numworks.com/372bf724.svg">

<h2> Como Funciona?</h2>

Para os curiosos que gostariam de saber como o programa funciona sem ter que procurar pelo código, aqui está uma breve explicação. O programa irá transformar a imagem em texto, usando base64, e após isso, vai substituir as letras que são iguais por números, para fins de otimização (a V1 não tem esta otimização, por isso sendo não recomendada). Por fim, a calculadora lê esse texto e apresenta os pixeis de acordo com a informação dada no texto.


<h2> Informação Importante </h2>

Além de ser um programador relativamente novo, entrarei no ensino secundário, então não sei quanto tempo terei para atualizar e manter este programa. Apesar disso, irei trazer novos programas, como paint, jogos, etc, para a calculadora. Obrigado por leres! :)
