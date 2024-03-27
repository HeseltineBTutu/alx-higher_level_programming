#!/bin/bash
# Sends a GET request to a URL and displays the body of the response
curl -s -X GET "$1" -o /tmp/body_response && grep -Pzo '(?<=<body>).*?(?=</body>)' /tmp/body_response
