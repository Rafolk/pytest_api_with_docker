#!/bin/bash

# В планах добавить:
# pip3 install -r requirements.txt
# запуск тестов после старта контейнеров

help_message="Usage: start.sh [Options]

Options:
    --start           		start all container - API and Allure services and tests;
    --stop            		stop all container;
    --reboot_api          reboot API container."

#flags:
fl_start=false
fl_stop=false
fl_reboot_api=false

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
        --reboot_api)
            if $fl_reboot_api
            then
                echo "Invalid flag."
                echo "$help_message"
                exit 1
            fi
            if ! $fl_reboot_api
            then
                fl_reboot_api=true
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

# start all container - API and Allure services
if [ "$fl_start" = true ]; then
    docker-compose up -d allure allure-ui test-api &&
	  echo "API and Allure services has been launched." #&&
	  #python -m pytest tests/. --alluredir=allure-results &&
	  #echo "The tests were completed."
fi

# stop all container
if [ "$fl_stop" = true ]; then
    docker-compose down && rm -rf ./allure-re* &&
	  echo "All container was deleted."
fi

# reboot API container
if [ "$fl_reboot_api" = true ]; then
    docker ps -f 'publish=3001' -q | xargs docker rm -f &&
	  echo "API-container was deleted." &&
	  docker-compose up -d test-api &&
	  echo "API-container has been launched."
fi

exit 0
