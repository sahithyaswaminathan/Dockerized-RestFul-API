# Dockerized RestFul API Implementation

```
SAHITHYA SWAMINATHAN
24-02-2019
```

### Requirements

Docker Toolbox for Windows and Virtual machine
Python 3.4 or above

#### Problem Definition

This project is intended to build Customer details database using REST API in Python. Flask is used to build the web framework and the app script is executed inside the docker container. Docker is used because it provides a hassle free environment to create, deploy and run scripts. 

##### Installations

###### Docker Toolbox: 
Step by step procedure to install docker toolbox is available in https://docs.docker.com/toolbox/toolbox_install_windows/

###### Configure VMbox to view localhost:
-> Once the docker machine is created, go to VMBox and click on Settings (of specific env machine) -> Network -> Adaptor 1 -> Advanced Configuration -> Port Forwarding -> Add new port forwarding -> Under 'Host port' = 80, 'Guest port' = 80

###### Install Flask and Flask_restful library:
Use the link to install flask - http://flask.pocoo.org/docs/1.0/installation/

###### Install Postman App:
This App will act as a client and help us to check the response

### Result

At the end of the project, you will be able to 'POST' new customer details into the Customer Database, 'GET' the details of a specific company, 'DELETE' specific company details. The action message will be visible in Postman App
