# PLATO
This is a REST API which caters to a part of an online food ordering system
(created as a part of Zappos Data Science Internship Challenge)

## Technologies used
- Flask Web Framework written in Python 
- MySQL database

## Directions to get this code started
1. Fork this repository
2. Clone this repository
3. Create a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) - dependencies can be found in the file requirements.txt in the home folder of this repo
4. Active the virtual environment
5. run `python run.py` to get the server started

## Supported Endpoints
All the endpoints work with [JSON](https://www.wired.com/2010/02/get_started_with_json/), ie. Post data is required in JSON format and GET data is responded in JSON format too. 

### Restaurant
- GET `<domainname>/restaurant` returns all the restaurants
- GET `<domainname>/restaurant/<rid>` returns details of the restaurant Id mentioned
- POST `<domainname>/restaurant/add` saves the data 
- DELETE `<domainname>/restaurant/<rid>` deletes the restaurant data and all the menu and menu items associated with it

### Menu
- GET `<domainname>/menu` returns all the menu categories
- GET `<domainname>/menu/<rid>` returns menu categories of the mentioned restaurant
- POST `<domainname>/menu/add/<rid>` saves the data 
- DELETE `<domainname>/menu/delete` deletes the menu data associated with the restaurant id

### Menu Items
- GET `<domainname>/menu_item/<rid>/` returns all the menu items according to the menu category of the mentioned restaurant
- GET `<domainname>/menu_item/<rid>/<category>` returns menu items of the mentioned restaurant and category (drinks, snacks etc.)
- POST `<domainname>/menu_item/add` saves the data (required params : rid, category, name, price)
- DELETE `<domainname>/menu/delete` deletes the menu item according to restaurant id, category and item name 

### Feel free to let me know if there are any errors/improvements in the code above. 
