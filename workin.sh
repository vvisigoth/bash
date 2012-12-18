#!/bin/bash

if [ -n "$1" ]; then
    if [ "$1" == "-l" ]; then
        cat /Users/anthonyarroyo/scripts/worklog.txt
        exit
    elif [ "$1" == "-s" ]; then
        tail -1 /Users/anthonyarroyo/scripts/worklog.txt | awk '{print $1}'
        exit
    elif [ "$1" == "-i" ]; then
        awk -v B=$2$3,E=$4$5 '$3$4 == B, $3$4 == E BEGIN {X=0; TOT=0} {if ($1 == "WORKIN") X=$8; else TOT+=($8-X); print $0} END {print TOT/3600}' /Users/anthonyarroyo/scripts/worklog.txt
        exit
    else
        MESSAGE="$1"
    fi
else
    MESSAGE=""
fi

T1=`date`
T2=`date +"%s"`


if [ ! -f /Users/anthonyarroyo/scripts/worklog.txt ]; then
    STATUS="WORKIN"
else
    PREV=`tail -1 /Users/anthonyarroyo/scripts/worklog.txt | awk '{print $1}'`
    if [ $PREV = "WORKIN" ]; then
        if [ ! -n "$MESSAGE" ]; then
            echo "And what exactly did you work on?"
            read input_variable
            MESSAGE=$input_variable
        fi
        STATUS="CHILLIN"
    else
        STATUS="WORKIN"
    fi
fi

growlnotify -m "$STATUS"
printf "$STATUS\t\t%s\t\t%s\t\t$MESSAGE\n" "$T1" "$T2" >> /Users/anthonyarroyo/scripts/worklog.txt
