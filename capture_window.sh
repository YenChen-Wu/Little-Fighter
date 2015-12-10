#!/bin/bash

IFS=- # use "local IFS=-" inside the function
export DISPLAY=":0";

ID=$(xdotool search --name "Little Fighter 2" | tail -n 1)
string=$(xdotool getwindowgeometry $ID |sed -n "2p" | sed  "s%  Position: %%g; s% (screen: 0)%%g; s%,%-%g")
set $string
init_x=$1
init_y=$2
string=$(xdotool getwindowgeometry $ID |sed -n "3p" | sed  "s%  Geometry: %%g; s%x%-%g")
set $string
width=$1
height=$2
crop="$width"x"$height"+"$init_x"+"$init_y"
xwd -silent -root | convert - -crop $crop +repage lf2.png
