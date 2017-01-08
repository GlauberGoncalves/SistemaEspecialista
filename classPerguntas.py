from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['O seu parente é um homem?','homem'],
		#['O seu parente é mais velho(a) que você?','maisvelho'],
		['O seu parente é filho(a) do seu avô ou avó?','filhoavoa'],
		['O seu parente e você são filhos da mesma mãe?','filhomesmamae'],
		['O seu parente é filho(a) de sua tia ou tio?','filhotioa'],
		['O seu parente é filho de sua avó ou avô?','filhoavoa']]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
