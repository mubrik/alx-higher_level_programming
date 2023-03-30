#!/bin/bash
# check body of 200 req
curl -s -w '\n%{http_code}\n' "$1" | awk 'END {if ($0 ~ /200/) {show_body=1};} /^$/ {body=1;next} {if (show_body && body) print $0}'
