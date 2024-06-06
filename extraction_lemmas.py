from jjcli import *
from linguakit import *
from collections import Counter

cl = clfilter("")

lemmas_clean = ["<blank>", ".", ",", ":", ";", "...", "?", "!", "—", "-", '"', "(", ")"]

light_words_pt = ["ir" ,"ser", "estar", "ter", "haver", "tipo", "coisa", "que", "aí", "aqui", "alí"]

stop_words_pt = ["a", "ao", "aos", "aquela", "aquelas",	"aquele", "aqueles", "aquilo", "as", "até",	
"com", "como", "da", "das",	"de", "dela", "delas", "dele", "deles", "depois", "do",	"dos", "e", "ela",
"elas",	"ele", "eles", "em", "entre", "era", "eram", "essa", "essas", "esse", "esses",
"esta",	"estamos", "estas",	"estava", "estavam", "este", "esteja", "estejam", "estejamos",
"estes", "esteve", "estive", "estivemos", "estiver", "estivera", "estiveram", "estiverem",
"estivermos", "estivesse", "estivessem", "estivéramos",	"estivéssemos",	"estou", "está",
"estávamos", "estão", "eu",	"foi", "fomos",	"for", "fora",	"foram", "forem", "formos",	"fosse",
"fossem", "fui", "fôramos",	"fôssemos",	"haja",	"hajam", "hajamos",	"havemos", "hei",	
"houve", "houvemos", "houver", "houvera", "houveram", "houverei", "houverem", "houveremos",
"houveria",	"houveriam", "houvermos", "houverá", "houverão", "houveríamos",	"houvesse",
"houvessem", "houvéramos", "houvéssemos", "há", "hão", "isso", "isto", "já", "lhe",	"lhes",
"mais",	"mas", "me", "mesmo", "meu", "meus", "minha", "minhas", "muito", "na", "nas", "nem",
"no", "nos", "nossa", "nossas",	"nosso", "nossos", "num", "numa", "não", "nós",	"o", "os", "ou",
"para",	"pela",	"pelas", "pelo", "pelos", "por", "qual", "quando", "que", "quem", "se",	"seja",
"sejam", "sejamos",	"sem", "serei",	"seremos", "seria",	"seriam", "será", "serão", "seríamos",
"seu", "seus",	"somos", "sou",	"sua", "suas", "são", "só",	"também", "te",	"tem", "temos",
"tenha", "tenham", "tenhamos", "tenho",	"terei", "teremos",	"teria", "teriam", "terá", "terão",
"teríamos",	"teu", "teus", "teve", "tinha",	"tinham", "tive", "tivemos", "tiver", "tivera",
"tiveram", "tiverem", "tivermos", "tivesse", "tivessem", "tivéramos", "tivéssemos",	"tu",
"tua", "tuas", "tém", "tínhamos", "um", "uma", "você", "vocês", "vos", "à",	"às", "éramos"]


lemma_type = []


def ajuda():
	print("""Comandos:\n
help 
- imprime a lista de comandos

lemmas
- imprime a extração de todos os lemmas encontrados

lemmas_clean
- imprime a extração de todos os lemmas encontrados,
eliminando os lemmas derivados de pontuações, stop words e linhas em branco <blank>

names
- imprime a extração de todos os lemmas derivados de NOMES PRÓPRIOS

subs
- imprime a extração de todos os lemmas derivados de SUBSTANTIVOS

adj
- imprime a extração de todos os lemmas derivados de ADJETIVOS

verbs
- imprime a extração de todos os lemmas derivados de VERBOS

exit
- encerra o programa
""")
       
def lemmas():
	a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''').lower()
	if a == "s":
		b = input("Nome do arquivo: ")
		if b == "":
			b = "x"
		c = input ("Formato (txt/csv)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					f.write(f"{k}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					f.write(f"{k}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")

	elif a == "n":     
		for a in cl.input():
			if a != "":
				x, y, z = a.split()
				print(x)
	else:
		for a in cl.input():
			if a != "":
				x, y, z = a.split()
				print(x)

def lemmas_cll():
	a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''').lower()
	if a == "s":
		b = input("Nome do arquivo: ")
		if b == "":
			b = "x"
		c = input ("Formato (txt/csv)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")

	elif a == "n":     
		for y in cl.input():
			if y != "":
				k, l, m = y.split()
				if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
					print(k)
	else:
		for y in cl.input():
			if y != "":
				k, l, m = y.split()
				if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
					print(k)

