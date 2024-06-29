# API Web Server

Term 2, Assignment 2  
Diploma of IT - Web Development  
Coder Academy

## Github Repository

https://github.com/jmcaluyafuentes/flask-recipe-api

## Purpose

This API web server is an assignment for Term 2 in the Coder Academy Diploma of IT. It aims to provide students with practical experience in developing a fully functional web application backend using modern web development technologies and best practices. My project involves creating a recipe management system that allows users to manage and discover recipes, leveraging Flask for the web framework and PostgreSQL for the relational database management system.

## Description

This API web server, named Flask Recipe API, is designed to manage a recipe application where users can create, save, and browse recipes. Built using Flask, a lightweight Python web framework, this server provides a robust backend for handling user authentication, recipe management, and data persistence using a PostgreSQL database.

1. User Management

    - Admin users can add new users to the platform.
    - Admin users can update and delete users.
    - User authentication and authorization to ensure secure access to the API endpoints.

2. Recipe Management

    - Users can create, update, and delete their own recipes.
    - Recipes can be marked as public or private.
    - Admins have the ability to delete a recipe (e.g., if it did not comply with the guidelines).

3. Recipe Discovery

    - Users can browse public recipes.
    - Users can filter recipes based on various criteria like cuisine, preparation time, etc.
    - Users can get a random recipe suggestion if unsure of what to cook.

4. Recipe Details

    - Recipes consist of step-by-step instructions that are ordered to ensure clarity.

## Requirements

### R1: Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

In our busy lives, many people, including my family, often struggle in planning meals and managing recipes. One of the problems that this app solves is the lack of organization in managing recipes. The abundance of recipes from diverse sources and blogs on the internet often overwhelms and presents challenges in organizing them (Laura 2010). The app offers user accounts, allowing individuals to consolidate and manage their recipes in a single, centralized location. This feature enables users to conveniently access their preferred recipes whenever they need them.

Meal planning is also a challenge that this app aims to solve. Deciding what to cook, especially when busy, can be quite time-consuming. To solve this problem, the app includes a feature that enables users to randomly select a recipe from their collection or from publicly available recipes. This simplifies the decision-making process, making it easier for users to decide on their next meal quickly. Additionally, users have the option to save public recipes to their personal accounts, allowing them to build a curated collection of meals that align with their preferences and support their meal planning efforts.

Customized searching is helpful for users with specific dietary preferences or time constraints. This app has filtering options that allow users to search for recipes based on criteria such as type of cuisine and preparation time. This feature helps users find recipes that match their specific needs and preferences.

To maintain the integrity of the platform, this app includes several administrative features. Admins can add users to the platform to ensure a controlled and secure user base. The admins have the authority to delete public recipes that do not comply with the guidelines. Users also have control over their accounts, with the ability to create, update, and delete their own recipes.

### R2: Describe the way tasks are allocated and tracked in your project.

I used Trello in managing my tasks due to its good visual, straightforward and user-friendly components.

Link to my Trello board --> https://trello.com/b/lqrZakZf/t2a2-api-web-server

I structured my Trello board into three primary lists: To Do, In Progress, and Completed. Before creating the tasks, I reviewed my notes from previous classes to plan my workflow. Initially, I placed all main tasks (represented by cards) into the To Do section. In order for me to manage the project effectively, I broke down each card into actionable steps using Trello's checklist feature. Additionally, I set due dates to manage my time effectively. Below is an example to illustrate how I organized a main task along with its corresponding subtasks:

![Trello sample card with subtasks](./markdown-images/card-sample.png)

After completing the planning phase, I moved the relevant cards from the To Do section to the In Progress section to initiate work. Here's a snapshot of my board as of June 15th:

![A card with sub tasks](./markdown-images/trello-1-15June.png)

Once I completed all the subtasks on a card, I move it to the Completed section to clear my focus and concentrate on remaining tasks. Here's an example of a card "Design the database & make ERD" and its activity log:

![Trello sample of completed card](./markdown-images/card-design-database.png)

![Trello sample of card activity log](./markdown-images/card-design-database-log.png)

Updated progress on my board as of 19th of June:

![Trello board on 19th June](./markdown-images/trello-2-19June.png)

Updated progress on my board as of 22nd of June:

![Trello board on 22nd June](./markdown-images/trello-3-22June.png)

