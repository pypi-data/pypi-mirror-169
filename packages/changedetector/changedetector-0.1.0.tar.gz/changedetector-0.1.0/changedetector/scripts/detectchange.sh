#!/usr/bin/env bash

function useChangeDetector () {
    # Get the current time
    now=$(date +"%s")
    # Use changedetector module
    echo "from changedetector import detectchange" > _temp$now.py
    echo "print(detectchange.activate(True))" >> _temp$now.py
    if [ "$1" == "Linux" ]; then
        python3 _temp$now.py
    elif [ "$1" == "Darwin" ]; then
        python3 _temp$now.py
    elif [ "$1" == "Windows" ]; then
        py _temp$now.py
    fi
    # if the python script exits with a 1 error, remove the temp.py file
    if [ $? -eq 1 ]; then
        if [ "$1" == "Linux" ]; then
            rm _temp$now.py
        elif [ "$1" == "Darwin" ]; then
            rm _temp$now.py
        elif [ "$1" == "Windows" ]; then
            del _temp$now.py
        fi
    fi
}

# Check for the OS
if [ "$(uname)" == "Darwin" ]; then
    # Mac OS X platform
    echo "Mac OS X"
    # Use changedetector module
    useChangeDetector "Darwin"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # GNU/Linux platform
    echo "Linux"
    # Use changedetector module
    useChangeDetector "Linux"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    # 32 bits Windows NT platform
    echo "32 bits Windows NT"
    # Use changedetector module
    useChangeDetector "Windows"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    # 64 bits Windows NT platform
    echo "64 bits Windows NT"
    # Use changedetector module
    useChangeDetector "Windows"
fi
