#!/bin/sh
################################################################################
#                                                                              #
#                     Script [GetNewIp] MLMConseil                             #
#                    ----------------------------------                        #
#                      permet dactualiser l'adresse IP                        #
#                    et l'envoyée vers une adresse Email                       #
#                    ----------------------------------                        #
#                  Ce fichier permet d'installer le Script                         #
#                  ---------------------------------------                     #
#                       langage : Python 2.7                                   #
#                       date creation : 30/09/2015                             #
#                       date modification : /08/2015                           #
#                       version : 0.1                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################
echo "------------------------Debut d'installation--------------------------- "
cp -R getnewip/ /usr/src/
chmod -R 777 /usr/src/getnewip/
cp getnewip.sh /etc/init.d/
cd /etc/init.d/
chmod 755 getnewip.sh
update-rc.d getnewip.sh defaults
/etc/init.d/getnewip.sh start
echo "------------------------Fin d'installation-----------------------------"
echo "Usage: /etc/init.d/getnewip {start|stop}"
exit 1
