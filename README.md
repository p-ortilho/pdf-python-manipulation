# pdf-python-manipulation

Olá 👋,

Esse script tem como funcionalidade extrair páginas de um arquivo pdf, fique a vontade para melhorá-lo, quando criei foi para resolver um problema de extração de páginas de um arquivo que queria, então não me importei muito de fazer da forma mais eficiente.

Por mais que o código seja simples, vou fazer a explicação de maneira breve.

Utilizei a biblioteca PyPDF2 para fazer a manipulação dos arquivos usando os métodos de leitura *PdfReader()* e escrita *PdfWriter()*.

A classe recebe dois parâmetros que são uma string que pode conter o caminho para o arquivo ou somente o nome do arquivo vai depender da onde você está executando o código e uma lista onde contem as paginas que serão extraídas.
Usei uma estrutura de condição *if* para verificar se a entrada do parâmetro *dir* estava formatada da maneira correta e caso não esteja faço uma pequena correção(formatação para Windows).

~~~
from PyPDF2 import PdfReader, PdfWriter

class Extractpages():
    def __init__(self, dir, page):
        self.dir = dir
        self.page = page
        if '\\' in self.dir:
            self.dir = self.dir.replace('\\', '\\\\')
~~~
No método criando para a extração das páginas utilizamos dois objetos, um para fazer a leitura de nosso arquivo,  que recebe o parâmetro *dir* e outro para fazer a escrita. Dentro do loop *for* percorremos cada item da nossa lista e adicionamos cada página extraída ao objeto *wd*. Posteriormente salvamos o novo arquivo com as páginas extraídas usando o método *write()*.
~~~
    def extr(self):
        rd = PdfReader(self.dir)
        wd = PdfWriter()
        for pg in self.page:
            pgextract = rd.pages[pg]
            wd.add_page(pgextract)
        wd.write('Extractpages.pdf')
~~~

O arquivo main.py é um exemplo de como usar o script, fique a vontade para pedir correções.