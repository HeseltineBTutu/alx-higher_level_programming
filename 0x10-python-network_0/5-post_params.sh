#!/bin/bash
# This script sends a POST request with parameters and displays the response
curl -s -X POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' $1
