#!/bin/sh
PIJUKEBOX_HOME=/home/pi/piJukebox

#MOPIDY_CONF=/home/pi/.config/mopidy/mopidy.conf

# start mopidy
#/usr/local/bin/mopidy --quiet --config $MOPIDY_CONF &

#give mopidy 60 seconds to start up
sleep 60

# start the jukeboxUI
/usr/bin/python $PIJUKEBOX_HOME/piJukebox.py
