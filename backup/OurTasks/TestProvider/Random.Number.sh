#!/bin/bash
if [[ $(($RANDOM % 2)) == 1 ]]
then
	echo -n "-"
fi
echo "`cat /dev/urandom | tr -dc '0-9' | fold -w $(($RANDOM % $1 + 1)) | head -n 1`"

