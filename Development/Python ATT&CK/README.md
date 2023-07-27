# Python ATT&CK (1/4)
## Challenge
Ready to do some programming? This very important assignment requires using the mitreattack package for Python to perform some TTP Analysis.

This repository will be a great reference for this series of challenges:
https://github.com/mitre-attack/mitreattack-python/tree/master/mitreattack/attackToExcel

You can install the required package using the following command:
> pip install mitreattack-python

Here is the beginning of the program:
> import mitreattack.attackToExcel.attackToExcel as attackToExcel
> import mitreattack.attackToExcel.stixToDf as stixToDf
> 
> attackdata = attackToExcel.get_stix_data("enterprise-attack")
> groups_data = stixToDf.groupsToDf(attackdata)

After running the above script, fill in the blank from the output:
mitreattack.attackToExcel.attackToExcel:get_stix_data:69 - Downloading ATT&CK data from _____________________

## Solution:
FLAG: github.com/mitre/cti


# Python ATT&CK (2/4)
## Challenge
Alright, now you take over the script. Go ahead and compile a list of TTPs for each of the following APTs.
> apt_list = ["APT28", "APT29", "Dragonfly", "Gamaredon Group", "Dragonfly", "Sandworm Team", "Turla", "Wizard Spider"]

The answer to this challenge will be the number of techniques associated with APT29.

## Solution:
FLAG: 105


# Python ATT&CK (3/4)
## Challenge
Good job on getting this far! Lets do some analysis and identify what techniques are most common amount the APTs.

Provide a list of which techniques are associated with at least 6 of the 7 APTs (in numerical order using the format shown below).

Example:
'T1005', 'T1027', 'T1059.001', 'T1059.003'

## Solution:
FLAG: 'T1005', 'T1027', 'T1059.001', 'T1059.003', 'T1070.004', 'T1071.001', 'T1083', 'T1105', 'T1204.002', 'T1547.001', 'T1566.001', 'T1588.002'


# Python ATT&CK (4/4)
## Challenge
Nice job! By this point, you should hopefully have a list of all the techniques associated with the APTs. Which tactic has the most associated techniques from that list? 

Free Hint - The following might be useful:
> techniques_data = stixToDf.techniquesToDf(attackdata, "enterprise-attack")

Provide the both the tactic T# and the number of associated TTPs as a comma seperated list.

Example:
TA0005, 24

## Solution:
FLAG: TA0005, 46