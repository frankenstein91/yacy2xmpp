#!/usr/bin/env python2
from jabberbot import JabberBot, botcmd
import datetime, json
import logging
from urllib import urlopen
#der Patch https://raw.githubusercontent.com/freebsd/freebsd-ports/master/net-im/py-xmpppy/files/patch-xmpp-transports.py muss sein.

class YacyJabberBot(JabberBot):
    logging.basicConfig()

    MSG_AUTHORIZE_ME = "Bitte fuege mich deiner Kontaktliste hinzu und ich werde es auch tun."

    @botcmd
    def yacy(self,mess,args):
        """Gibt die URL zu Yacy aus"""
        user = self.get_sender_username(mess)
        text = "Hallo " + user + " hier ist dein Link zu Yacy\nGerman: http://yacy.de\tEnglish: http://yacy.de/en/"
        return text

    @botcmd
    def time(self, mess, args):
        """Zeigt die Serverzeit an"""
        return str(datetime.datetime.now())

    @botcmd
    def suchen(self,mess,args):
        """Bei Yacy suchen"""
        YacyServer = "http://search.yacy.de"
        url = urlopen(YacyServer + "/yacysearch.json?query=" + args).read()
        suche = json.loads(url)
        raus = "\n" + suche["channels"][0]["title"] + "\n\n"
        for item in suche["channels"][0]["items"][:10]:
            raus = raus + item["title"] + "\n" + item["link"] + "\n Size: " + item["sizename"]
            raus = raus + "\n Pup. Date: " + item["pubDate"] + "\n\n"
        f = open("debug2.txt", "w")
        f.write(raus.encode('utf-8'))
        return str(raus.encode('utf-8'))

