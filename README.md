# AddAudioToStartup
its a python script that'll add the given audio file to startup


# working
it basically creates a 'startupscript.desktop' in '/root/.config/autostart/' directory.
which is executed on startup (every .desktop file in that directory start at startup)


# requirement
your given file must be in *.ogg format (you can use https://www.onlineconverter.com/mp3-to-ogg)


# usage
python AddAudioToStartup.py <audioFile.ogg>
