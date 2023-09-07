"""
1. Create a list of dictionaries, where each dictionary represents a person with the following information:
name (string)
age (integer)
gender (string)
email (string)
occupation (string)
Example: ```python 

people = [
    {"name": "John", "age": 25, "gender": "male", "email": "john@gmail.com", "occupation": "developer"},
    {"name": "Jane", "age": 30, "gender": "female", "email": "jane@gmail.com", "occupation": "engineer"},
    {"name": "Bob", "age": 35, "gender": "male", "email": "bob@gmail.com", "occupation": "manager"}
]
```

2. Sort the list of dictionaries by age, in descending order.

3. Convert the list of dictionaries into a dictionary of dictionaries, where each key is the name of a person.

Example: ```python
people_dict = {
    "John": {"age": 25, "gender": "male", "email": "john@gmail.com", "occupation": "developer"},
    "Jane": {"age": 30, "gender": "female", "email": "jane@gmail.com", "occupation": "engineer"},
    "Bob": {"age": 35, "gender": "male", "email": "bob@gmail.com", "occupation": "manager"}
}
```

4. Use a set to find the unique occupations in the list of dictionaries.

5. Use a list comprehension to create a list of all the email addresses in the list of dictionaries.

These exercises cover several important aspects of working with Python data structures, including sorting, nested dictionaries, sets, and list comprehensions. They should help you develop a better understanding of these concepts and how to use them effectively in your Python code. 
Good luck!
"""

people = [
    {"name": "John", "age": 25, "gender": "male", "email": "john@gmail.com", "occupation": "developer"},
    {"name": "Jane", "age": 30, "gender": "female", "email": "jane@gmail.com", "occupation": "engineer"},
    {"name": "Bob", "age": 35, "gender": "male", "email": "bob@gmail.com", "occupation": "manager"}
]

# print(people[0]["age"])
for i in people:
    print(i.get("age"))
people_dict = {
    "John": {"age": 25, "gender": "male", "email": "john@gmail.com", "occupation": "developer"},
    "Jane": {"age": 30, "gender": "female", "email": "jane@gmail.com", "occupation": "engineer"},
    "Bob": {"age": 35, "gender": "male", "email": "bob@gmail.com", "occupation": "manager"}
}


