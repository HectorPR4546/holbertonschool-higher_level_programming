Basics of HTTP/HTTPS
1. Differences Between HTTP and HTTPS
Feature	HTTP	HTTPS
Security	No encryption (plaintext)	Encrypted (SSL/TLS)
Port	Port 80	Port 443
Data Integrity	Vulnerable to tampering	Prevents tampering
Authentication	No identity verification	Uses certificates (trusted)
Use Case	Non-sensitive sites (blogs)	Secure sites (banking, logins)

🔹 Key Takeaway:
HTTPS = HTTP + Encryption (SSL/TLS). Essential for security.
2. HTTP Request & Response Structure
Example HTTP Request
http

GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html

    Method: GET (retrieve data)

    Path: /index.html (requested resource)

    Headers:

        Host → Domain name

        User-Agent → Client (browser) info

        Accept → Expected response format

Example HTTP Response
http

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<!DOCTYPE html>
<html>...</html>

    Status: 200 OK (success)

    Headers:

        Content-Type → Format (text/html)

        Content-Length → Response size

    Body: Actual HTML content

3. Common HTTP Methods
Method	Description	Use Case
GET	Retrieve data	Loading a webpage, API fetch
POST	Send data (create)	Form submission, file upload
PUT	Update existing data	Editing a user profile
DELETE	Remove data	Deleting a file from a server
4. Common HTTP Status Codes
Code	Name	Description	Scenario
200	OK	Success	Page loaded correctly
301	Moved Permanently	Resource moved to a new URL	Website domain change
404	Not Found	Resource doesn’t exist	Wrong URL entered
403	Forbidden	Access denied	Unauthorized admin access
500	Internal Server Error	Server failed to process request	Backend code crash
Summary

✔ HTTP = Unsecured, HTTPS = Secured (SSL/TLS).
✔ HTTP Request = Method (GET, POST), Path, Headers, (Optional Body).
✔ HTTP Response = Status Code (200, 404), Headers, Body.
✔ HTTP Methods = Actions (GET, POST, PUT, DELETE).
✔ Status Codes = Success (2xx), Redirection (3xx), Errors (4xx, 5xx).
