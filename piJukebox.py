#!/usr/bin/python
# -*- coding: utf-8 -*-

playlistName="TC Jukebox"

import time
import curses
import curses.wrapper
from curses.textpad import Textbox, rectangle
from mpd import MPDClient
from threading import Timer
import locale
import logging
locale.setlocale(locale.LC_ALL, '')

logging.basicConfig(filename='debug.log',level=logging.DEBUG)

x='blank'

maxHeight=0
maxWidth=0

def drawScreen(stdscr):
	logging.debug("Drawing Screen\n")
	global maxHeight
	global maxWidth

	if x=='blank':
		stdscr.erase()
		client = MPDClient()               # create client object
		client.timeout = 10                # network timeout in seconds (floats allowed), default: None
		client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
		client.connect("localhost", 6600)  # connect to localhost:6600
		client.consume(1)

		songs=client.listplaylistinfo(playlistName) # print result of the command find playlist

		stdscr.addstr(0,35," _______   __    __   _______           __   __    __   __  ___  _______    .______     ______   ___   ___ ")
		stdscr.addstr(1,35,"|       \ |  |  |  | |   ____|         |  | |  |  |  | |  |/  / |   ____|   |   _  \   /  __  \  \  \ /  / ")
		stdscr.addstr(2,35,"|  .--.  ||  |__|  | |  |__            |  | |  |  |  | |  '  /  |  |__      |  |_)  | |  |  |  |  \  V  /  ")
		stdscr.addstr(3,35,"|  |  |  ||   __   | |   __|     .--.  |  | |  |  |  | |    <   |   __|     |   _  <  |  |  |  |   >   <   ")
		stdscr.addstr(4,35,"|  '--'  ||  |  |  | |  |        |  `--'  | |  `--'  | |  .  \  |  |____    |  |_)  | |  `--'  |  /  .  \  ")
		stdscr.addstr(5,35,"|_______/ |__|  |__| |__|         \______/   \______/  |__|\__\ |_______|   |______/   \______/  /__/ \__\ ")


		maxHeight, maxWidth =stdscr.getmaxyx()

		colCount=1
		rowCount=1
		yStart=6
		xStart=2
		maxRows= ((maxHeight-5)) - yStart
		maxStringLength=(maxWidth/2 - 13) / 2

		songStart=0

		for song in songs:
			songStart+=1

			artist= song['artist']
			artist= (artist[:maxStringLength] + '...') if len(artist) > maxStringLength else artist

			songTitle=song['title']
			songTitle=(songTitle[:maxStringLength] + '...') if len(songTitle) > maxStringLength else songTitle

			if(rowCount < maxRows):
				# stdscr.addstr(yStart+rowCount,xStart,str(rowCount) + " of " + str(maxRows))
				logging.debug(str(rowCount) + " of " + str(maxRows) + "\n")
				logging.debug(str(songStart).zfill(2) + ". " +  songTitle + " (" + artist + ")")
				stdscr.addstr(yStart+rowCount,xStart,str(songStart).zfill(2) + ". " +  songTitle + " (" + artist + ")" )

			#stdscr.addstr(yStart+rowCount,xStart,str(song))

			rowCount+=1
			if rowCount > maxRows :
				rowCount=1
				xStart=maxWidth/2

		status=client.status()
		if status['state']=="stop":
			client.play()

		client.close()                     # send the close command
		client.disconnect()



		stdscr.addstr(1,3, "Enter 2 Digit Song Number: ")

		rectangle(stdscr, 0,0, 5, 30)

		# editwin = curses.newwin(1,30, 2,1)

		curses.echo()            # Enable echoing of characters
		stdscr.refresh()

		drawSongs(stdscr)

