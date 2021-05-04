# pizza-demo-task
Overview:
The following is a django application which is able to store information about different types of Pizzas, having multiple api and functionalities to edit delete list and create pizzas.The database in this project used is Mongodb.

APIs and Functionalities:

1.endpoint to create regular pizza and a square pizza.
    end point :"pizza/"
    method : POST
    input:{
    "type": "regular"/"square",
    "size": id of the sizes available,
    "topping": id of the toppings available
}

2. endpoint which lists the information about all the stored pizza

    end point :"pizza/"
    method : GET

3. endpoint that allows the user to edit any pizza

    endpoint : "pizza/<id of the pizza/>"
    method : PATCH
    input: input:{
    "type": "regular"/"square",
    "size": id of the sizes available,
    "topping": id of the toppings available
}

4.  filtering the list of pizza returned by the API based on Size & Type of Pizza.

    endpoint : pizza/?size=<id of size>&topping=<id of topping>
    method : GET

5.endpoint that allows the user to delete any pizza

    endpoint : "pizza/<id of the pizza/>"
    method : DELETE

6. to get the id of pizza size or pizza toppings :
pizza size :
        endpoint: "PizzaSize/"
        methoid : GET 
        you will get the list of puizza sizes with id
        
pizza toppings :
        endpoint: "PizzaToppings/"
        methoid : GET 
        you will get the list of puizza pizza toppings with id

How to run the project: 

1. Clone the code from github repository
2. install all the modules from requirements.txt either in virtual environment or directly in system 1.endpoint
3. makemigrations using - python mamange.py makemigrations.
4. migrate using - python mamange.py migrate.
5.run the server using - python mamange.py runserver.
