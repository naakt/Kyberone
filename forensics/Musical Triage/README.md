# Musical Triage (Part 1. Wake Me Up)
## Challenge
Hint: https://www.youtube.com/watch?v=IcrbM1l_BoI (Wake Me Up)

## Solution:
Download the VM and boot it up. The flag will be right above the login prompt
FLAG: when_im_wiser_and_im_older_83

# Musical Triage (Part 2. Enter Sandman)
## Challenge
Hint: https://www.youtube.com/watch?v=CD-E-LDc384 (Enter Sandman)

## Solution:
Hint: https://kb.parallels.com/123324

1. Go to virtual machine's Configuration > Hardware > Boot Order.
2. Tick Select boot device on startup
3. Run Ubuntu
4. Once the virtual machine start to boot, make sure that the virtual machine is active (click inside virtual machine window) and press Shift key repeatedly until you see the grub menu. 
5. From the boot menu, select "Advanced options for Ubuntu", and then recovery mode
6. After you select recovery mode and wait for all the boot-up processes to finish, you'll be presented with a few options. Navigate to the Drop to root shell prompt using the arrow keys and press Enter.
7. To find the username: `ls /home`
8. To reset the password: `passwd craig`
9. Type `exit`
10. Select "Resume normal boot mode"
11. Login with the new credentials for craig
12. The flag will be in the welcome message.

FLAG: sleep_with_one_eye_open_32

# Musical Triage (Part 3. Through the Fire and Flames)
## Challenge
Hint: https://www.youtube.com/watch?v=0jgrCKhxE1s (Through the Fire and Flames)

## Solution:
Check the firewall rules using iptables
`sudo iptables -S`

FLAG: part3{for_now_we_fly_ever_free_48}

# Musical Triage (Part 4. Sweet Stairway To California?)
## Challenge
https://www.youtube.com/watch?v=1w7OgIMMRc4 (Sweet Child of Mine)
https://www.youtube.com/watch?v=xbhCPt6PZIU (Stairway to Heaven)
https://www.youtube.com/watch?v=09839DpTctU (Hotel California)

## Solution
Log into the VM via SSH

FLAG: cool_wind_in_my_hair_57

# Musical Triage (Part 5. We Will Rock You)
## Challenge
https://www.youtube.com/watch?v=-tJYN-eG1zk (We Will Rock You)

Note: The flag for this challenge is not in the same flag format as the other challenges in this series. It is a series of one or more words without spaces (ex. babyshark)

## Solution
`sudo apt install john -y`
`wget https://github.com/brannondorsey/naive-hashcat/releases/download/rockyou.txt`
`sudo john --wordlist=rockyou.txt /etc/shadow`

FLAG: truelove


# Musical Triage (Part 6. We Didn't Start the Fire)
## Challenge
https://www.youtube.com/watch?v=eFTLKWw542g (We Didn't Start the Fire)

## Solution
Check bash history using the command `history`. The flag is on the first line

FLAG: since_the_worlds_been_turning_74

## Setup
To clear bash history: `history -c && history -w`


# Musical Triage (Part 7. Hidden Treasure)
## Challenge
https://www.youtube.com/watch?v=PUntEk2wuLo (Hidden Treasure)

## Solution
1. The flag is in a hidden file
2. To find it, use `ls a` in the home directory

FLAG: message_in_the_deep_19


# Musical Triage (Part 8. Earth Song)
## Challenge
https://www.youtube.com/watch?v=XAi3VTSdTxU (Earth Song)

## Solution
Check the environmental variables using `env`

FLAG: what_about_the_sunrise_03

# Musical Triage (Part 9. Listen to the Music)
## Challenge
https://www.youtube.com/watch?v=DkytJLoxGmQ (Listen to the Music)

## Solution
1. Looks for open ports using a command like `sudo lsof -i -P -n`
2. The user "hacker" has port 3000 listening
3. connect to the port using `nc localhost 3000` and press enter
4. The flag is returned

FLAG: gotta_let_the_music_play_38

## Setup
/etc/music
```
#!/bin/bash

while true; do
    coproc nc -l localhost 3000
    while read -r cmd; do
    case $cmd in
        d) date ;;
        q) break ;;
        *) echo 'part9{so_climb_aboard_38}'
    esac
    done <&"${COPROC[0]}" >&"${COPROC[1]}"
    kill "$COPROC_PID"
done
```
`crontab -e`
`@reboot sh /etc/music`

# Musical Triage (Part 10. The Imperial March)
## Challenge
https://www.youtube.com/watch?v=4ODD7m3n3Yo (The Imperial March)

## Solution
1. There are imperial files on the VM.
2. In the Intelligence folder, there is a file (Kyber_One_Solutions_Reconnaissance_Logs) that contains a key (echo-niner-delta)
3. The key unlocks a zip file ("Prototype_Blueprints.zip") that is in the Documents folder
4. `sudo apt install unzip` to install the tool unzip
5. `unzip -P echo-niner-delta Prototype_Blueprints.zip` to unzip the file with the key
6. `sudo apt install poppler-utils` to install the tool pdftotext
7. `pdftotext Prototype_Blueprints.pdf` to convert the PDF to a txt file
8. `cat Prototype_Blueprints.txt` to display the flag

FLAG: a_long_time_ago_in_a_glaxy_far_far_away_93

# Setup Notes
## Compacting VM
https://www.howtogeek.com/312883/how-to-shrink-a-virtualbox-virtual-machine-and-free-up-disk-space/
```
systemctl stop systemd-journal* \
&& sudo swapoff -a && mount -n -o remount,ro -t ext2 /dev/sda1 / \
&& zerofree -v /dev/sda1
```
