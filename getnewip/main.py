#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp] MLMConseil     			       #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une adresse Email                       #
#                    ----------------------------------                        #
#                                                                              #
#                       langage : Python 2.7                                   #
#                       date creation : 26/09/2015                             #
#                       date modification : /08/2015                           #
#                       version : 0.1                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################
import sys, os, time
import myip
import mail
from threading import Thread
import logging
from logging.handlers import RotatingFileHandler

class GetNewIp(Thread):
	"""cette classe recupere l'adresse IP chaque tmp en seconde 
	et le comparre avec l'ancienne adresse IP, si l'adresse a changée 
	un message sera envoyé a l'dresse email avec cette nouvelle adresse
	la classe prends 4 parametres
	tmp : temps d'actualisation de l'adresse IP
	emetteur : adresse email de l'emetteur
	passw : mot de passe de l'adresse email de l'emetteur
	recepteur : adresse email du recepteur"""
	def __init__(self, emetteur, passw, recepteur, tmp):
		Thread.__init__(self)
		self.arret = False
		self.emetteur = emetteur
		self.mot_passe = passw
		self.recepteur = recepteur
		self.tmp = tmp
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
		file_handler = RotatingFileHandler('/var/log/getnewip.log', 'a', 1000000, 1)
		file_handler.setLevel(logging.DEBUG)
		file_handler.setFormatter(formatter)
		self.logger.addHandler(file_handler)
	def run(self):
		self.logger.info("démarrage du service")
		ip_1 = '0.0.0.0'
		ip_2 = '0.0.0.0'
		try:
			ip_2 = str(myip.myip())
		except:
			self.logger.warning('pas de connexion... tentative de reconnexion dans  1 minute')
			time.sleep(60)
			#ip_2 = '0.0.0.0'
		while not self.arret:
			if ip_1 == ip_2:
				self.logger.info("le processus s'arrete pour %d seconde"%self.tmp)
				time.sleep(self.tmp)
			else:
				self.logger.info( "le processus vas envoyer un email \n")
				#print " ip :  %s"%ip_2
				m = mail.mail(self.emetteur, self.mot_passe, self.recepteur, ip_2)
				m.EnvoyerMail()
				info = "Emetteur : "+str(self.emetteur) + " | recepteur : "+ str(self.recepteur) + " | IP : "+str(ip_2)
				self.logger.warning("un message a été envoyé --> %s "%info)
				ip_1 = ip_2
			try:
				ip_2 = str(myip.myip()) # entourer par try catch en cas de deconnexion , retourne un message pas de conexion
			except:
				#ip_2 = '0.0.0.0'
				self.logger.warning("pas de connexion... tentative apres 1 minute")
				time.sleep(60)
			#print " ip :  %s"%ip_2
	def stop(self):
		self.logger.info("arret du service")
		time.sleep(1)
		self.arret = True

def main():
	g = GetNewIp('ybouslahi@mlmconseil.fr','Algerie2015','yacine.bouslahi@gmail.com',120)
	if sys.argv[1] == 'start':
		g.start()
	elif sys.argv[1] ==  'stop':
		g.stop()
	else:
		print " \n main4.py : Usage :  /etc/init.d/getnewip {start|stop} \n"
	#pause = 300
	#time.sleep(pause)
	#g.stop()

	#print "Exit apres %d seconde de mise en marche" %pause

if __name__ == '__main__':
    main()
