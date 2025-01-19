# Assessment 4: Django REST API
to load data : 
    `python manage.py loaddata backup.json to load data`
    

## Due Date
- You will push up your PR on Monday at the beginning of class


## Requirements
- This assessment must be completed using Django/Django REST Framework.
- You must use postgres for your database.
- You must include a `docker-compose.yml` file that specifies two services (containers): one for your postgres database and one for your API.

## Challenge
Everyone loves going on Craigslist to find interesting people and interesting items.  Today, you will build a basic Craigslist CRUD API with nested routes. 

Use the below REST interface to guide your development process.  You will have to reverse engineer the database tables appropriately.

Here are a list of the routes you will need to build. They should all return JSON:
| URI | HTTP Method | Expected Behavior |
| ------------- | ------------- | --------------- |
| `/categories` | GET |  List view of all the categories |
| `/categories` | POST | Creates a new category |
| `/categories/:category_id` | GET | Detail view of a specific category |
| `/categories/:category_id` | PUT | Update a specific category |
| `/categories/:category_id` | DELETE | Delete a specific category |
| `/categories/:category_id/posts` | GET | List view of all the posts for a given category |
| `/categories/:category_id/posts` | POST | Create a new post for a given category |
| `/categories/:category_id/posts/:post_id` | GET  | Detail view of a specific post in a specific category |
| `/categories/:category_id/posts/:post_id` | PUT | Update a specific post ina  specific category |
| `/categories/:category_id/posts/:post_id` | DELETE | Delete a specific post in a specific category |

You are welcome to take whatever approach you think best (functions, views, serializers, etc.), as long as it works.

NOTE: For creating and updating, all endpoints should return some kind of message (either indicating success or failure).

If you would like to include a script to start the containers and run migrations ([for example](https://github.com/foxtrotplatoonew/drf-wine-api/blob/composeV2End/run_compose.sh)), feel free, but it's not a requirement.

