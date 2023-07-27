# Description
    CPT Rex made a mistake with powershell and accidentally archived his files smany times. A maximum of three common compression techniques used in this challenge.

# Solution
CTF{infinite_loops_are_rough}

```
#!/bin/bash 


name="documents.zip"
prev=0
for i in {1000..1} 
  do
    res=$(file $name$i)
    echo $res
    if [[ $res == *"Zip"* ]]

     then
       echo "y" | unzip -q $name$i
   # unzip -q $name$i

     else
        tar -xvf $name$i
     fi
done
```

# Source Code

The initial commands used to create the challenge.
`zip output-archive file1 file2 file3`
`tar -cjvf output-archive  file1 file2 file3`

```
#!/bin/bash 


name="documents.zip"
echo "$name"
prev=0
for i in {1..1000} 
  do
    if ((i % 2 == 0)) 
     then
        zip $name$i $name$prev
        prev=$i
     else
        if ((i==1))
         then 
           tar -cjvf $name$i $1
           prev=$i 
       else
           tar -cjvf $name$i $name$prev
           prev=$i 
       fi
    fi 
done


```
