# yacy2xmpp

At first (of course) you need to create a Jabber account for your bot.

Then you make a file with the following contents. Of course, you have to enter username and password of the created account.
```
#!/usr/bin/env python2
from yacyBot import YacyJabberBot
bot = YacyJabberBot(username, password)
bot.serve_forever()
```
Give the file any name and save the file in the same directory as the yacyBot.py.

Now you can make your own Yacy Bot for you and others (and run it).
# nice to know
At the moment you still need to edit the yacyBot.py if you wish to use your own Yacy Server.

This bot also supports loklak.
