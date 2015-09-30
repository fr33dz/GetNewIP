################################################################################
#                                                                              #
#                     Script [GetNewIp] MLMConseil                             #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une adresse Email                       #
#                    ----------------------------------                        #
#          				                                       #
#                 -----------------------------------------                    #
#                       langage : Python 2.7                                   #
#                       date creation : 30/09/2015                             #
#                       date modification : /08/2015                           #
#                       version : 0.1                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################

Utilisation 

1.Configuration :

	dans le repertoire getnewip , editer le ficher main.py 
	modifier la ligne 83
	g = GetNewIp('adresse-emetteur@mlmconseil.fr','mot-de-passe','adresse-	destination@gmail.com','pause_en_seconde')

exemple de configuration:
	g = GetNewIp('ybouslahi@mlmconseil.fr','bouslahi','client_1@gmail.com',120)

------------------------

2.Installation

su 
chmod 755 install.sh
./install.sh
