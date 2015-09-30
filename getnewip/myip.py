#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp] MLMConseil             			       #
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
from urllib2 import urlopen

def myip():
	return urlopen('http://ip.42.pl/raw').read()
