#!/bin/bash 

export DISPLAY=":0";
declare -a arr=("w" "s" "a" "d" "z" "x" "c" "aa" "dd" "")
str=${arr[$1]}
for(( i=0; i <${#str}; i++)); do
   xdotool keydown ${str:$i:1}
   sleep 0.04
   xdotool keyup ${str:$i:1}
   sleep 0.1
done
