# S4_HTTP_Web_APIs
## Server App EndPoints
## Students
Get Students with Headers
```bash
curl -i -X GET -H 'Origin:localhost:40000' http://127.0.0.1:8080/students
```
## Interests
GET Interests with Headers
```bash
curl -i -X GET -H 'Origin:localhost:40000' http://127.0.0.1:8080/interests
```

POST Interests with Headers
```bash
curl -i -X POST -H 'Origin:localhost:40000' -H 'Content-Type:application/json' -d '{"name":"Islands of Danger"}' http:
//127.0.0.1:8080/interests
```

PATCH Interests with Headers
```bash
curl -i -X PATCH -H 'Origin:localhost:40000' -H 'Content-Type:application/json' -d '{"name":"Islands of Danger P2"}' http://127.0.0.1:8080/interests/27
```

DELETE Interests with Headers
```bash
curl -i -X DELETE -H 'Origin:localhost:40000' -H 'Content-Type:application/json' -d '{"name":"Islands of Danger P2"}' http://127.0.0.1:8080/interests/2
7
```