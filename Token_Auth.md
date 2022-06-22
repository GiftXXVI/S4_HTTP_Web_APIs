# JSON Web Token (JWT)
## What is a JWT?
- JSON Web Token or JWT, is a standard for safely passing security information (specifically claims) between applications in a simple, optionally validated and/or encrypted, format.
- The standard is supported by all major web frameworks. (flask, Django, Express ...)
## Claims
- Claims are definitions or assertions made about a certain party or object. (examples: Role, Permission ...)
- Some of these claims and their meaning are defined as part of the JWT spec. 
- Standards claims allow frameworks to be able to check expiry/validity automatically
- Others are defined by the developer.
## Standard Claims
Claim	Name	    Format	Usage
‘exp’	Expiration	int	    The time after which the token is invalid.
‘nbf’	Not Before	int	    The time before which the token is invalid.
‘iss’	Issuer	    str	    The principal that issued the JWT.
‘aud’	Audience	str or list(str)	The recipient that the JWT is intended for.
‘iat’	Issued At	int	    The time at which the JWT was issued.
## Why we use JWTs
They are simple,compact and usable.
We will use them for:
- Authentication: to identify the user.
- Authorization: to evaluate the user's permissions.
- Stateless sessions: digital signatures are used to validate the data against tampering.
## Dissecting a JWT
A JWT is made of the following parts
- Header: Holds metadata such as encryption type
- Payload: Holds user-identifying data
- Signature: Holds the signature of the token

Example:

Encoded:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cThIIoDvwdueQB468K5xDc5633seEFoqwxjF_xSJyQQ 

Decoded:

Header (DS Algorithm name and Token type):

{
  "alg": "HS256",
  "typ": "JWT"
}

Payload (Claims):

{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}

Signature:
Hash of Header and Payload. May be encrypted with the private key of the server (issuer) for enhanced security (in this case, it is signed). In this case, the hash is protected from tampering.

## Validating a JWT
If a JWT payload can be read and edited how does it stay secure?
Validating a JWT can be done by re-hashing the token using a secret key and comparing the result with the JWT signature

## Storing a JWT
Explain to students the different methods of storing a token such as local storage
## Sending a JWT
Demo: Sending a JWT using Postman
## Handling JWT Errors
Demonstrate or talk about 401 and 403 scenarios.