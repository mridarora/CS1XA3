#!/bin/bash

read -p "Enter the password to execute further commands " pswd
z=$(cat password)
if [ $pswd == $z ] ; then
	echo "1. FIXME Log"
	echo "2. File Size List"
	echo "3. File Type Count"
	echo "4. Backup and Restore"
	echo "5. Tag "
	echo "6. Change Password"
	echo "7. Arrange in alphabatical order"
	echo "8. Checkout Latest Merge"
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

	elif [ "$inp" -eq 4 ] ; then
		echo "1. Backup"
		echo "2. Restore"
		read -p "Enter backup or restore according the given number i.e. 1 for Backup and 2 for Restore" inp
		f=$(find .. -type f -name "*.tmp")
		touch temp
		echo "$f" > temp
		if [ $inp -eq 1 ] ; then
			if [ ! -d "backup" ] ; then
				mkdir backup
			elif [ -d "backup" ] ; then
				rm -r backup
				mkdir backup
			fi
			for x in $f ; do
				mv $x ./backup
			done
			touch ./backup/restore.log
			cp temp ./backup/restore.log
		elif [ $inp -eq 2 ] ; then
			touch filen
			touch dirn
			cat .//backup/restore.log | while read line
			do
				echo $(dirname "${line}") >> dirn
				echo $(basename "${line}") >> filen
			done
			noflines=($(wc -l filen))
			for ((i=1 ; i<"$noflines"+1 ; i++)) ; do
				fl=$(sed "${i}q;d" filen)
				dl=$(sed "${i}q;d" dirn)
				mv ./backup/$fl $dl
			done
			rm dirn filen
		fi
		rm temp

	elif [ "$inp" -eq 5 ] ; then
		cd ..
		read -p "Enter a tag for file " t
		if [ -f ./Project01/"$t.log" ] ; then
			rm ./Project01/"$t.log"
		fi
		touch ./Project01/"$t.log"
		z=`find . -name "*.py" | xargs grep -h "#"* | grep -h "$t"`
		echo "$z" > ./Project01/"$t.log"
 
	elif [ "$inp" -eq 6 ] ; then
		read -p "Enter the old password " opswd
		if [ $opswd == $z ] ; then
			read -p "Enter new password " npswd
			echo $npswd > password
			echo "Password changed successfully"
		else
			echo "Wrong old password"
			echo "Restart the program to change the password"
		fi

	elif [ "$inp" -eq 7 ] ; then
		function sort_f1 {
 			local ar
  			mapfile -t ar < "$1"
  			local x y t
  			for ((x=0; x <= ${#ar[@]} - 2; x++))
  			do
    				for ((y=i + 1; y <= ${#ar[@]} - 1; y++))
    				do
      					local xval yval
      					[[ ${ar[x]} =~ ([^[:space:]]+)[[:space:]]+(.*) ]]
     					xval="${BASH_REMATCH[1]}"
      					[[ ${ar[y]} =~ ([^[:space:]]+)[[:space:]]+(.*) ]]
      					yval=${BASH_REMATCH[1]}
      					if [[ $xval > $yval ]]
      					then
        					t=${ar[x]}
        					ar[x]=${ar[y]}
        					ar[y]=$t
      					fi
    				done
  			done
			printf "%s\n" "${ar[@]}"
			}

		function sort_f2 {
  			local ar
  			mapfile -t ar < "$1"
  			local x y t
  			for ((x=0; x <= ${#ar[@]} - 2; x++))
  			do
    				for ((y=x + 1; y <= ${#ar[@]} - 1; y++))
    				do
      					local xval yval
     					[[ ${ar[x]} =~ ([^[:space:]]+)[[:space:]]+(.*) ]]
      					xval="${BASH_REMATCH[2]}"
      					[[ ${ar[y]} =~ ([^[:space:]]+)[[:space:]]+(.*) ]]
      					yval=${BASH_REMATCH[2]}
      					if [[ $xval > $yval ]]
      					then
        					t=${ar[x]}
        					ar[x]=${ar[y]}
        					ar[y]=$t
      					fi
    				done
  			done
  			printf "%s\n" "${ar[@]}"
			}

		function sort_key_f1 {
  			local a b k val
  			while IFS=' ' read -r a b
  			do
    				k+=("$a")
    				val+=("$a $b")
  			done < "$1"

  			local m n tk tv
  			for ((m=0; m <= ${#k[@]} - 2; m++))
 			do
    				for ((n=m + 1; n <= ${#k[@]} - 1; n++))
    				do
      					if [[ ${k[m]} > ${k[n]} ]]
      					then
        					# swap keys
        					tk=${k[m]}
        					k[m]=${k[n]}
        					k[n]=$tk
        					# swap values
        					tv=${val[m]}
       		 				val[m]=${val[n]}
        					val[n]=$tv
      					fi
    				done
  			done
  			printf "%s\n" "${val[@]}"
			}

		function sort_key_f2 {
  			local a b k val
  			while IFS=' ' read -r a b
  			do
    				k+=("$b")
    				val+=("$a $b")
  			done < "$1"

  			local m n tk tv
  			for ((m=0; m <= ${#k[@]} - 2; m++))
  			do
    				for ((n=m + 1; n <= ${#k[@]} - 1; n++))
    				do
      					if [[ ${k[m]} -gt ${k[n]} ]]
      					then
      						# swap keys
        					tk=${k[m]}
        					k[m]=${k[n]}
        					k[n]=$tk
        					# swap values
        					tv=${val[m]}
        					val[m]=${val[n]}
        					val[n]=$tv
      					fi
    				done
  			done
  			printf "%s\n" "${val[@]}"
			}

	elif [ "$inp" -eq 8 ] ; then
		git log --all --grep='merge' -n 1 | grep -e ".{50}" | git checkout

	else 
		echo "Wrong Input"
	fi
else
	echo "Wrong Password! Please try again by running the program again."
fi
