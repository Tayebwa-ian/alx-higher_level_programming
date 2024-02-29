#!/bin/bash
# displays the size of the body of the response
if [ "$#" -eq 1 ]; then
    curl -s -w "%{size_download}" -o /dev/null "$1"
fi
