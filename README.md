<p align="center">
  <img src="https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/toolbox-512.png" width=150/>
</p>

Esta é a minha caixa de ferramentas. Aqui eu tentei os meios mais pythonicos de resolver problemas em... Python, utilizando na maioria das vezes a biblioteca padrão.  
Voce é livre para:
* Executar o programa, para qualquer propósito;
* Estudar como o programa funciona e adaptá-lo às suas necessidades;
* Redistribuir cópias de modo que você possa ajudar ao seu próximo.
Só não se esqueça de dar crédito ao autor, eu! =p

## Bob Tools
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/datalivre)

* December/2019
    - [x] [COMPYRE](/python3/december/compyre/compyre.py) - script que abre dois arquivos de texto, transforma-os em listas, compara linha a linha a primeira lista com a segunda e retorna a diferença entre as duas.
    - Argumentos:
      - usage: compyre.py [-h] [-f1 FILE1] [-f2 FILE2]
      - optional arguments:
           * -h, --help  show this help message and exit
           * -f1 FILE1   first file name.
           * -f2 FILE2   second file name.
    - Como usar:
       * Você pode colocar os dois arquivos de texto ao lado do script **compyre** e então executá-lo com `python compyre.py`. Atenção ao nome do primeiro e segundo arquivo: **file1** e **file2**, respectivamente. Alternativamente, você pode usar a linha de comando:
       
         `python compyre.py -f1 file1 -f2 file2`
---
    - [x] [COMMANDER](/python3/december/commander/commander.py) - este script executa uma lista de comandos no host local. Pode ser usado para automatizar rotinas ou facilitar processo de instalação ou atulização de software.
    - Argumentos:
      - usage: Executa um ou mais comandos no host local. [-h] [-c CMD]
      - optional arguments:
           * -h, --help  show this help message and exit
           * -c CMD      insira um ou mais comandos separados por vírgula entre aspas.
    - Como usar:
       * Tente inserir alguns comandos no arquivo confile e em seguida digite o comando `python commander.py`. Alternativamente, você pode usar a linha de comando:
       
         `python commander.py -c "hostname, date, pwd"`
---