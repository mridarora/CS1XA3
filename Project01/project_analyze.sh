#!/bin/bash

echo "1. FIXME Log"
echo "2. File Size List"
echo "3. File Type Count"
read -p "Enter the feature : " inp 

if [ "$inp" -eq 1 ] ; then
	s=$(find .. -type f)
	if [ -f "tempfixme1" ] ; then
		echo "inside 1"
		echo "$s" > tempfixme1
	else
		touch tempfixme1
		echo "inside 2"
		echo "$s" > tempfixme1
	fi
	if [ -f "fixme.log" ] ; then
		rm fixme.log
	fi
	noflines=($(wc -l tempfixme1))
	for ((i=1 ; i<"$noflines"+1 ; i++)) ; do
		ch=$(sed "${i}q;d" tempfixme1)
		ta=$(tail -1 "$ch")
		if [ "$ta" == *"#FIXME"* ] ; then
			if [[ -f "fixme.log" ]] ; then
				echo "$ch" >> fixme.log
			else
				touch fixme.log
				echo "$ch" >> fixme.log
			fi
		fi
	done
	rm tempfixme1

elif [ "$inp" -eq 2 ] ; then
	s=$(find .. -type f)
	if [ -f "tempfile1" ] ; then
		echo "$s" > tempfile1
	else
		touch tempfile1
		echo "$s" > tempfile1
	fi
	noflines=($(wc -l tempfile1))
	if [ -f "tempfile2" ] ; then
		truncate -s 0 tempfile2
	fi
	if [ -f "tempfile3" ] ; then
		truncate -s 0 tempfile3
	fi
	for ((i=1 ; i<"$noflines"+1 ; i++)) ; do
		ch=$(sed "${i}q;d" tempfile1)
		size=($(stat --printf="%s" "$ch"))
			if [ -f "tempfile2" ] ; then
				echo "$size     :     $ch" >> tempfile2
			else
				touch tempfile2
				echo "$size     :     $ch" >> tempfile2
			fi
	done
	ans=$(sort -n tempfile2)
	rm tempfile*
	echo "$ans" 

elif [ "$inp" -eq 3 ] ; then 
	read -p "Enter the file extension:  " us
	ans=$(find .. -type f -name "*.$us" | wc -l)
	echo "$ans"
else 
	echo "Wrong Input"
fi
