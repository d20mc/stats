# Import some necessary libraries.
import socket 
import urllib2
import sqlite3 as lite
import sys
# Some basic variables used to configure the bot
server = "irc.esper.net" # Server 199.9.252.26 irc.twitch.tv
channel = "#ducky" # Channel
botnick = "Statty" # Your bots nick
botpass = "" # Your bots password
con = lite.connect('stats.db') # location of database sqllite3
player1 = ""
player2 = ""

def ping(): # This is our first function! It will respond to server Pings.
	ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
	ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
	ircsock.send("JOIN "+ chan +"\n")


def exit(reason):
	print "Closing due to %s" % reason
	sys.exit()

#
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("PASS " + botpass + "\n") # here we send the server Password
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot
joinchan(channel) # Join the channel using the functions we previously defined
ircmsg = ircsock.recv(512)
ircmsg = ircmsg.strip('\n\r')
print ircmsg

if ircmsg.find("Login unsuccessful") != -1:
	exit("Login Failure")


while 1: # Be careful with these! it might send you to an infinite loop
	ircmsg = ircsock.recv(512) # receive data from the server
	ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
	print ircmsg
	if ircmsg.find(" left the game.") != -1:
		print "dude left"


	if ircmsg.find(" joined the game.") != -1:
		print "dude joined"

	if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
		ping()

	if ircmsg.find("     ") != -1: # if the server pings us then we've got to respond!
		break
		exit("Unknown Error")