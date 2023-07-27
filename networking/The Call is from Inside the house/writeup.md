# Description
A laptop was recently turned back in to the unit. It was configured to capture local pcap while it was checked out to ensure there are no security violations. The administrator suspects the user was disgruntled and may have used the laptop for malicious activity. What actions has the user done?

Flag Format: XXX.XXX.XXX.XXX:ZZZZZ

# Solution

1 TASK NUMBER: CPB-COM-2104 (4.1.5), CPB-COM-2111 (4.2.6)
At what frame does malicious scanning begin?
Frame 14136, First SYN Packet sent to 192.168.56.1 to port 443.

2 TASK NUMBER: CPB-COM-2104 (4.1.5), CPB-COM-2111 (4.2.6)
What type of scan was used?

SYN stealth scan, targeting all scan default ports.

3. TASK NUMBER: CPB-COM-2108 (4.2.2)
What MITRE ATT&CK TTP or number would appropriately describe this event (Give at least 1)?

Network Service Discovery: T1046
Active Scanning: T1595

4. Extra Credit: What were the DNS answers for IP address for armytimes.com?

Frame 22823: 76.73.236.154, 76.73.236.170
![DNS Answer for armytimes.com](dns.png)

Remedial Training:
    https://dfirmadness.com/case-001-pcap-analysis/

