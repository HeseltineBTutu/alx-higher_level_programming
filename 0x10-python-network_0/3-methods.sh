#!/bin/bash
# This script displays HTTP methods allowed by a server
curl -s -I -X OPTIONS $1 | grep -i 'Allow:' | cut -d':' -f2 | tr -d ' '