def lemmas_cl():
	lemma_type = []
	z = input('''Digite "allocc" para a lista de todas lemmas (com as devidas limpezas) por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas dos x lemmas (com as devidas limpezas) mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							lemma_type.append(k)

				d = (Counter(lemma_type).most_common())
				for e in d:
					f.write(f"{e}\n")

				lemma_type = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							lemma_type.append(k)

				d = (Counter(lemma_type).most_common())
				for e in d:
					f.write(f"{e}\n")
					
				lemma_type = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							lemma_type.append(k)
						
			print(Counter(lemma_type).most_common())
			lemma_type = []
		else:
			for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							lemma_type.append(k)
						
			print(Counter(lemma_type).most_common())
			lemma_type = []

	elif z != "allocc":
		z = int(z)
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							lemma_type.append(k)

				d = (Counter(lemma_type).most_common())
				for e in d:
					f.write(f"{e}\n")
					
				lemma_type = []
				f.close()

			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							lemma_type.append(k)

				d = (Counter(lemma_type).most_common())
				for e in d:
					f.write(f"{e}\n")
					
				lemma_type = []
				f.close()

			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						lemma_type.append(k)
								
			print(Counter(lemma_type).most_common(z))
			lemma_type = []
		else:
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						lemma_type.append(k)
								
			print(Counter(lemma_type).most_common(z))
			lemma_type = []

def lemma_name():
	a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''').lower()
	if a == "s":
		b = input("Nome do arquivo: ")
		if b == "":
			b = "x"
		c = input ("Formato (txt/csv)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "NP00SP0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "NP00SP0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	
	elif a == "n":     
		for y in cl.input():
				if "NP00SP0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						print(k)
	else:
		for y in cl.input():
				if "NP00SP0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						print(k)

def lemma_subs():
	a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''').lower()
	if a == "s":
		b = input("Nome do arquivo: ")
		if b == "":
			b = "x"
		c = input ("Formato (txt/csv)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "NCMS000" in y or "NCMP000" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "NCMS000" in y or "NCMP000" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	
	elif a == "n":     
		for y in cl.input():
				if "NCMS000" in y or "NCMP000" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						print(k)
	else:
		for y in cl.input():
				if "NCMS000" in y or "NCMP000" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						print(k)

def lemma_adj():
	a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''').lower()
	if a == "s":
		b = input("Nome do arquivo: ")
		if b == "":
			b = "x"
		c = input ("Formato (txt/csv)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	
	elif a == "n":     
		for y in cl.input():
				if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						print(k)
	else:
		for y in cl.input():
				if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						print(k)

def lemma_verbs():
	a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''').lower()
	if a == "s":
		b = input("Nome do arquivo: ")
		if b == "":
			b = "x"
		c = input ("Formato (txt/csv)? ").lower()
		if c == "txt":
			f = open(b + ".txt", "w")
			for y in cl.input():
				if "VMIS3P0" in y or "VMIS3S0" in y: 
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		elif c == "csv":
			f = open(b + ".csv", "w")
			for y in cl.input():
				if "VMIS3P0" in y or "VMIS3S0" in y: 
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						f.write(f"{k}\n")
			f.close()
		else:
			print("ERRO: Formato Inválido.")
			print("Não foi possível gerar o resultado.")
	
	elif a == "n":     
		for y in cl.input():
				if "VMIS3P0" in y or "VMIS3S0" in y: 
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						print(k)
	else:
		for y in cl.input():
				if "VMIS3P0" in y or "VMIS3S0" in y: 
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						print(k)

def lemmas_main():    
	lemma_type = []
	z = input('''Digite "allocc" para a lista de todas as entidades por ordem de ocorrência. 
Digite (x) - um número inteiro - para a extração apenas das x entidades mais recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						lemma_type.append(k)

				d = (Counter(lemma_type).most_common())
				for e in d:
					f.write(f"{e}\n")
					
				lemma_type = []
				f.close()
					
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						lemma_type.append(k)

				d = (Counter(lemma_type).most_common())
				for e in d:
					f.write(f"{e}\n")
					
				lemma_type = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if y != "":
						k, l, m = y.split()
						lemma_type.append(k)
						
			print(Counter(lemma_type).most_common())
			lemma_type = []
		else:
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					lemma_type.append(k)
						
			print(Counter(lemma_type).most_common())
			lemma_type = []

	elif z != "allocc":
		z = int(z)
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						lemma_type.append(k)

				d = (Counter(lemma_type).most_common())
				for e in d:
					f.write(f"{e}\n")
					
				lemma_type = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if y != "":
						k, l, m = y.split()
						lemma_type.append(k)
			
				d = (Counter(lemma_type).most_common())
				for e in d:
					f.write(f"{e}\n")

				lemma_type = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if y != "":
					k, l, m = y.split()
					lemma_type.append(k)
							
			print(Counter(lemma_type).most_common(z))
			lemma_type = []
		else:
			for y in cl.input():
				if y != "":
					k, l, m = y.split() 
					lemma_type.append(k)
							
			print(Counter(lemma_type).most_common(z))
			lemma_type = []

def names_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todos os NOMES PRÓPRIOS (por ordem de ocorrência). 
Digite (x) - um número inteiro - para a extração apenas dos x NOMES PRÓPRIOS recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NP00SP0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NP00SP0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "NP00SP0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
				if "NP00SP0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		z = int(z)
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NP00SP0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common(z))
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NP00SP0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common(z))
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "NP00SP0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common(z))
			ent_list = []
		else:
			for y in cl.input():
				if "NP00SP0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common(z))
			ent_list = []

