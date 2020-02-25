
### Objectives
YWBAT 
* design OOPs to optimize tasks

# Creating an ORM
ORMs are ways for us to interact with dbs using python (in our case). You can build them with other languages though such as javascript, scala, etc. 

To start building an ORM, open the my_class.py file
* Create a class called MyDatabase
* Then create an init method that takes in the connection information of your class
    * in other words when you instantiate your object you should be able to connect to your database
* Create methods for your class to
    * query the tables in your database
    * query all the information for a given table
    * query the columns of a table
* After this create a child class called Customers
* Create methods to
    * query all the information from the Customers class (but ideally this should be inherited from your parent class, so you really don't have to do this)
    * query specific customers given a column and a value (you can pick)
    * create your own function specific to the customers table
* Create another class for a given table and write at least 3 methods

Use Jupyter to import your file and test your methods

Example

```python
my_db = MyDatabase(params)
my_db.list_tables()
```


```python

```