There were instances where I needed to extend the due dates because of the unforeseen complexities or personal reasons. In such cases, I made sure to review the tasks and adjust the timelines reasonably. Additionally, I encountered situations where I realized some subtasks were overlooked during the initial planning phase and prompted me to add them later. Below is the updated progress of my board as of 25th of June:

![Trello board on 25th June](./markdown-images/trello-4-25June.png)

In addition to task management in Trello, we held daily standups on Discord. These standups were beneficial as it allowed me to evaluate my progress by answering key questions. It helped me process my thoughts and assess my remaining tasks to determine if I was on track, if there were other tasks I needed to add, or if I needed to adjust my due dates. Standups provided a daily reminder to keep me focused on my goals. Here are some snapshots:

![Daily standups on 24th June](./markdown-images/standups-1.png)

I also used Git for source control and regularly pushed my changes to a GitHub repository. This allowed me to track the changes and their descriptions effectively. In case of errors while coding, I could revert to a previous version, which was particularly beneficial given the modular nature of my project. Additionally, the GitHub repository served as a backup of my codebase and I could retrieve it in case of issues with my local copies such as corruption or loss. Here is a sample snapshot of my commits in GitHub:




### R3: List and explain the third-party services, packages and dependencies used in this app.

### R4: Explain the benefits and drawbacks of this app’s underlying database system.

### R5: Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

### R6: Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. 

#### This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

### R7: Explain the implemented models and their relationships, including how the relationships aid the database implementation.

#### This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

### R8: Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:

- HTTP verb  
- Path or route  
- Any required body or header data  
- Response

Bruno app is an API client that allows you to construct, test, and debug HTTP requests. The following are endpoints of the Flask Recipe API and their details.

![Bruno app snapshot](./markdown-images/endpoints/bruno.png)

### 1. Route: /users/login

HTTP Request Verb: POST  
URL Parameters: None

Required Body:

* email: User's email address  
* password: User's password (minimum 8 characters)

Header Data: None  
Expected Response: JWT token  
Status Code: 200 OK

Description: This endpoint allows users (and admin) to log in by providing their email and password. Upon successful authentication, a JWT token is returned for use in subsequent authenticated requests.

![Bruno app snapshot](./markdown-images/endpoints/users_login-admin_Success.png)

#### Possible Errors

400 Bad Request: If either email or password is not provided.

![Bruno app snapshot](./markdown-images/endpoints/users_login-admin_No-Email-or-Password.png)

400 Bad Request: If request has no body.

![Bruno app snapshot](./markdown-images/endpoints/users_login-admin_No-Body.png)

401 Unauthorized: Invalid email or password.

![Bruno app snapshot](./markdown-images/endpoints/users_login-admin_Invalid-Email_Password.png)

### 2. Route: /users/register

HTTP Request Verb: POST  
URL Parameters: None

Required Body:

* email: User's email address
* password: User's password (minimum 8 characters)
* name: User's name

Header Data: Admin's JWT token  
Expected Response: The created user data  
Status Code: 201 Created

Description: This endpoint allows an admin user to register a new user by providing the required user information in the request body. The admin must include a valid JWT token in the request header for authorization.

![Bruno app snapshot](./markdown-images/endpoints/users_register-Success.png)

#### Possible Errors

400 Bad Request: The provided email address already exists.

![Bruno app snapshot](./markdown-images/endpoints/users_register-Email-Exists.png)

400 Bad Request: Email, password, and name are not provided in the request body.

![Bruno app snapshot](./markdown-images/endpoints/users_register-Missing-Data.png)

401 Unauthorized: The JWT token has expired.

![Bruno app snapshot](./markdown-images/endpoints/users_register-Token-Expired.png)

401 Unauthorized: JWT token not provided in the request header.

![Bruno app snapshot](./markdown-images/endpoints/users_register-No-Header.png)

403 Forbidden: The JWT token does not belong to an admin user.

![Bruno app snapshot](./markdown-images/endpoints/users_register-Token-Not-Admin.png)

500 Internal Server Error: A general database error occurs during the creation of the user. This error was not encountered during testing but may potentially occur.

### 3. Route: /recipes

HTTP Request Verb: POST  
URL Parameters: None

Required Body:

* title: Title of the recipe (string)
* description: Description of the recipe (string, optional)
* preparation_time: Preparation time in minutes (integer, optional)
* is_public: Whether the recipe is public (default is true for public)
* category: An array containing cuisine_name field (from categories table)
* ingredients: List of ingredients with name and quantity fields (from ingredients table)
* instructions: List of instructions with step_number and task fields (from instructions table)

