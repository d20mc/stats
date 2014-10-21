# Import some necessary libraries.
import socket 
import urllib2
import sqlite3 as lite
import sys
import re

from time import sleep

# Some basic variables used to configure the bot
server = "irc.esper.net" #
channel = "#ducky" # Channel
botnick = "Statty" # Your bots nick
botpass = "" # Your bots password
con = lite.connect('stats.db') # location of database sqllite3

def ping(ircmsg): # This is our first function! It will respond to server Pings.
	print ircmsg
	stamp = re.search('(?<=:).+',ircmsg)
	print stamp.group(0)
	ircsock.send("PONG :"+stamp.group(0)+"\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
	ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
	ircsock.send("JOIN "+ chan +"\n")


def exit(reason):
	print "Closing due to %s" % reason
	sys.exit()
ping_cnt = 0
#
print "entering"
print "2"
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
print "connected"
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot
ircsock.send("USER "+ botnick +" 2 * :" + botnick + "\n") # here we actually assign the nick to the bot
while (ping_cnt < 2):
	print "while"
	ircmsg = ircsock.recv(1024)
	ircmsg = ircmsg.strip('\n\r')
	print ircmsg
	if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
		print "pinged"
		ping_cnt = ping_cnt + 1
		print ping_cnt
		ping(ircmsg)
		#sleep(9999)
	print "exiting"


joinchan(channel) # Join the channel using the functions we previously defined
print "join?"

while 1: # Be careful with these! it might send you to an infinite loop
	ircmsg = ircsock.recv(1024) # receive data from the server
	ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
	print ircmsg
	if ircmsg.find(" left the game.") != -1:
		print "dude left"
	if ircmsg.find(" joined the game.") != -1:
		print "dude joined"
	if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
		ping(ircmsg)
#
#	if ircmsg.find("     ") != -1: # if the server pings us then we've got to respond!
#		break
#		exit("Unknown Error")