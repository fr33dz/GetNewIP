#!/bin/bash
#/etc/init.d/getnewip
################################################################################
#                                                                              #
#                     Script [GetNewIp] MLMConseil                             #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une adresse Email                       #
#                    ----------------------------------                        #
#           Ce fichier permet d'ajouter le script /usr/src/getnewip/main.py    #
#                               comme service                                  #
#                 -----------------------------------------                    #
#                       langage : Python 2.7                                   #
#                       date creation : 30/09/2015                             #
#                       date modification : /08/2015                           #
#                       version : 0.1                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################
#
RUN=0
case "$1" in
  start)
    echo "Starting script GetNewIP "
    RUN=1
    python /usr/src/getnewip/main.py start &
    ;;
  stop)
    echo "Stopping script GetNewIP"
    RUN=0
    python /usr/src/getnewip/main.py stop &
    ;;
  status)
    if [ $RUN -eq 0 ]
    then
    	return 0
    	exit 1
    else
	    return 1
	    exit 1
    fi
    ;;
  *)
    echo "Usage: /etc/init.d/getnewip {start|stop}"
    exit 1
    ;;
esac

exit 0
