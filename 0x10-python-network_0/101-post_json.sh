#!/bin/bash
#a script thats sends a json POST request with the content of the file
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