def subs_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todos os SUBSTANTIVOS (por ordem de ocorrência). 
Digite (x) - um número inteiro - para a extração apenas dos x SUBSTANTIVOS recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NCMS000" in y or "NCMP000" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NCMS000" in y or "NCMP000" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "NCMS000" in y or "NCMP000" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
				if "NCMS000" in y or "NCMP000" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		z = int(z)
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "NCMS000" in y or "NCMP000" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common(z))
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "NCMS000" in y or "NCMP000" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common(z))
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "NCMS000" in y or "NCMP000" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common(z))
			ent_list = []
		else:
			for y in cl.input():
				if "NCMS000" in y or "NCMP000" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common(z))
			ent_list = []

def adj_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todos os ADJETIVOS (por ordem de ocorrência). 
Digite (x) - um número inteiro - para a extração apenas dos x ADJETIVOS recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
				if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		z = int(z)
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common(z))
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common(z))
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common(z))
			ent_list = []
		else:
			for y in cl.input():
				if "AQ0MP0" in y or "AQ0MS0" in y or "AQ0FP0" in y or "AQ0FS0" in y or "AQ0CS0" in y or "AQ0CP0" in y or "AQ0CN0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common(z))
			ent_list = []

def verbs_main():    
	ent_list = []
	z = input('''Digite "allocc" para a lista de todos os VERBOS (por ordem de ocorrência). 
Digite (x) - um número inteiro - para a extração apenas dos x VERBOS recorrentes.\n''').lower()
	if z == "allocc":
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "VMIS3P0" in y or "VMIS3S0" in y: 
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "VMIS3P0" in y or "VMIS3S0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common())
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "VMIS3P0" in y or "VMIS3S0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common())
			ent_list = []
		else:
			for y in cl.input():
				if "VMIS3P0" in y or "VMIS3S0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common())
			ent_list = []

	elif z != "allocc":
		z = int(z)
		a = input('''Gostaria de guardar a extração em um arquivo? 
(s/n): ''')
		if a == "s":
			b = input("Nome do arquivo: ")
			if b == "":
				b = "x"
			c = input ("Formato (txt/csv)? ").lower()
			if c == "txt":
				f = open(b + ".txt", "w")
				for y in cl.input():
					if "VMIS3P0" in y or "VMIS3S0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common(z))
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			elif c == "csv":
				f = open(b + ".csv", "w")
				for y in cl.input():
					if "VMIS3P0" in y or "VMIS3S0" in y:
						k, l, m = y.split()
						if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
							ent_list.append(k)

				d = (Counter(ent_list).most_common(z))
				for e in d:
					f.write(f"{e}\n")

				ent_list = []
				f.close()
			else:
				print("ERRO: Formato Inválido.")
				print("Não foi possível gerar o resultado.")

		elif a == "n":
			for y in cl.input():
				if "VMIS3P0" in y or "VMIS3S0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common(z))
			ent_list = []
		else:
			for y in cl.input():
				if "VMIS3P0" in y or "VMIS3S0" in y:
					k, l, m = y.split()
					if l not in stop_words_pt and l not in lemmas_clean and l not in light_words_pt: 
						ent_list.append(k)
						
			print(Counter(ent_list).most_common(z))
			ent_list = []

