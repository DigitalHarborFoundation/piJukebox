#!/bin/sh
PIJUKEBOX_HOME=/home/pi/piJukebox

# start mopidy
/usr/local/bin/mopidy --config $PIJUKEBOX_HOME/.config/mopidy/mopidy.conf

#give mopidy 60 seconds to start up
sleep 60

# start the jukeboxUI
/usr/bin/python $PIJUKEBOX_HOME/piJukebox/piJukebox.py