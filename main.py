from classes import *

html = HTML()
selection = html.select("body")
selection = selection.add_element("h1")
selection.set_inner_html("Trabalho final de POO")
selection = selection.exit_element()

selection = selection.add_element("h2")
selection.set_inner_html("Design Pattern: Builder")
selection = selection.exit_element()
html.save("00-SemConstruir.html")
html.build()

html.save("01-Apenas Titulo e Subtitulo.html")
print("---------------------APENAS TITULO E SUBTITULO---------------------")
print(html.html)
print("\n\n\n\n\n\n")
selection.add_element("h3").set_inner_html("Definição e demonstração")
selection.add_text("O design pattern builder foi desenvolvido para objetos complexos e difíceis de inicializar com apenas o construtor normal de uma classe.")
selection.add_text("<br>Imagine, por exemplo, criar uma tag HTML. Seria necessário especificar se há um id, se há uma classe, se há outros atributos - que mudam de acordo com a tag -, se há um estilo diferente etc.Um construtor ficaria algo semelhante a:")

selection = selection.add_element("p")
selection.set_attribute("class","errado")
selection.set_inner_html("element = HTMLElement(hasId = true,id = 'identificacao',hasClass = false,innerHtml='...',...)")
selection = selection.exit_element()
selection.add_text("Difícil, não? Assim foi criado o Builder, ao invés de construir em apenas uma linha, você cria métodos que constroem o elemento para você:")

selection = selection.add_element("p")
selection.set_attributes({"class":"certo","id":"inicioCerto"})
selection.set_inner_html("element = HTMLElement('p')<br>")
selection.add_text("element.set_attribute('class','certo')<br>")
selection.add_text("element.set_attribute('id','inicioCerto')<br>")
selection.add_text("element.set_inner_html('Metalinguagem')")
selection = selection.exit_element()


selection = selection.add_element("div").set_attribute("class","methodChaining")
selection.add_element("h3").set_inner_html("Method Chaining")
(selection.add_text("Com o Builder, tem como encadear métodos para acelerar o processo, contanto que o método retorne o próprio objeto")
 .add_text("<br>Por exemplo, ao invés do que vimos acima, podemos fazer:")
 .add_element("p").set_attribute("class","codigo")
 .add_text("element.set_attribute('class','certo').set_attribute('id','inicioCerto').set_inner_html('Metalinguagem')")
 .exit_element()
 .add_text("<br>ou<br>")
 .add_element("p").set_attribute("class","codigo")
 .add_text("element.set_attribute('class','certo')<br>.set_attribute('id','inicioCerto')<br>.set_inner_html('Metalinguagem')")
 .exit_element()
 .add_element("p")
 .add_text("Mas deve-se tomar cuidado com a quebra de linhas dependendo da linguagem.")
 .exit_element()
 .add_element("p")
 .add_text("Parece simples, mas pode economizar muito trabalho, como vocês poderão ver claramente nesta seção do código fonte em python deste projeto.")
)

(html.select("body").add_element("div")
 .add_element("h3").add_text("Inspiração do projeto").exit_element()
 .add_text("Este projeto foi criado apenas como um trabalho para a disciplina de Programação Orientada a Objetos, logo não há muita utilidade.<br><br>")
 .add_text("Este projeto foi inspirado pela biblioteca D3js, a qual não é recomendada para a criação de uma página HTML normal já que dá muito mais trabalho do que digitar normalmente")
 .add_text("A biblioteca foi projetada e amplamente usada para a apresentação de dados usando a tag svg. <br><br>Este projeto também não está bem desenvolvido para tal função.")
)


html.build()
print("---------------------APENAS OS TEXTOS---------------------")
print(html.html)
html.save("02 - Apenas os textos.html")
print("\n\n\n\n\n\n")

(html.select("head").add_element("style")
 .add_text(r"h3{background:#CCCCCC;}")
 .add_text(r".codigo{font-family:Consolas, 'Courier New', monospace}")
)
selection = html.select("body").set_attribute("style","font-family:sans-serif")
selection.select("h3").set_attribute("style","background:#DDDDDD")
# O selectAll retorna uma classe especial com uma lista de todos os HTMLElements com aquela tag 
#filho da tag atual.
# O método call recebe o nome da função a ser chamada em todos os HTMLElements e os parâmetros das funções
selection.selectAll("p").call("set_attribute","style","font-family:Consolas, 'Courier New', monospace")
selection.selectAll("div").call("set_attribute","style","border-style:solid;padding:10px;margin-bottom: 5px")

# O selectByCLass é semelhante ao All, mas seleciona pela classe
selection.selectByClass("errado").call("set_attribute","style","color:red")
# O selectByd retorna apenas um HTMLElement, já que as IDs são únicas
selection.selectById("inicioCerto").set_attribute("style","color:green")



html.build()
print("---------------------RESULTADO FINAL---------------------")
print(html.html)
html.save("03 - Trabalho final.html")
print("\n\n\n\n\n\033[1m\033[94mAgora vá na pasta para checar os resultados.\033[0m")