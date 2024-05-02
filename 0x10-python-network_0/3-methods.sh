#!/bin/bash
# This script displays HTTP methods allowed by a server
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
