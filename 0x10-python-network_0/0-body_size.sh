#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

url="$1"

# Use curl to fetch the content of the URL
response=$(curl -s "$url")

# Use wc -c to count the number of characters in the response(body size)
body_size=$(echo -n "$response" | wc -c)
# Print it
echo "$body_size"