Header Data: JWT token of user  
Expected Response: The created recipe data with nested  category, ingredients and instructions data.  
Status Code: 201 Created

Description: This endpoint allows users to create a recipe by providing details such as title, description, preparation time, category, ingredients and instructions. Authentication via a JWT token is required, and only authorized users can perform this action.

![Bruno app snapshot](./markdown-images/endpoints/recipes_create_Success.png)

#### Possible Errors

400 Bad Request: Missing required fields or invalid data format

![Bruno app snapshot](./markdown-images/endpoints/recipes_create_Missing-Field.png)

400 Bad Request: The provided title already exists

![Bruno app snapshot](./markdown-images/endpoints/recipes_create_Title-Exists.png)

401 Unauthorized: JWT token expired or not provided

![Bruno app snapshot](./markdown-images/endpoints/recipes_create-Token-Expired.png)

500 Internal Server Error: General server error during recipe creation

### 4. Route: /users

HTTP Request Verb: GET  
URL Parameters: None  
Required Body: None  
Header Data: Admin's JWT token  
Expected Response: A list of all users' data
Status Code: 200 OK

Description: This endpoint fetches all registered users. This is accessible only by admin users, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/users-get-all_Success.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/users_get-all_Token-Expired.png)

403 Forbidden: JWT token does not belong to an admin.

![RBruno app snapshot](./markdown-images/endpoints/users_get-all_Token-Not-Admin.png)

### 5. Route: /users/{int:user_id}

HTTP Request Verb: GET

URL Parameters:

* user_id (int): The ID of the user to retrieve

Required Body: None  
Header Data: User's or Admin's JWT token  
Expected Response: User data  
Status Code: 200 OK

Description: Retrieves details of a specific user identified by user_id. This endpoint can be accessed by the admin or the user themself, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/users_get-one_OK.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/users_get-one_Token-Expired.png)

403 Forbidden: JWT token does not belong to the admin or the user themself.

![Bruno app snapshot](./markdown-images/endpoints/users_get-one_Unauthorized.png)

404 Not Found: User with the specified user_id does not exist.

![Bruno app snapshot](./markdown-images/endpoints/users_get-one_Not-Found.png)

### 6. Route: /recipes/all

HTTP Request Verb: GET  
URL Parameters: None  
Required Body: None  
Header Data: Admin's JWT token  
Expected Response: List of all recipes (public and private)  
Status Code: 200 OK

Description: Fetches all recipes from the database, including both public and private recipes. This endpoint is accessible only by the admin, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-all_Success.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-all_Token-Expired.png)

403 Forbidden: JWT token does not belong to the admin.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-all_Token-Not-Admin.png)

### 7. Route: /recipes/user

HTTP Request Verb: GET  
URL Parameters: None  
Required Body: None  
Header Data: User's JWT token  
Expected Response: List of all recipes owned by the user  
Status Code: 200 OK

Description: Fetches all recipes owned by a specific user from the database, including both public and private recipes. This endpoint is accessible by the user who created the recipes, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-all-user_Success.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-all-by-user_Token-Expired.png)

### 8. Route: /recipes/user/{user_id}/category/{category_id}

HTTP Request Verb: GET

URL Parameters:  

* user_id: (int) ID of the user whose recipes are to be fetched.
* category_id: (int) ID of the category to filter recipes by.

Required Body: None  
Header Data: User's or Admin's JWT token  
Expected Response: List of recipes owned by the specified user and filtered by the specified category  
Status Code: 200 OK

Description: Retrieves all recipes owned by a specific user and filtered by a specified category from the database. This endpoint is accessible by the admin or the user themselves, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-user-category_Success.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-by-user-category_Token-Expired.png)

403 Forbidden: JWT token does not belong to the admin or the user themselves.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-by-user-category_Unauthorized.png)

404 Not Found: User with the specified user_id not found, or category not found.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-by-user-category_Not-Found.png)

### 9. Route: /recipes/user/random

HTTP Request Verb: GET

URL Parameters: None  
Required Body: None  
Header Data: User's JWT token  
Expected Response: A single recipe randomly selected from the specified user's recipes  
Status Code: 200 OK

Description: Retrieves a randomly selected recipe from the recipes owned by the specified user. This endpoint is accessible by the user who created the recipes, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-random_Success.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-by-user-random_Token-Expired.png)

