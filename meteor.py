#!/usr/bin/env python
#run python 3 for this script (python 2 takes raw input and %r)


name = input("Hi, please enter your name ")
loc = input("What zipcode are you currently located in ")

print (" {} , your current location is {}".format(name, loc))

events = {'January':'Quadrantids', 'April    ':'Lyrids', 'May    ':'Eta Aquarids', 'August    ':'Perseids', 'October':'Orionids', 'November':'Leonids', 'December':'Geminids'}


#print (events['January'])
#print (events.keys())
#------------------------
#for kv in events.items():
	#print (kv[0],'\t',kv[1])

print ("Here is a list of the upcoming meteor showers this year!")

for key, value in events.items():
	print (key,'\t',value)