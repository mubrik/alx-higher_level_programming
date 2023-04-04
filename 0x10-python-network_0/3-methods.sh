#!/bin/bash
# check body of 200 req
curl -sI "$1" | grep "Allow:" | cut -d" " -f 2-