while True:
	x = input('''Digite o comando desejado:
Digite "help" para ter acesso a lista de comandos.\n''').lower()
	if x == ("help"):
		ajuda()
		continue
	elif x == "lemmas":
		y = input(
'''Digite "alllemmas" para a extração de todos os lemmas.
Digite "lemmamain" para a extração de todos os lemmas (dado suas ocorrências).\n''').lower()
		if y == "alllemmas":
			lemmas()
			print("\n")
			continue
		elif y == "lemmamain":
			lemmas_main()
			print("\n")
			continue
	elif x == "lemmas_clean":
		y = input(
'''Digite "alllecl" para a extração de todos os lemmas com exceção dos lemmas derivados de pontuações, stop words e linhas em branco <blank>.\n
Digite "leclmain" para a extração de todos os lemmas com exceção dos lemmas derivados de pontuações, stop words e linhas em branco <blank> (dado suas ocorrências).\n''').lower()
		if y == "alllecl":
			lemmas_cll()
			print("\n")
			continue
		elif y == "leclmain":
			lemmas_cl()
			print("\n")
			continue
	elif x == "names":
		y = input(
'''Digite "allnames" para a extração de todos os lemmas derivados de NOMES PRÓPRIOS.
Digite "namemain" para a extração de todos os lemmas derivados de NOMES PRÓPRIOS (dado suas ocorrências).\n''').lower()
		if y == "allnames":
			lemma_name()
			print("\n")
			continue
		elif y == "namemain":
			names_main()
			print("\n")
			continue
	elif x == "subs":
		y = input(
'''Digite "allsubs" para a extração de todos os lemmas derivados de SUBSTANTIVOS.
Digite "submain" para a extração de todos os lemmas derivados de SUBSTANTIVOS (dado suas ocorrências)\n''').lower()
		if y == "allsubs":
			lemma_subs()
			print("\n")
			continue
		elif y == "submain":
			subs_main()
			print("\n")
			continue
	elif x == "adj":
		y = input(
'''Digite "alladj" para a extração de todos os lemmas derivados de ADJETIVOS.
Digite "adjmain" para a extração de todos os lemmas derivados de ADJETIVOS (dado suas ocorrências)\n''').lower()
		if y == "alladj":
			lemma_adj()
			print("\n")
			continue
		elif y == "adjmain":
			adj_main()
			print("\n")
			continue
	elif x == "verbs":
		y = input(
'''Digite "allverbs" para a extração de todos os lemmas derivados de VERBOS.
Digite "verbmain" para a extração de todos os lemmas derivados de VERBOS (dado suas ocorrências)\n''').lower()
		if y == "allverbs":
			lemma_verbs()
			print("\n")
			continue
		elif y == "verbmain":
			verbs_main()
			print("\n")
			continue
	elif x == "exit":
		break
	else:
		pass