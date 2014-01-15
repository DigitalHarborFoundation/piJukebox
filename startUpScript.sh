#!/bin/sh
PIJUKEBOX_HOME=/home/pi/piJukebox

MOPIDY_CONFI=/home/pi/.config/mopidy/mopidy.conf

# start mopidy
/usr/local/bin/mopidy --config $MOPIDY_CONFI

#give mopidy 60 seconds to start up
sleep 60

# start the jukeboxUI
/usr/bin/python $PIJUKEBOX_HOME/piJukebox.py