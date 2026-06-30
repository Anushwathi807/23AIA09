## Logging Middleware
1. In postman below Body open raw and JSON editor 
{
    "stack":"backend",
    "level":"error",
    "package":"handler",
    "message":"received string, expected bool"
}
2. Authorization 
Auth Type - Bearer Token
Token - (given token)
3. Method ['POST']
4. SEND
5. {} JSON output as:
{
    "logID": "f1c0ed7b-69ac-446b-994d-5474b9da778a",
    "message": "log created successfully"
}
6. python3 logging_middleware.py