piJukebox
=========

A jukebox script written in python for controlling a specific playlist in spotify.  Intended to be run on a raspberry pi but anything should/could work.

Created By:

[Shawn Grimes](www.shawngrimes.me) - Director of Technology at [Digital Harbor Foundation](www.digitalharbor.org)

Uses:
* http://www.mopidy.com/


# Installation
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo rpi-update
4. sudo reboot
5. Follow directions from: https://docs.mopidy.com/en/v1.0.0/installation/raspberrypi/
	1. sudo modprobe ipv6
	2. echo ipv6 | sudo tee -a /etc/modules
	3. sudo amixer cset numid=3 1
	4. Test Sound:    
aplay /usr/share/sounds/alsa/Front_Center.wav
	5. echo amixer cset numid=3 1  | sudo tee -a /etc/rc.local
	6. wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -
	7. echo \# Mopidy APT archive | sudo tee -a /etc/apt/sources.list
	8. echo deb http:\/\/apt.mopidy.com\/ stable main contrib non-free | sudo tee -a /etc/apt/sources.list
	9. echo deb-src http:\/\/apt.mopidy.com\/ stable main contrib non-free | sudo tee -a /etc/apt/sources.list
	10. sudo apt-get update
	11. sudo apt-get install mopidy
	12. sudo apt-get install mopidy-spotify
	13. sudo apt-get install python-pip
	14. sudo apt-get install python-mpd
	13. sudo pip install mpd
	13. sudo nano /etc/inittab
	14. Find the line that reads:  
1:2345:respawn:/sbin/getty —noclear 38400 tty1  
And add a # to the beginning of the line.
Then add a new line that reads:
1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1

	13. sudo dpkg-reconfigure mopidy
	14. nano ~/.config/mopidy/mopidy.conf
	15. Find the spotify section and add:
	16. enabled = true  
username = yourspotifyusername
password = yourspotifypassword

17. echo \/home\/pi\/piJukebox\/startUpScript.sh | tee -a ~/.profile


18. sudo nano /etc/kbd/config
19. Change these two lines.

# screen blanking timeout. monitor remains on, but the screen is cleared to
# range: 0-60 min (0==never) kernels I’ve looked at default to 10 minutes.
# (see linux/drivers/char/console.c)
BLANK_TIME=0 (Was 30)

# Powerdown time. The console will go to DPMS Off mode POWERDOWN_TIME
# minutes _after_ blanking. (POWERDOWN_TIME + BLANK_TIME after the last input)
POWERDOWN_TIME=0 (I think it was 15)



