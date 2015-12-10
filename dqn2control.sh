#!/bin/bash 

export DISPLAY=":0";
declare -a arr=("w" "s" "a" "d" "z" "x" "c" "aa" "dd" "")

str=${arr[$1]}

if [ "$1" -le "3" ]
then
	slp=0.6
else
	slp=0.04
fi

for(( i=0; i <${#str}; i++)); do
   xdotool keydown ${str:$i:1}
   sleep $slp
   xdotool keyup ${str:$i:1}
   sleep 0.1
done
