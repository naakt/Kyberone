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
       rm $name$i   # unzip -q $name$i

     else
        tar -xvf $name$i
        rm $name$i
     fi
done