def drawRick(stdscr):
	stdscr.erase()
	stdscr.addstr(0,0,"~~~~~~~~:~~~~~++I$O88DDDDD88DDDDD88OO88DD8D8ZZZ8Z$$$$?+==~==~~~~~~~==~~~~~~~~~==")
	stdscr.addstr(1,0,"~~~~~~~~~~~~~I$77$O8DDDDDDDD88DNDDD88D8D888OZ$ZOOZZZZI+==~~~~~~~~~~===~~~=~====~")
	stdscr.addstr(2,0,"~~~~~~~~~~~=7I$Z88888888D8D8DDDDDD88888OO8OZ$ZZZOZOZZI=~~~~~~~~~~~~====~~~~~==~~")
	stdscr.addstr(3,0,"~~~~~~~~~~~=ZZOZO8O88888D88DDDDDD888OZZ$$77I??I$ZOOZZZ+~~~~~:~::~::~~==~~~~==~~~")
	stdscr.addstr(4,0,"~~~~~~~~~~~Z77ZOOO88888888888888OZZ$7I????++++++IZZZZ$I~~::::::::::~~~~~=~~=~~~~")
	stdscr.addstr(5,0,"~~~~~~~~~~~+7$ZZOO88O8OZZZ$$$$$77$7I??????+++++++77Z$$7=~~~~:~~~~:~~~~~~~=====~~")
	stdscr.addstr(6,0,"~~~~~~~~~~~==ZOOO8OOOZ$$$$$77777III???II??+++++++?7$$$$+~::::::::::~~~~~~~~=~~~~")
	stdscr.addstr(7,0,"~~~~~~~~~~~~~?O888OZ$$$$$$$$777IIIIIIIII??++++++++I7$ZI?=~~~~~~~~~~~~~~~~~~~=~~~")
	stdscr.addstr(8,0,"~~~~~~~~~~~~=IZOOOOZ$$$$$$$$$77IIIIIIII????+++++++I7$77+==~~~~~~~~~~~=~~~~~~~~~~")
	stdscr.addstr(9,0,"~~~~~~~~~~~::IZOOOO$$$$$$$$$$$77IIIIIIII???+++++++?7$I?+~~~~~~~:~:~~==~~=~~~~~~~")
	stdscr.addstr(10,0,"::~:~~~~~~~~~I$8OOO$$$$$$$$$$$$7II?II7II??+++++++++I$I+~=~~~~~~~~~~====~=~~=~~:~")
	stdscr.addstr(11,0,"~:~~~::~~~::~~IOOOO$$$$$$$$$$$$777III77777$7$77I?==+7I+~~~~:~~~~~~====~~~~~~::::")
	stdscr.addstr(12,0,":::::::::~::::IZOOO$$$$$ZZOO8OOOOZ$7I7777$$7I?????++I7+==~~:~~========~~~~~~~:::")
	stdscr.addstr(13,0,"::::~:::::::::=ZOOO$$$ZZZ$$$$$$$ZOZ$I++?IZO8OZZ$?+++?7I?~~~~~~========~~~:::::::")
	stdscr.addstr(14,0,":::::::::,,,:::$OOO$$$$$$ZO888ZOZZZ$7?++I77I??++++++++=7=~~:~:~======~~~~~:~~:::")
	stdscr.addstr(15,0,":::::::::,:,:~:=ZOO$$$$ZZ$$$$$$$ZZZZ$??+++???I??+++++7=I~~~~~~~~~~====~~~~~~~~::")
	stdscr.addstr(16,0,":::::::::,:,::7$$OOZ$$$$$$$$$$Z$$$$$$I?++??????+++++=II+~~~~~~~=====~~~~~:~~~~::")
	stdscr.addstr(17,0,"~::~:::::,:,:,7I$$Z$$$$$$$$$$$$$$$$$$I?+??II??++++++=II==========~~~~~~~::::::::")
	stdscr.addstr(18,0,"~:~:::::::::::I7$Z$$$$$$$$$$$$$$ZZ$Z$I??++?$$I?++++++++~:~~~~~~~:~~~~~:~:::~~~::")
	stdscr.addstr(19,0,"~~::::::::::::~77$$$$$$$$$$$$$$$Z$$Z$7I?$I+I$$7??+++++~::::~::~::~~~~:::::::::::")
	stdscr.addstr(20,0,"~~~~:~~~~~~~::~~77Z$$$$$$$$$$$$$ZZOZZ$I?++++?$$7?+=++~::::~:~:~::~~~~~~::::~::::")
	stdscr.addstr(21,0,"~::~~~~~::::::~~=77$Z$$Z$$$ZZ$ZZZZ$$7III??+++?I$?++=~~~~~::~:::::~:~::::::::::::")
	stdscr.addstr(22,0,"~~~~~~~~~::::~~~~:7$Z$$$$$$ZZZZZ$$$$7IIIIII?7II7??+=~~::~::~:::,,:::::::::::::::")
	stdscr.addstr(23,0,"~~~~~~~::::::~~~~,,:?$$$$$$$ZZOOOOOO$7I?+?I?+?II?++~~::~~~:~::::::~~::::::::::::")
	stdscr.addstr(24,0,"~~~~~~~:::~::~~~~:::=7$$$$$$$$$$ZZ$OZ$ZZ7????????++~~~~:~::::::,,::~:::::::~~:::")
	stdscr.addstr(25,0,"~~~~~~:::::::~~~::::=7$$Z$$$$$$$$$Z$7III????????++~~~~~~:::::::::~~~::::::::::::")
	stdscr.addstr(26,0,"~~~~~~::,:,,~~~~~~~=7I$$ZZZZ$$$$$ZZZZ$$7I?????++++=~~~~~~:~:::,,:~~~~::::~::~:::")
	stdscr.addstr(27,0,"~~~~~:::::,,~~~~::?ZO7$ZZZZZZZ$$$$$$77II?????+?++=~~~~~~:~~::~:::~~~::::::::::::")
	stdscr.addstr(28,0,"~~~~:::,,:::~~~~~7ZOD7$$ZZZZZZZ$$$$77III????++++==~~~::~~:~::~::~~~~~~~~~~~:::::")
	stdscr.addstr(29,0,"~~~::::,:,:~~~~I$88DDZ$$ZZZZZZZZ$$$$7IIII??????+==~~~~~~~~~~:~::~~~~~~~~~~::~~::")
	stdscr.addstr(30,0,"~~~::::::::~~+$O8DDDDOZZZZZZOOZZZZZZZ7$7III???+===~~~~:~~~~~~~~~==~=~~~~~~~:::::")
	stdscr.addstr(31,0,"~~~::::::=I$ZO88DDDDDD$ZZZZZZOZOZZZ$$$$$7I??+?++==~~~~~~~~:~~~~~~===~~~~~~~:~:::")
	stdscr.addstr(32,0,"~~~~:~I7$ZO88DDDDDDDDD7$ZZZ$ZZZOOOOI8OZ77III==?+++~~~:~::::~~~~~===~~~~=~~~~~:::")
	stdscr.addstr(33,0,"=+?$$ZO8DDDDDDDDDDDDDDOI$ZZZ$Z$$$Z$7?ZZZ8$Z??87++~$ZZ7=~~~~~~~~~===~~~~~~~~~~~::")
	stdscr.addstr(34,0,"$$ZO8DDDDDDNDDDNDDDNDDD7IZZZ$$$777$I$O$OZZO$IOI?=~I$ZOOOZI=~===+=====~=~~~~~~~~:")
	stdscr.addstr(35,0,"O8DDDDDDDDDNDDDDDDNDDNNZ?=77$$77777$ZZ$8ZZZ$I7I++==ZZZOOOZOZZ7=======~~=~~~~~~~~")
	stdscr.addstr(36,0,"DNDDDDNDNDDNDDDDDDDDNND87++I7777III7ZZOZOZZ$?$?+==~$ZOOO8OOOOOZZ$?==~~~~~~~~=~~~")
	stdscr.addstr(37,0,"DDDDDDDDDDDDD88888DDDDDD$?++I77III?7$ZO$O$$$?7?+==~$ZOOOOOOOOZOZZZZ7=~~~~~~~~~~~")

	stdscr.addstr(40,0," _______      _          __        _______           __   __               __  ")
	stdscr.addstr(41,0,"|_   __ \    (_)        [  |  _   |_   __ \         [  | [  |             |  ] ")
	stdscr.addstr(42,0,"  | |__) |   __   .---.  | | / ]    | |__) |   .--.  | |  | | .---.   .--.| |  ")
	stdscr.addstr(43,0,"  |  __ /   [  | / /'`\] | '' <     |  __ /  / .'`\ \| |  | |/ /__\\/ /'`\' |  ")
	stdscr.addstr(44,0," _| |  \ \_  | | | \__.  | |`\ \   _| |  \ \_| \__. || |  | || \__.,| \__/  |  ")
	stdscr.addstr(45,0,"|____| |___|[___]'.___.'[__|  \_] |____| |___|'.__.'[___][___]'.__.' '.__.;__]")
	stdscr.refresh()

	time.sleep(3)
	stdscr.clear()
	drawScreen(stdscr)


