### Calling API from Huggingface

## 1. What is an API ?

API is Application Programming Interface, which acts as a translator between different programm. With this, a program can communicate with other programm.

## 2. API workflow 

1. *Request*: Client sends request to the server to specified what is needed and which actions need to be done. 

2. *Process*: The server executes the requests of the client. 

3. *Response*: The server gives the fulfilled requests back to the client. 

Imagine API is a waiter between the customer and the kitchen. It will carry the *request* food order from the customer to ask the kitchen to *process* food. Then the kitchen will send the food (*response*) back to the customer through the waiter.

## 3. Huggingface API

Huggingface is the Github of open-source model for user to inference (means just takes the pretrained weight from model and apply it without to retrain everything from scratch). 

Register for it at https://huggingface.co/ . Then you can find your api key (needed for authorization and permission to call the model). Find in Settings -> Access tokens

(Thats what I personally used for the code, there is many ways to use it documented carefully in the huggingface already)