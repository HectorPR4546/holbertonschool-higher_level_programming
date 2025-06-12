Consuming APIs with curl
1. Installing and Verifying curl
bash

# Install curl (Ubuntu/Debian)
sudo apt update && sudo apt install curl

# Verify installation
curl --version

Expected Output:
text

curl 7.68.0 (x86_64-pc-linux-gnu) 
Protocols: http https ftp ...

2. Basic curl Commands
Fetch a Webpage
bash

curl http://example.com

Output: HTML content of example.com.
3. Fetching Data from an API (JSONPlaceholder)
GET Request (Retrieve Posts)
bash

curl https://jsonplaceholder.typicode.com/posts

Expected Output (Excerpt):
json

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere...",
    "body": "quia et suscipit..."
  },
  ...
]

GET Headers Only
bash

curl -I https://jsonplaceholder.typicode.com/posts

Output:
text

HTTP/2 200 
content-type: application/json; charset=utf-8
...

4. Sending Data with curl
POST Request (Create a Post)
bash

curl -X POST -d "title=foo&body=bar&userId=1" \
  https://jsonplaceholder.typicode.com/posts

Expected Output:
json

{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}

Key Flags:
Flag	Purpose	Example
-X	Specify HTTP method (GET, POST, etc.)	curl -X POST [URL]
-d	Send request body data	curl -d "key=value" [URL]
-I	Fetch headers only	curl -I [URL]
-H	Add headers (e.g., Content-Type)	curl -H "Content-Type: application/json" [URL]
5. Formatting JSON Output with jq
bash

curl https://jsonplaceholder.typicode.com/posts | jq

Output: Pretty-printed JSON with syntax highlighting (if jq is installed).
Summary

    curl is a CLI tool for making HTTP/HTTPS requests.

    GET Requests: Fetch data (e.g., curl [URL]).

    POST Requests: Send data (e.g., curl -X POST -d "data" [URL]).

    Headers: Use -I to inspect response headers.

    JSON Formatting: Pipe output to jq for readability.

Example Workflow:

    Retrieve data:
    bash

curl https://jsonplaceholder.typicode.com/users

Create a resource:
bash

curl -X POST -d "name=John" https://jsonplaceholder.typicode.com/users
