#!/usr/bin/bash
# This script gets a URL and displays response body for 200 status codes 
response=$(curl -s -w '%{http_code}' -o /dev/null $1); [[ $response == 200 ]] && curl -s $1
