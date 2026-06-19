# Install dependencies
```
pip install fastapi uvicorn
pip install email-validator
```

# Run service
```
uvicorn main:app --reload
```

# Check service
```
http://127.0.0.1:8000/health
expect: {"status": "ok", "message": "User Service is running"}
```

# Check Swagger UI
```
http://127.0.0.1:8000/docs
expect: Swagger UI page is displayed
```

# Post data
```
curl -X POST http://127.0.0.1:8000/users \
-H "Content-Type: application/json" \
-d '{
  "name":"Alice",
  "email":"alice@example.com"
}'
```
## check 

```
http://127.0.0.1:8000/users/1
expect: {"name":"Alice","email":"alice@example.com","id":1}
```