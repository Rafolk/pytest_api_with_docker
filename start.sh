#!/bin/bash

help_message="Usage: start.sh [Options]

Options:
    --start           start API container;
    --stop            stop API container;
    --reboot          reboot API container."

#flags:
fl_start=false
fl_stop=false
fl_reboot=false

while test $# -gt 0
do
    case "$1" in
        --start)
            if $fl_start
            then
                echo "Invalid flag."
                echo "$help_message"
                exit 1
            fi
            if ! $fl_start
            then
                fl_start=true
            fi
            ;;
        --stop)
            if $fl_stop
            then
                echo "Invalid flag."
                echo "$help_message"
                exit 1
            fi
            if ! $fl_stop
            then
                fl_stop=true
            fi
            ;;
        --reboot)
            if $fl_reboot
            then
                echo "Invalid flag."
                echo "$help_message"
                exit 1
            fi
            if ! $fl_reboot
            then
                fl_reboot=true
            fi
            ;;
        --help|-h)
            echo "$help_message"
            exit 1
            ;;
        *)
            echo "Bad option '$1'. Allowed options are: --start; --stop; --help."
            echo "$help_message"
            exit 1
            ;;
    esac
    shift
done

# Start API container
if [ "$fl_start" = true ]; then
    docker run -d -p 3001:3001 rafolk/training_api:latest &&
	  echo "API-container has been launched."
fi

# Stop API container
if [ "$fl_stop" = true ]; then
    docker ps -f 'publish=3001' -q | xargs docker rm -f &&
	  echo "API-container was deleted."
fi

# Reboot API container
if [ "$fl_reboot" = true ]; then
    docker ps -f 'publish=3001' -q | xargs docker rm -f &&
	  echo "API-container was deleted." &&
	  docker run -d -p 3001:3001 rafolk/training_api:latest &&
	  echo "API-container has been launched."
fi

exit 0

# pip3 install -r requirements.txt