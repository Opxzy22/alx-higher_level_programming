#!/bin/bash
# a script that takes in a URL and send a post request
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
