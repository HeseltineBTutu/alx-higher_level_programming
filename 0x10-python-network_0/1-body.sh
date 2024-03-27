#!/usr/bash
# This script displays the response body for successful (200) GET requests
response=$(curl -s -w '%{http_code}' -o /dev/null $1)
if [[ $response == "200" ]]; then curl -s $1; fi
