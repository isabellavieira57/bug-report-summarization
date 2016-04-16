# bugReportsSummarization

Para compilar é necessário ter instalado python 2.7 e as seguintes bibliotecas: igraph, numpy, sklearn, scipy, nltk.

Comando para executar o algoritmo:
  python main.py -c entradas/<nome-arquivo-entrada> <oraculo>
  
onde:
  <nome-arquivo-entrada> é o nome do arquivo de entrada. Todos os arquivos estão na pasta "entradas".
  <oraculo> é o oraculo com o id de cada comentario separado por vírgulas.
  
Obs:
  1) Para rodar todos os experimentos de uma só vez, basta executar:
      bash experimentos.sh
      Esse script já possui o oraculo de cada uma das entradas.
