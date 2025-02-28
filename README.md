#Craigslist Django REST API

Here are a list of the routes , all return JSON:
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
