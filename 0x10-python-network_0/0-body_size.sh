#!/bin/bash
# check body size of curl
curl -sSL $1 | wc -c
