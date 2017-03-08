#!/bin/bash
cat /dev/urandom | tr -dc 'a-zA-Z0-9 ' | fold -w $(($RANDOM % $1)) | head -n 1

