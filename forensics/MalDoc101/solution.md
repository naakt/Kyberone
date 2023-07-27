# Description
    It is common for threat actors to utilize living off the land (LOTL) techniques, such as the execution of PowerShell to further their attacks and transition from macro code. This challenge is intended to show how you can often times perform quick analysis to extract important IOCs. The focus of this exercise is on static techniques for analysis.

# Solution


## Multiple streams contain macros in this document. Provide the number of highest one.

**CTF{16}**

`oledump.py sample.bin`

![Q1](images/q1.png)

The letters `m` and `M` indicate a stream has a macro within it.

## What event is used to begin the execution of the macros?

**CTF{Document_open}**

`olevba sample.bin`

![Q2](images/q2.png)

You want to look for the AutoExec macro. An AutoExec macro runs before any other macros.

## What malware family was this maldoc attempting to drop?

**CTF{emotet}**

`sha256sum sample.bin`

![Q3](images/q3_1.png)

Input the SHA256 hash into VirusTotal to find the malware family name.

![Q3](images/q3_2.png)


## What stream is responsible for the storage of the base64-encoded string?

**CTF{34}**

`olevba sample.bin`

![Q4](images/q4_1.png)

Using oledump to get the stream number of Macros/roubhaol/i09/o.

`oledump.py sample.bin | grep Macros/roubhaol/i09/o`

![Q4](images/q4_2.png)

## This document contains a user-form, provide the name.

**CTF{roubhaol}**

`oledir sample.bin`

![Q5](images/q5.png)

## This document contains an obfuscated base64 encoded string; what value is used to pad (or obfuscate) this string?

**CTF{2342772g3&*gs7712ffvs626fq}**

`oledump.py -s 15 --vbadecompresscorrupt sample.bin`

![Q6](images/q6_1.png)
![Q6](images/q6_2.png)

## What is the program executed by the base64 encoded string?

**CTF{powershell}** or **CTF{powershell.exe}**

`oledump.py -s 34 -d sample.bin`

![Q7](images/q7.png)

## What WMI class is used to create the process to launch the trojan?

**CTF{win32_process}**

![Q8](images/q8.png)

## Multiple domains were contacted to download a trojan. Provide first FQDN?

**CTF{haoqunkong.com}**

![Q9](images/q9.png)