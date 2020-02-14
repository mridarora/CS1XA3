#!/bin/bash

echo "1. FIXME Log"
echo "2. File Size List"
echo "3. File Type Count"

read -p "Enter a number to implement the feature listed" inp

if [ "$inp" -eq 1 ] ; then
	s=$(find ~/CS1XA3 -type f)
	if [ -f "tempfixme1" ] ; then
		echo "$s" > tempfixme1
	else
		touch tempfixme1
		echo "$s" > tempfixme1
	fi
	if [ -f "fixme.log" ] ; then
		rm fixme.log
	fi
	noflines=($(wc -l tempfixme1))
	for ((i=1 ; i<"$noflines"+1 ; i++)) ; do
		ch=$(sed "${i}q;d" tempfixme1)
		ta=$(tail -1 "$ch")
		if [[ "$ta" == *"#FIXME"* ]] ; then
			if [ -f "fixme.log" ] ; then
				echo "$ch" >> fixme.log
			else
				touch fixme.log
				echo "$ch" >> fixme.log
			fi
		fi
	done
	rm tempfixme1
