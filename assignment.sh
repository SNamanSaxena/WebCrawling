
#!/bin/bash

url=$1
item_count=$2
PYTHON="/usr/bin/python3"
echo $url
echo $item_count

result=$PYTHON ./soup.py $url $item_count
echo $result
