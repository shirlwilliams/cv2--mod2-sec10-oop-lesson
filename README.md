
### Questions
* how to debug with print statements

### Crap I USE
* VSCODE
* PYLINTER


### Objectives
YWBAT 
* design OOPs to optimize tasks

### Outline
* just get started with data


```python
from importlib import reload

import numpy as np
import pandas as pd
import sqlite3

import myconn as mc

import matplotlib.pyplot as plt

reload(mc)
```




    <module 'myconn' from '/Users/rafael/flatiron_dsc/curriculum-v2/section10/cv2--mod2-sec10-oop-lesson/myconn.py'>




```python
myconn = mc.MyConn(filename="data.sqlite")
```


```python
cust = mc.Customers(filename='data.sqlite')
```


```python
cust.get_table_description()
```




    (('customerNumber', None, None, None, None, None, None),
     ('customerName', None, None, None, None, None, None),
     ('contactLastName', None, None, None, None, None, None),
     ('contactFirstName', None, None, None, None, None, None),
     ('phone', None, None, None, None, None, None),
     ('addressLine1', None, None, None, None, None, None),
     ('addressLine2', None, None, None, None, None, None),
     ('city', None, None, None, None, None, None),
     ('state', None, None, None, None, None, None),
     ('postalCode', None, None, None, None, None, None),
     ('country', None, None, None, None, None, None),
     ('salesRepEmployeeNumber', None, None, None, None, None, None),
     ('creditLimit', None, None, None, None, None, None))




```python
myconn.list_tables()
```

    orderdetails
    payments
    offices
    customers
    orders
    productlines
    products
    employees
    contacts
    contacts2



```python
myconn.load_table_as_df('employees').head(2)
```

    ---no tablename in object, exception:---
    'MyConn' object has no attribute 'table_name'





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>employeeNumber</th>
      <th>lastName</th>
      <th>firstName</th>
      <th>extension</th>
      <th>email</th>
      <th>officeCode</th>
      <th>reportsTo</th>
      <th>jobTitle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1002</td>
      <td>Murphy</td>
      <td>Diane</td>
      <td>x5800</td>
      <td>dmurphy@classicmodelcars.com</td>
      <td>1</td>
      <td></td>
      <td>President</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1056</td>
      <td>Patterson</td>
      <td>Mary</td>
      <td>x4611</td>
      <td>mpatterso@classicmodelcars.com</td>
      <td>1</td>
      <td>1002</td>
      <td>VP Sales</td>
    </tr>
  </tbody>
</table>
</div>




```python
cust.build_select_all_query()
```




    'select * from customers'




```python

```


```python
myconn.build_select_all_query()
```

    ---no tablename in object, exception:---
    'MyConn' object has no attribute 'table_name'





    'select * from None'




```python
conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()
```


```python
cursor.execute('select * from employees')
```




    <sqlite3.Cursor at 0x11bbaf490>




```python
cursor.description
```




    (('employeeNumber', None, None, None, None, None, None),
     ('lastName', None, None, None, None, None, None),
     ('firstName', None, None, None, None, None, None),
     ('extension', None, None, None, None, None, None),
     ('email', None, None, None, None, None, None),
     ('officeCode', None, None, None, None, None, None),
     ('reportsTo', None, None, None, None, None, None),
     ('jobTitle', None, None, None, None, None, None))




```python
emp = mc.Employees(filename='data.sqlite')
```


```python
emp.get_table_description()
```




    (('employeeNumber', None, None, None, None, None, None),
     ('lastName', None, None, None, None, None, None),
     ('firstName', None, None, None, None, None, None),
     ('extension', None, None, None, None, None, None),
     ('email', None, None, None, None, None, None),
     ('officeCode', None, None, None, None, None, None),
     ('reportsTo', None, None, None, None, None, None),
     ('jobTitle', None, None, None, None, None, None))



### Assessment/What did we learn?
* static methods
* see the workflow for oop
* try and except the baaaaassssttt
* write good docstrings


```python

```
