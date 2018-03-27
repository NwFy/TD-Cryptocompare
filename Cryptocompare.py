import cryptocompare
def main ():
	while 1:
		entree = input ("Choisissez une action avec les commandes suivantes\ndevise : affiche toutes les devises \nprice : affiche la valeur des devises \nexit : pour quitter l'application\n:")
		if entree == "devise":
			for i in get_all_devise():
				print(i)
		elif entree == "price":
			print ('Entrez une cryptomonnaie (btc pour Bitcoin par ex) : ')
			get_price()
		elif entree == exit:
			print ('merci à bientôt')
			break
		else:
			print('Ceci n\'est pas une commande valide')

def get_all_devise():
	datas = cryptocompare.get_coin_list(format=True)
	table = []
	for data in datas:
		table.append(data)
	return table

def get_price():
	choice = input().upper()
	if choice in get_all_devise():
		print (cryptocompare.get_price(choice))

main()