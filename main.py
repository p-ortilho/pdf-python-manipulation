import ExtractPages

#Váriaveis com nossos parametros
diretorio = r'C:\Users\pegasus\Livros\C++.pdf'
paginas = [1, 41, 20, 33, 12]

#Criação do objeto extração
objextracao = ExtractPages.Extractpages(diretorio, paginas)

#Extraido páginas
objextracao.extr()