def addSong(stdscr, selectedSongNumber):
	client = MPDClient()               # create client object
	client.timeout = 10                # network timeout in seconds (floats allowed), default: None
	client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
	client.connect("localhost", 6600)  # connect to localhost:6600
	songs=client.listplaylistinfo("TC Jukebox")
	client.consume(1)

	if selectedSongNumber==30:
		selectedSong=songs[selectedSongNumber]
		songid=client.addid(selectedSong['file'], 0)
		client.play(0)
		drawRick(stdscr)
	elif selectedSongNumber==98:
		client.clear()

	elif selectedSongNumber<100:
		selectedSong=songs[selectedSongNumber]
		#stdscr.addstr(50,5,str(selectedSong['file']))
		client.add(selectedSong['file'])
		drawScreen(stdscr)

	client.close()                     # send the close command
	client.disconnect()

def drawSongs(stdscr):
	logging.debug("Drawing Songs" + "\n")
	client = MPDClient()               # create client object
	client.timeout = 10                # network timeout in seconds (floats allowed), default: None
	client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
	client.connect("localhost", 6600)  # connect to localhost:6600
	client.consume(1)

	if x=='blank':
		blankLine="                                                                                                                                                                                     "

		# print("Max Height", maxHeight)
		# print("Max Width", maxWidth)

		stdscr.addstr(maxHeight-2,0,blankLine[:maxWidth-5])
		stdscr.addstr(maxHeight-3,0,blankLine[:maxWidth-5])

		songList=[]
		try:
			currentPlaylist=client.playlistinfo()
			for playlistSong in currentPlaylist:
				songList.append(playlistSong['title'])
			stdscr.addstr(maxHeight-2,5,"Up Next: " + str(songList))
		except:
			pass

		try:
			currentSong=client.currentsong()
			stdscr.addstr(maxHeight-3,5,"Now Playing: " + str(currentSong['title']) + " (" + str(currentSong['artist']) + ")", curses.A_BOLD)
		except:
			stdscr.addstr(maxHeight-3,5,"Now Playing: ", curses.A_BOLD)
			pass

		client.close()                     # send the close command
		client.disconnect()
		stdscr.refresh()


def main(stdscr):
	drawScreen(stdscr)

	stdscr.nodelay(True)

	t = Timer(7.0, drawSongs,args=[stdscr,])
	t.start()

	fullScreenTimer=Timer(60.0, drawScreen,args=[stdscr,])
	fullScreenTimer.start()

	x='blank'
	while x!='qq':
		try:
			if x!='blank':
				x=str(x) + str(stdscr.getkey(4,16))
				selectedSongNumber=int(x)-1

				if selectedSongNumber<100:
					addSong(stdscr,selectedSongNumber)
				x='blank'
			else:
				x=stdscr.getkey(4,15)

		except:
			if t.isAlive() == False:
				# logging.debug("Exception getting key\n")
				# logging.debug("t is alive: " + str(t.isAlive()) + "\n")
				t = Timer(7.0, drawSongs,args=[stdscr,])
				t.start() # after 5 seconds
			if fullScreenTimer.isAlive()==False:
				fullScreenTimer=Timer(60.0, drawScreen,args=[stdscr,])
				fullScreenTimer.start()
			pass


	time.sleep(5)


curses.wrapper(main)
