#!/bin/bash
if [[ $3 == 1 ]]
then
	if [[ $(($RANDOM % 2)) == 1 ]]
	then
		echo -n "-"
	fi
fi
echo -n "`cat /dev/urandom | tr -dc '0-9' | fold -w $(($RANDOM % $1)) | head -n 1`"
echo -n "."
echo "`cat /dev/urandom | tr -dc '0-9' | fold -w $(($RANDOM % $2)) | head -n 1`"

