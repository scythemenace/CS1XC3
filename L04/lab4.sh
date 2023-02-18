#!/bin/bash
# Use First Argument As Working Directory
WDIR="$(pwd)"
cd "$WDIR"

if [ $# -eq 3 ] ; then

        if [ "$2" -eq 1 ] ; then
            if [ ! -e "$3" ] ; then
                touch "$3"
                echo "$USER" > "$3"
            fi

        elif [ "$2" -eq 2 ] ; then
            if [ -e "$3" ] ; then
                mkdir backup
                cp "$3" backup
            fi


        elif [ "$2" -eq 3 ] ; then
            if [ -e backup/"$3" ] ; then
                cp backup/"$3" "$WDIR"
                rm backup/"$3"

            fi

      fi



elif [ $# -lt 3 ] ; then

    if [ "$2" -eq 1 ] ; then
        if [ ! -e file1.txt ] ; then
            touch file1.txt
              echo "$USER" > file1.txt
        fi

    elif [ "$2" -eq 2 ] ; then
        if [ -e file1.txt ] ; then
            mkdir backup
            cp file1.txt backup
        fi


    elif [ "$2" -eq 3 ] ; then
        if [ -e backup/file1.txt ] ; then
            cp backup/file1.txt "$WDIR"
            rm backup/file1.txt

        fi

    fi




elif [ $# -gt 3 ] ; then
    count=1
    touch excess.txt
    for arg in "$@"
        do
                if [ $count -gt 3 ] ; then
                echo "$arg" >> excess.txt
                fi
                count=$((count+1))
      done



fi

echo "Finished"