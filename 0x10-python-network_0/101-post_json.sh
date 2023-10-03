#!/bin/bash

# a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

json_file = "$2"

curl -sX POST -H "content-type: application/json" -d "@$json_file" "$1"
