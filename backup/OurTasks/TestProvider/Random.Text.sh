#!/bin/bash
cat /dev/urandom | tr -dc 'a-zA-Z ' | fold -w $(($RANDOM % $1)) | head -n 1
