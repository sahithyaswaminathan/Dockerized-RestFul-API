# Customer data retreival

## Collection: /customer
- GET - view collection
- POST - create new resource

## Resource: /customer/<identifier>
- GET - view resource
- DELETE - delete resource

### Format of the response

```json
{
	"data": "Mixed data type which holds the data of the customer"
	"message": "Status of the api call"
}
```

### List of all customers

- GET /customer

** Response
- 200 OK on success

```json
[
{
	"identifier": "decathlan_india",
	"name": "Decathlan India",
	"subscription": "Gold",
	"size": "50"
},
{
	"identifier": "tesla_motors",
	"name": "Tesla",
	"subscription": "Platinum",
	"size": "100"
}
]
```
### Registering a new device

- POST/customer

** Arguments
-"identifier": string unique identifier
-"name": string name of the company
-"subscription": string plan the company has opted
-"size": string size of the company

If post response has the identifier which is already present, the value will be replaced by the new request
** Response 
-201 createdon success

```json
{
	"identifier": "decathlan_india",
	"name": "Decathlan India",
	"subscription": "Gold",
	"size": "50"
}
```

### Check for customer data

-GET /customer/<identifier>

** Responses
-404 Not found
-200 Ok on sucess

```json
{
	"identifier": "decathlan_india",
	"name": "Decathlan India",
	"subscription": "Gold",
	"size": "50"
}
```

### Delete a customer 

-DELETE /customer/<identifier>

** Responses
-404 Not found if the customer does not exist
-204 No content on success