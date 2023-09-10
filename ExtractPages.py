from PyPDF2 import PdfReader, PdfWriter

class Extractpages():
    def __init__(self, dir, page):
        self.dir = dir
        self.page = page
        #Verifica se o parametro dir está formatado da maneira correta e se não estiver faz uma leve correção
        if '\\' in self.dir:
            self.dir = self.dir.replace('\\', '\\\\')
    #Metodo de extração de páginas
    def extr(self):
        rd = PdfReader(self.dir)
        wd = PdfWriter()
        #Percorre cada item dentro do parametro page e extrai as páginas correspondentes escrevendo no objeto wd
        for pg in self.page:
            pgextract = rd.pages[pg]
            wd.add_page(pgextract)
        #Salva o arquivo com as páginas extraidas
        wd.write('Extractpages.pdf')