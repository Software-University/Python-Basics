#!/bin/bash
echo $1 "`cat /dev/urandom | tr -dc '0-9' | fold -w 1 | head -n 1`"

