#!/bin/bash

# python3 main.py

# file=$(cat data)

#export DISPLAY=:0.0
export SCREENSAVER='/home/alok/Pictures/screensavers'
file=file:///home/alok/Pictures/screensavers/IMG20240629094759.jpg

echo $file

gsettings set org.gnome.desktop.background picture-uri-dark $file
gsettings set org.gnome.desktop.background  picture-options 'stretched'


echo $SCREENSAVER

while [ 1 -eq 1 ]
do 
    for files in "$SCREENSAVER"/*
    do
    if [[ $files == *.heic || $files == *.jpg || $files == *.png ]]; then 
    file_uri="file://$files"
    echo "Setting up $file_uri" 
    gsettings set org.gnome.desktop.background picture-uri-dark "$file_uri"
    fi
    sleep 60
    done

sleep 100
done



#gsettings set org.gnome.desktop.background picture-uri-dark file:///home/alok/Pictures/screensavers/pexels-pixabay-236599.jpg

# gsettings set org.gnome.desktop.background  picture-options 'stretched'
