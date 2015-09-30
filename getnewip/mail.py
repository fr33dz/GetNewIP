#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp] MLMConseil                             #
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
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class   mail():
    """classe de configuration et de l envoi du message
        la classe prends 3 parametres 
        mail1 : l'email de l'emetteur 
        mail2 : l'mail de recepteur 
        ip : l'adresse ip à envoyer
    """
    def __init__(self, mail1, passw, mail2, ip):
        self.srvsmtp = 'smtp.mlmconseil.fr'
        self.port = 587
        self.mail1 = mail1
        self.passw = passw
        self.mail2 = mail2
        self.ip = ip


    def EnvoyerMail(self):
        """Envoyer un message on utilisant un serveur SMTP """
        
        msg = MIMEMultipart()
        msg['From'] = str(self.mail1)
        msg['To'] = str(self.mail2)
        msg['Subject'] = 'Nouvelle Adresse  ODOO'
        message = ' Ce message est envoyé par la société MLMConseil ..! \n \n'
        message += 'la nouvelle adresse de votre serveur ODOO est : \n \n \t http://'+str(self.ip)
        message += '\n \n si vous rencontrez des problemes lors de la connexion a votre serveur odoo \n \
        contactez nous a cette adresse \n \n \
        admin@mlmconseil.fr'
	message += "\n \n \n Date d'envoi : "+str(time.strftime("%d-%m-%Y-[%H-%M-%S]"))
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP(self.srvsmtp, self.port) #smtp.gmail.com
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(str(self.mail1), str(self.passw))
        mailserver.sendmail(str(self.mail1), str(self.mail2), msg.as_string())
        mailserver.quit()
       # print("le Message est bien envoyé ")


# def main():
#     m = mail('ybouslahi@mlmconseil.fr','Algerie2015', 'yacine.bouslahi@gmail.com','192.168.1.99')
#     m.EnvoyerMail()

# if __name__ == '__main__':
#     main()


