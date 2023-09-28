#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me 
# that causes the server to respond with a message containing You got me!, in the body of the response.
# curl -sL 0.0.0.0:5000/catch_me -d "user_id=98" -X PUT -H "Origin:School"
curl -sLX PUT -H "Origin:School" -d "user_id=98" "0.0.0.0:5000/catch_me"