404 Not Found: User with the specified user_id not found, or no recipes found for the user.

![Bruno app snapshot](./markdown-images/endpoints/.png)

### 10. Route: /recipes/{recipe_id}

HTTP Request Verb: GET

URL Parameters:

recipe_id: (int) ID of the recipe to retrieve.

Required Body: None  
Header Data: User's or Admin's JWT token  
Expected Response: Details of the specified recipe  
Status Code: 200 OK

Description: Retrieves the details of a specific recipe identified by its unique recipe_id. This endpoint is accessible by the admin or the user who created the recipe, authenticated via their JWT token provided in the request header.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-one_Success.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-one_Token-Expired.png)

403 Forbidden: JWT token does not belong to the admin or the user who created the recipe.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-one_Unauthorized.png)

404 Not Found: Recipe with the specified recipe_id not found.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-one_Not-Found.png)

### 11. Route: /recipes/public

HTTP Request Verb: GET  
URL Parameters: None  
Required Body: None  
Header Data: None  
Expected Response: List of all public recipes  
Status Code: 200 OK

Description: Retrieves a list of all recipes marked as public in the database. This endpoint is accessible to anyone without requiring authentication.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-all-public.png)

### 12. Route: /recipes/public/filter

HTTP Request Verb: GET

Query Parameters:

* title: Title or name of the recipe (string)
* prep_time: Maximum preparation time in minutes (integer)
* ingredient_name: Name of the ingredient (string)
* cuisine_name: Name of the cuisine category (string)

Required Body: None  
Header Data: None  
Expected Response: List of filtered public recipes  
Status Code: 200 OK

Description: Retrieves a list of public recipes filtered by title, preparation time, ingredient name, and cuisine name criteria from the database. This endpoint is accessible to anyone without requiring authentication.

Sample URL:

* /recipes/public/filter?title=menudo
* /recipes/public/filter?prep_time=25
* /recipes/public/filter?ingredient_name=bacon
* /recipes/public/filter?cuisine_name=filipino

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-filter_Success.png)

#### Possible Errors

400 Bad Request: Invalid query parameters.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-filter_Invalid-Parameter.png)

400 Bad Request: Invalid query type.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-filter_Invalid-Value.png)

404 Not Found: The recipe with the specified value of given parameter does not exists.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-filter_Not-Found.png)

### 13. Route: /recipes/public/random

HTTP Request Verb: GET  
URL Parameters: None  
Required Body: None  
Header Data: None  
Expected Response: A randomly selected public recipe  
Status Code: 200 OK

Description: Retrieves a randomly selected recipe from the public recipes in the database. This endpoint does not require authentication and can be accessed by anyone.

![Bruno app snapshot](./markdown-images/endpoints/recipes_get-public-random_Success.png)

#### Possible Errors

404 Not Found: No public recipes are available.

![Bruno app snapshot](./markdown-images/endpoints/.png)

### 14. Route: /categories

HTTP Request Verb: GET  
URL Parameters: None  
Required Body: None  
Header Data: None  
Expected Response: A list of all categories  
Status Code: 200 OK

Description: Retrieves all categories from the database. This endpoint does not require authentication and can be accessed by anyone.

![Bruno app snapshot](./markdown-images/endpoints/categories_get-all_Success.png)

#### Possible Errors

404 Not Found: No categories are available.

![Bruno app snapshot](./markdown-images/endpoints/categories_get-all_Not-Found.png)

### 15. Route: /categories/{category_id}

HTTP Request Verb: GET

URL Parameters:

* category_id: (int) ID of the category to retrieve.

Required Body: None  
Header Data: None  
Expected Response: The details of the specified category  
Status Code: 200 OK

Description: Retrieves the details of a specific category by its ID from the database. This endpoint does not require authentication and can be accessed by anyone.

![Bruno app snapshot](./markdown-images/endpoints/categories_get-one_Success.png)

#### Possible Errors

404 Not Found: Category with the specified ID not found.

![Bruno app snapshot](./markdown-images/endpoints/categories_get-one_Not-Found.png)

### 16. Route: /users/{user_id}

HTTP Request Verb: PUT, PATCH

URL Parameters:

* user_id: (int) ID of the user to update.

Required Body:

* email: User's new email address (string)
* password: User's new password (string)
* name: User's new name (string, optional)
* is_admin: Whether the user is an admin (boolean, default False; only admin can update this field)

