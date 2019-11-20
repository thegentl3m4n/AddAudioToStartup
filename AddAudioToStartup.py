import os, sys, shutil, time


desktop_script = ('[Desktop Entry]', 'Name=StartupAudio', 'GenericName=startup audio', 'Comment=adds startup sound ', 'Exec=/root/.startupAudio/script.sh', 'Terminal=false', 'Type=Application', 'X-GNOME-Autostart-enabled=true')


#this code chechs if the input file is in .ogg format or not

if sys.argv[1].endswith('.ogg'):
    os.system('mkdir /root/.startupAudio/')                                      # it creates a hidden folder in root directory
    shutil.move(sys.argv[1], '/root/.startupAudio/audio.ogg')               #it renames any input .ogg filename into audio.ogg
    print('working on it.\n')
    time.sleep(1)
    print('working on it..\n')
    time.sleep(1)
    print('working on it...\n')
    time.sleep(1)

else:
    sys.exit(sys.stderr.write('Unsupported file format.\n File must be in .ogg format\n'))          #this line gives the error if input file is not in .ogg format


#this line creates an shell file which is suppose to be add on startup

os.system('echo "paplay /root/.startupAudio/audio.ogg" >> /root/.startupAudio/script.sh')
os.system('chmod +x script.sh')


#it will write the .desktop file in /root/.config/autostart directory

with open('/root/.config/autostart/AudioOnStartup.desktop' , 'w+') as file:
    for line in desktop_script:
        file.write(line + '\n')


os.system('systemctl restart cron.service')
print('congratulation your audio is set successfully!\n Your system will now reboot in 10 seconds.\n')
time.sleep(10)
os.system('reboot')

