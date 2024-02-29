#!/bin/bash
# displays the size of the body of the response
if [ "$#" -ge 1 ]; then
    curl -s -L "$1"
fi
