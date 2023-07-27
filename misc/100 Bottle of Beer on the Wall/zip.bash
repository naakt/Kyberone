zip_count=10000
i=0
fname=flag.txt
while [ "$i" -lt "$zip_count" ]; do
    zip "f$i" "$fname"
    fname="f$i.zip"
    i=$((i+1))
done
