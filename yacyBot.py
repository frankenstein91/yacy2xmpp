#!/usr/bin/env python2
from jabberbot import JabberBot, botcmd
import datetime, json
#der Patch https://raw.githubusercontent.com/freebsd/freebsd-ports/master/net-im/py-xmpppy/files/patch-xmpp-transports.py muss sein.

class YacyJabberBot(JabberBot):

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
        return str("todo")