Header Data: JWT token of user or admin  
Expected Response: The updated user data  
Status Code: 200 OK

Description: Updates the details of a specific user by their ID. This endpoint is accessible by the admin or the user themselves, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/users_update-Success.png)

#### Possible Errors

400 Bad Request: Missing required fields or invalid data format

![Bruno app snapshot](./markdown-images/endpoints/users_update-Missing-Field.png)

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/users_update-Token-Expired.png)

403 Forbidden: JWT token does not belong to the admin or the user themselves.

![Bruno app snapshot](./markdown-images/endpoints/users_update-Unauthorized.png)

404 Not Found: User with the specified ID not found.

![Bruno app snapshot](./markdown-images/endpoints/users_update-Not-found.png)

500 Internal Server Error: General server error during user update.

### 17. Route: /recipes/{recipe_id}

HTTP Request Verb: PUT, PATCH

URL Parameters:

* recipe_id: (int) ID of the recipe to update.

Required Body:

* title: New title of the recipe (string, optional)
* description: New description of the recipe (string, optional)
* preparation_time: New preparation time in minutes (integer, optional)
* is_public: Whether the recipe is public (boolean, optional)
* cuisine_name: New cuisine_name of the recipe (string, optional)
* ingredients: List of new ingredients with name and quantity fields (array, optional)
* instructions: List of new instructions with step_number and task fields (array, optional)

Header Data: JWT token of user or admin  
Expected Response: The updated recipe data  
Status Code: 200 OK

Description: Updates the details of a specific recipe by its ID. This endpoint is accessible by the admin or the user who created the recipe, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/recipes_update-Success.png)

#### Possible Errors

400 Bad Request: Missing required fields, invalid data format or title already exists

![Bruno app snapshot](./markdown-images/endpoints/recipes_update-Recipe-Exists.png)

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/recipes_update-Token-Expired.png)

403 Forbidden: JWT token does not belong to the admin or the user themselves.

![Bruno app snapshot](./markdown-images/endpoints/recipes_update-Unauthorized.png)

404 Not Found: Recipe with the specified ID not found.

![Bruno app snapshot](./markdown-images/endpoints/recipes_update-Not-Found.png)

500 Internal Server Error: General server error during recipe update.

### 18. Route: /users/{user_id}

HTTP Request Verb: DELETE

URL Parameters:

* user_id: (int) ID of the user to delete.

Required Body: None  
Header Data: JWT token of user or admin  
Expected Response: Empty response indicating successful deletion  
Status Code: 200 OK

Description: Deletes a user by their ID. This endpoint is accessible by the admin or the user themselves, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/users_delete_Success.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/users_delete_Token-Expired.png)

403 Forbidden: JWT token does not belong to the admin or the user themselves.

![Bruno app snapshot](./markdown-images/endpoints/users_delete_Unauthorized.png)

404 Not Found: User with the specified ID not found.

![Bruno app snapshot](./markdown-images/endpoints/users_delete_Not-Found.png)

500 Internal Server Error: General server error during user deletion.

### 19. Route: /recipes/{recipe_id}

HTTP Request Verb: DELETE

URL Parameters:

* recipe_id (int): The ID of the recipe to be deleted

Required Body: None  
Header Data: JWT token of user or admin  
Expected Response: Empty response indicating successful deletion  
Status Code: 200 OK

Description: Deletes a specific recipe from the database. Accessible by the admin or the user who created the recipe, who must provide their JWT token in the request header for authentication.

![Bruno app snapshot](./markdown-images/endpoints/recipes_delete-Success.png)

#### Possible Errors

401 Unauthorized: JWT token not provided or expired.

![Bruno app snapshot](./markdown-images/endpoints/recipes_delete-Token-Expired.png)

403 Forbidden: JWT token does not belong to the admin or the user who created the recipe.

![Bruno app snapshot](./markdown-images/endpoints/recipes_delete-Unauthorized.png)

404 Not Found: Recipe with the specified recipe_id not found.

![Bruno app snapshot](./markdown-images/endpoints/recipes_delete-Not-Found.png)

500 Internal Server Error: General server error during user deletion.

### Reference List

Laura, 2010, *How to Organize Recipes You Find Online*, viewed 27 June 2024, https://orgjunkie.com/2010/07/how-to-organize-recipes-you-find-online.html