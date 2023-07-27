#!/bin/bash 

dstname="documents.zip"
echo "$dstname"
prev=0
for i in {1..1000} 
  do
    if ((i % 2 == 0)) 
     then
        zip $dstname$i $dstname$prev
        prev=$i
     else
        if ((i==1))
         then 
           tar -cjvf $dstname$i $1
           prev=$i 
       else
           tar -cjvf $dstname$i $dstname$prev
           prev=$i 
       fi
    fi 
done

