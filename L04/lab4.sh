#!/bin/bash

# Use First Argument As Working Directory
WDIR="$(pwd)"
cd "$WDIR"

if [ $# -eq 3 ] ; then
    if [ ! -f "$3".txt ] ; then
        touch "$3".txt
        echo "$USER" > "$3".txt

    elif [ ! -d backup ] ; then
        mkdir backup
        cp "$3".txt backup
    fi


    if [ $2 -eq 3 ] ; then
        if [ -f backup/"$3".txt ] ; then
            cp backup/"$3".txt "$WDIR"
            rm backup/"$3".txt
        fi
    fi





else
    if [ ! -f file1.txt ] ; then
        touch file1.txt
        echo "$USER" > file1.txt

    elif [ ! -d backup ] ; then
        mkdir backup
        cp file1.txt backup
    fi


    if [ $2 -eq 3 ] ; then
	if [ -f backup/file1.txt ] ; then
            cp backup/file1.txt "$WDIR"
            rm backup/file1.txt
	fi
    fi

fi



counter=1
if [ $# -gt 2 ] ; then
    touch excess.txt
    for var in "$@"
    do
	if [ $counter -gt 3 ] ; then
            echo "$var" >> excess.txt
	fi
	counter=$((counter+1))
    done
fi

echo "Finished"