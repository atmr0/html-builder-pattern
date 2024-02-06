import re


# Métodos em comum das classes HTML e HTMLElement
class Base:
	def add_element(self, element_tag):
		new_element = HTMLElement(element_tag, self)
		self.content.append(new_element)
		return new_element

	def select(self, selector):
		for content in self.content:
			if isinstance(content,HTMLElement):
				if content.tag_name == selector:
					return content
		return None

	def selectAll(self, selector):
		return HTMLElementList(selector, self.content)
	def selectByClass(self, selector):
		return HTMLElementList(selector, self.content,"class")

	def selectById(self,id):
		for content in self.content:
				if isinstance(content,HTMLElement):
						if "id" in content.attributes and content.attributes["id"] == id:
								return content


class HTMLElement(Base):
	html = "" 
	content = []
	attributes = {}
	tag_name = ""
	parent = None
	ident = 0
	closing_tag = ""
	html = ""
	def __init__(self, tag, parent = None):
		self.content = []
		self.attributes = {}
		self.tag_name = tag
		self.parent = parent
		self.ident = parent.ident+1 #para a identação ficar correta no final
		self.closing_tag = "</" + self.tag_name + ">\n"
		self.html = "	"*self.ident+"<" + tag + "></" + tag + ">\n"
			


	def set_attribute(self, attribute_name, attribute_value):
		# o único atributo que penso em adicionar ao invés de substituir é style
		if attribute_name != "style" or "style" not in self.attributes: 
				self.attributes[attribute_name] = attribute_value
		else:
				self.attributes[attribute_name]+=";"+str(attribute_value)

		return self
	
	def set_attributes(self, attributes):
		for key, value in attributes.items():
			if key != "style":
				self.attributes[key] = value
			else:
				self.attributes[key]+=";"+value
		return self
	
	
	# Apaga tudo dentro do elemento e coloca o que foi passado
	def set_inner_html(self, inner_html):
		self.content = [inner_html]
		return self
	
	# Diferente do método anterior, só adiciona um texto
	def add_text(self, text):
		self.content.append(text)
		return self
	
	# Útil no method chaining, retornando ao elemento anterior
	def exit_element(self):
		return self.parent
	
	def build(self):
		new_attributes_string = ""
		#cria a tag de abertura com os atributos
		for key, value in self.attributes.items():
			new_attributes_string += (" "+key + "=\"" + value + "\"")
		self.html = "	"*self.ident+"<"+self.tag_name+new_attributes_string+">"
		self.html+= self.closing_tag
	
		if len(self.content) == 0: 
			return self.html
	
	
		new_html = ""
		for content in self.content:
			if isinstance(content,str):
				new_html+="	"*(self.ident+1) + content + "\n"
			else: 
				new_html+= content.build()
	
		new_html += "	"*self.ident+ self.closing_tag
		self.html = re.sub(self.closing_tag, "\n"+new_html,self.html,1)
		return self.html

class HTML(Base):
	content = []
	title = ""
	body = ""
	html = ""
	ident = 0

	def __init__(self, title="", body=""):
		self.title = title
		self.body = body
		# cria um template de página html
		self.html = "<!DOCTYPE html>\n"
		(self.add_element("head")
			.add_element("title")
				.add_text("Titulo" if title=="" else title)
				.exit_element()
			.exit_element()
			.add_element("body")
		 .set_inner_html(body))

	def save(self, filename):
		with open(filename, "w") as f:
			f.write(self.html)

	def load(self, filename):
		with open(filename, "r") as f:
			self.html = f.read()

	# Constrói o código
	def build(self):
		new_html = "<html>\n"
		for content in self.content:
			if isinstance(content,str):
				new_html+="	"*(self.ident+1) + content + "\n"
			else: 
				new_html+= content.build()
		self.html = new_html
		self.html+= "</html>\n"


# Usado apenas no método selectAll
class HTMLElementList:
	elements = []
	def __init__(self,selector,contents,criteria = "tag"):
		self.elements = []
		for content in contents:
			if isinstance(content,HTMLElement):
				if content.tag_name == selector and criteria == "tag":
						self.elements.append(content)
				elif "class" in content.attributes and	content.attributes["class"] == selector and criteria == "class":
						self.elements.append(content)

	def call(self,funcao,*args) :
		for element in self.elements:
			method = getattr(element,funcao)
			method(*args)
		return self