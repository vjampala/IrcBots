# Borrowed heavily from http://wiki.shellium.org/w/Writing_an_IRC_bot_in_Python. Thanks!

import random
import socket

class Bot:
    def __init__(self, server, channel, nick):
        self.server = server
        self.channel = channel
        self.nick = nick
    
    def generate(self):
        return "hello!"

    def joinChannel(self):
        ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ircsock.connect((self.server, 6667)) 
        ircsock.send("USER "+ self.nick +" "+ self.nick +" "+ self.nick +" :Name\n")
        ircsock.send("NICK "+ self.nick +"\n") 

        ircsock.send("JOIN "+ self.channel +"\n")
        while 1:
            ircmsg = ircsock.recv(2048) # receive data from the server
            ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
            print(ircmsg) # Here we print what's coming from the server

            if ircmsg.find(".hello "+ self.nick) != -1:
                response = self.generate("<s>")
                print response
                ircsock.send("PRIVMSG "+ self.channel +" :"+ response +"\n")
