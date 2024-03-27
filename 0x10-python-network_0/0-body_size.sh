#!/bin/bash
# This script calculates the body size in bytes of a web response
curl -s $1 | wc -c
