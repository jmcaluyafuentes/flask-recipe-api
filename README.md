# API Web Server

Term 2, Assignment 2  
Diploma of IT - Web Development  
Coder Academy

## Table of Contents

1. [Deployed API](#deployed-api)
2. [Purpose of API](#purpose)
3. [Installation and Set Up Instructions](#installation-and-set-up-instructions)
4. [Requirements](#requirements)  
    4.1 [Problem statement](#r1-explain-the-problem-that-this-app-will-solve-and-explain-how-this-app-solves-or-addresses-the-problem)  
    4.2 [Project management](#r2-describe-the-way-tasks-are-allocated-and-tracked-in-your-project)  
    4.3 [Packages and dependencies](#r3-list-and-explain-the-third-party-services-packages-and-dependencies-used-in-this-app)  
    4.4 [Database benefits and drawbacks](#r4-explain-the-benefits-and-drawbacks-of-this-apps-underlying-database-system)  
    4.5 [Functionality of ORM in this app](#r5-explain-the-features-purpose-and-functionalities-of-the-object-relational-mapping-system-orm-used-in-this-app)  
    4.6 [Entity Relationship Diagram](#r6-design-an-entity-relationship-diagram-erd-for-this-apps-database-and-explain-how-the-relations-between-the-diagrammed-models-will-aid-the-database-design)  
    4.7 [Models and their relationships](#r7-explain-the-implemented-models-and-their-relationships-including-how-the-relationships-aid-the-database-implementation)  
    4.8 [Endpoints](#r8-explain-how-to-use-this-applications-api-endpoints-each-endpoint-should-be-explained-including-the-following-data-for-each-endpoint)










## Deployed API

You can access the deployed API at: [https://flask-recipe-api.onrender.com/](https://flask-recipe-api.onrender.com/)

## Purpose

This API web server is an assignment for Term 2 in the Coder Academy Diploma of IT. It aims to provide students with practical experience in developing a fully functional API web server using modern web development technologies and best practices. My project involves creating a recipe management system that allows users to manage and discover recipes, leveraging Flask for the web framework and PostgreSQL for the relational database management system.

## Installation and Set Up Instructions

### Prerequisites

1. Windows Subsystem for Linux (WSL)

    Make sure you have WSL installed and set up on your Windows machine.

2. Python and pip

    Python 3.7 or higher is required. Check if Python is installed:

    ```
    python3 --version
    ```

    Install Python if not already installed:

    ```
    sudo apt update  
    sudo apt install python3 python3-pip
    ```

3. PostgreSQL

    Install PostgreSQL database server:

    ```
    sudo apt update
    sudo apt install postgresql
    ```

    Start PostgreSQL service:

    ```
    sudo service postgresql start
    ```

### Clone Repository

1. Clone the Recipe API repository from GitHub

    ```
    git clone https://github.com/jmcaluyafuentes/flask-recipe-api
    cd recipe-api
    ```

### Set Up Virtual Environment

1. Create a virtual environment

    ```
    python3 -m venv venv
    ```

2. Activate the virtual environment

    ```
    source venv/bin/activate
    ```

### Install Dependencies

1. Install required Python packages

    ```
    pip install -r requirements.txt
    ```

### Set Up Environment Variables

1. Create a .env file in the root directory of the project

    ```
    touch .env
    ```

2. Add the following environment variables to .env file

    ```
    JWT_KEY='your_secret_key'
    DB_URL='postgresql+psycopg2://username:password@localhost:5432/databasename
    # Replace `username`, `password`, and `databasename` with your
      PostgreSQL credentials and database name
    ```

### Database Setup

1. Create the database and populate initial data

    ```
    flask db create
    ```

### Run the Application

1. Start the Flask development server

    ```
    flask run
    ```

2. Access the API in your browser at http://localhost:5000.

[Back to Top](#)

## Requirements

### R1: Explain the problem that this app will solve and explain how this app solves or addresses the problem

In our busy lives, many people, including my family, often struggle in planning meals and managing recipes. One of the problems that this app solves is the lack of organization in managing recipes. The abundance of recipes from diverse sources and blogs on the internet often overwhelms and presents challenges in organizing them (Laura 2010). The app offers user accounts, allowing individuals to consolidate and manage their recipes in a single, centralized location. This feature enables users to conveniently access their preferred recipes whenever they need them.

Meal planning is also a challenge that this app aims to solve. Deciding what to cook, especially when busy, can be quite time-consuming. To solve this problem, the app includes a feature that enables users to randomly select a recipe from their collection or from publicly available recipes. This simplifies the decision-making process, making it easier for users to decide on their next meal quickly. Additionally, users have the option to save public recipes to their personal accounts, allowing them to build a curated collection of meals that align with their preferences and support their meal planning efforts.

Customized searching is helpful for users with specific dietary preferences or time constraints. This app has filtering options that allow users to search for recipes based on criteria such as type of cuisine and preparation time. This feature helps users find recipes that match their specific needs and preferences.

To maintain the integrity of the platform, this app includes several administrative features. Admins can add users to the platform to ensure a controlled and secure user base. The admins have the authority to delete public recipes that do not comply with the guidelines. Users also have control over their accounts, with the ability to create, update, and delete their own recipes.

[Back to Top](#)

### R2: Describe the way tasks are allocated and tracked in your project

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

In addition to task management in Trello, we held daily standups on Discord. These standups were beneficial as it allowed me to evaluate my progress by answering key questions. It helped me process my thoughts and assess my remaining tasks to determine if I was on track, if there were other tasks I needed to add, or if I needed to adjust my due dates. Standups provided a daily reminder to keep me focused on my goals. Here are sample standups:

![Daily standups on 24th June](./markdown-images/standups-1.png)

![Daily standups on 25th June](./markdown-images/standups-2.png)

![Daily standups on 26th June](./markdown-images/standups-3.png)

I also used Git for source control and regularly pushed my changes to a GitHub repository. This allowed me to track the changes and their descriptions effectively. In case of errors while coding, I could revert to a previous version, which was particularly beneficial given the modular nature of my project. Additionally, the GitHub repository served as a backup of my codebase and I could retrieve it in case of issues with my local copies such as corruption or loss. Here is a sample snapshot of my commits in GitHub:

![Github regular commits](./markdown-images/github-1.png)

![Github regular commits](./markdown-images/github-2.png)

[Back to Top](#)

### R3: List and explain the third-party services, packages and dependencies used in this app

* Flask - it is a lightweight web application framework in Python. It provides tools, libraries, and patterns to build web applications. Flask provides the core framework for routing, request handling, and response generation in your application.

* Flask-SQLAlchemy - it integrates SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapping (ORM) library, with Flask. SQLAlchemy simplifies database operations by allowing developers to work with database models and queries using Python objects. Flask-SQLAlchemy extends Flask's capabilities by providing ORM features, schema creation, and migration tools.

* Psycopg2-binary - it is a PostgreSQL adapter for Python. It allows Flask applications to interact with PostgreSQL databases efficiently. Psycopg2-binary enables executing SQL queries, managing transactions, and handling database connections seamlessly within Flask-SQLAlchemy.

* Python-dotenv - it is a Python library that manages environment variables from a .env file. It loads environment variables into the application's environment, making it easy to configure Flask applications across different environments (development, testing, production) without exposing sensitive information in version-controlled files.

* Flask-marshmallow - it integrates the Marshmallow library with Flask. Marshmallow is a powerful library for object serialization and deserialization, commonly used in Flask applications for data validation, schema definition, and converting complex Python objects to JSON-compatible formats. Flask-marshmallow simplifies integrating Marshmallow schemas with Flask routes, enabling clean API responses and request handling.

* Marshmallow - it is the core library for object serialization and deserialization in Python. It is used alongside flask-marshmallow for defining and validating API schemas, ensuring that the data exchanged between the client and server conforms to expected formats. 

* Flask-JWT-Extended - it is an extension that adds support for JSON Web Tokens (JWT) to Flask for authentication. It simplifies handling JWTs for protecting routes and controlling user access. It allows a secure access to protected routes based on token validation.

* Bcrypt - it is a password hashing library that securely stores passwords. It employs the bcrypt hashing algorithm, which includes salting and multiple hashing rounds to protect against brute-force attacks. In the Recipe API, bcrypt is crucial for securely storing user passwords by hashing them before saving them to the database. It ensures that even if the database is compromised, passwords remain protected.

* Sqlalchemy.orm - the mapped, mapped_column, relationship are SQLAlchemy ORM components used to define and manage database relationships. Mapped and mapped_column help define the columns of the database models, while relationship establishes relationships between different models, such as one-to-many or many-to-many associations.

* Sqlalchemy.exc - it utilizes the IntegrityError and SQLAlchemyError exceptions used for error handling. IntegrityError is raised when a database integrity constraint (such as a unique constraint) is violated. SQLAlchemyError is a base class for all SQLAlchemy-specific exceptions.

* Datetime - This module provides date-related functionalities in Python. It is used in the Recipe API to manage and manipulate date values, such as storing the creation date of recipes.

* Typing - the List and Optional are type hinting tools from Python's typing module. List specifies that a variable is a list of a specific type, and Optional indicates that a variable can be of a specified type or None.

* Random - This module implements pseudo-random number generators for various distributions. It is used in the Recipe API to generate random recipe.

[Back to Top](#)

### R4: Explain the benefits and drawbacks of this app’s underlying database system

The Recipe API uses PostgreSQL as its database system and it is interface with SQLAlchemy and psycopg2-binary. Below are the benefits and drawbacks of using PostgreSQL for this application:

#### Benefits of PostgreSQL

* Reliability and ACID Compliance - PostgreSQL is known for its robustness and adherence to ACID (Atomicity, Consistency, Isolation, Durability) principles. This ensures data integrity and reliability, which is crucial for applications managing sensitive data, such as user information and recipes.

* Advanced SQL Features - PostgreSQL supports a wide range of advanced SQL features like window functions, common table expressions (CTEs), and full-text search. These features allow for complex queries and data manipulations that enhance the application's capability to handle sophisticated data operations.

* Extensibility- PostgreSQL is highly extensible that allow users to define custom functions, data types, and operators. This flexibility can be leveraged to implement specific application logic directly within the database to improve the performance and maintainability.

* Strong Community and Support - PostgreSQL has a large and active community that provides extensive documentation, plugins, and support. This community-driven development ensures continuous improvements, timely bug fixes, and security patches.

* Security Features - PostgreSQL offers robust security features that includes user authentication, role-based access control, and encryption. These features are essential for protecting sensitive user data and ensuring that only authorized users can access certain parts of the application.

#### Drawbacks of PostgreSQL

* Complexity - PostgreSQL's rich feature set and advanced capabilities can introduce complexity, particularly for new users or those migrating from simpler database systems. Learning to utilize all of its features effectively can require a steep learning curve.

* Performance Overhead - while PostgreSQL is highly performant, certain features, such as full-text search or complex query operations, can introduce performance overhead. Proper indexing and query optimization are necessary to maintain high performance, which can add to development and maintenance efforts.

* Resource Intensive - PostgreSQL can be resource-intensive in terms of memory and CPU usage, especially under heavy loads or when performing complex operations. Ensuring the underlying infrastructure can support PostgreSQL's requirements is important for maintaining performance and stability.

* Configuration Complexity - Optimizing PostgreSQL for specific use cases often requires fine-tuning various configuration parameters. This process can be complex and requires a deep understanding of the database's internals and the application's workload.

[Back to Top](#)

### R5: Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.

In the Recipe API application, SQLAlchemy is used as the Object-Relational Mapping (ORM) system.

#### 1. Model Definition and Schema Generation

Feature: SQLAlchemy ORM allows us to define database schemas using Python classes. These classes represent tables in the database, with attributes corresponding to columns.

Functionality: Automatically generate the schema from the model definitions.

Example:

![Models](./markdown-images/images-models/model-category.png)

![Models](./markdown-images/images-models/create-table.png)

In this example, the Category class defines a table named categories with columns category_id and cuisine_name. The db.create_all method generates the corresponding table in the postgres database.

#### 2. Relationships and Foreign Keys

Feature: SQLAlchemy ORM supports defining relationships between tables using foreign keys. This includes one-to-one, one-to-many, and many-to-many relationships.

Functionality: Establish and navigate relationships between models.

![Models](./markdown-images/images-models/model-category.png)

![Models](./markdown-images/images-models/category-recipe.png)

In this example, a one-to-many relationship is established between Category and Recipe. Each Recipe belongs to one Category, and each Category can have multiple Recipe objects.

#### 3. Data Validation and Constraints

Feature: SQLAlchemy supports various data types and constraints, ensuring data integrity at the model level.

Functionality: Enforce data types and constraints in the database schema.

![Models](./markdown-images/images-models/model-instruction.png)

In this example, the Instruction model includes a check constraint to ensure that the step_number must be an integer. If the provided value is not an integer, an error will be raised.

#### 4. Session Management

Feature: SQLAlchemy ORM uses a session to manage database operations, handling transactions, and ensuring data consistency.

Functionality: Perform database operations within a managed context.

![Models](./markdown-images/images-models/query-recipes-delete.png)

In this example, the session `db.session.delete(recipe)` is used to delete a recipe in the database. If an error occurs, the session is rolled back using `db.session.rollback` to maintain data consistency.

#### 5. Querying the Database

Feature: SQLAlchemy ORM provides a high-level API for building and executing queries. This includes support for filtering, ordering, and joining tables.

Functionality: Perform complex queries without writing raw SQL.

![Models](./markdown-images/images-models/query-recipes-user.png)

In this example, a query is performed to retrieve the recipe by the user's ID. The `db.get_or_404(Recipe, recipe_id)` will retrieve the recipe with the specified ID or it will return a 404 error if the recipe is not found.

[Back to Top](#)

### R6: Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.

#### This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.

This process begins with identifying the entities and their attributes, followed by applying normalization to organize the data to eliminate redundancy and improve data integrity. It involves decomposing a set of data into multiple related tables based on rules that ensure the data is logically stored and reduces redundancy.

Once the data is normalized, the ERD is created. The ERD is a visual representation of the entities (tables) and the relationships between them. It shows how the data will be structured in the database, including primary keys, foreign keys, and other constraints that ensure data integrity. The ERD helps to visualize the logical structure of the database and how different tables connect with each other.

### Step 1 - Identify the entities and their attributes

Since the primary purpose of the database is to manage recipes, we begin by identifying the key entities and their attributes.

1. Users

    Users are individuals who create, manage, and access recipes. Each user has the following attributes.

    * name: The name of the user
    * email: The email address of the user
    * password: The password used for login

2. Recipes

    Recipes are the main content of the application, created and managed by users. Initially, in a non-normalized form, each recipe might include the following attributes.

    * title: The title or name of the recipe
    * description: A description of the recipe
    * ingredients: The ingredients required for the recipe
    * instructions: The step-by-step instructions for preparing the recipe
    * preparation time: The preparation time in minutes
    * category: The category to which the recipe belongs
    * user: The user who created the recipe
    * date created: The date when the recipe was created
    * is_public: A boolean indicating if the recipe is public or private

### Step 2 - Normalization Process

Normalization is a systematic approach to organize data in a database to reduce redundancy and improve data integrity. The normalization process involves several steps as follows.

2.1 Non-Normalized Data

Initially, all data might be stored in a single table, leading to redundancy and potential anomalies such as duplication.

Each entity is represented by a table and the entity's attributes are represented in columns. The instance of an entity is represented in rows.

Users table:

![ERD design](./markdown-images/erd/users-0.png)

In my database design, the name can only be a first name or nickname which does not matter if the user put any name. What matters most is the email address which must be unique for each user since this identifies them when logging in to the platform. The password is required for authentication while the is_admin flag determines whether the user has an admin privileges or not.

Recipes table:

![ERD design](./markdown-images/erd/0-recipes.png)

The recipes table has several redundancy. There are multiple values in ingredients and instructions columns.

2.2 First Normal Form (1NF)

The rules of 1NF are the following:

* Column names must be unique
* Order of records does not matter
* Records of on column must be of same type
* Must have atomic values in columns (single values)

Users table: No change required since it already meets 1NF criteria.

Recipes table:

![ERD design](./markdown-images/erd/1-recipes.png)

By applying the 1NF rules, the ingredients are separated into two columns for the ingredient name and quantity. The instructions are also separated into step number and the instruction. The result has many rows but it more clear and it will be reduce the chances of mistake (anomalies) when updating the data.

2.3 Second Normal Form (2NF)

The rules of 2NF are the following:

* Table is in 1NF
* All columns depend on the table's primary key

Users table: No change

The recipes table will be divided into recipes, ingredients and instructions tables so that each table has a single purpose.

Recipes table:

![ERD design](./markdown-images/erd/2-recipes.png)

Each column will now depend on the the primary key recipe_id. Each recipe will be linked to a user on user_id.

Ingredients table:

![ERD design](./markdown-images/erd/2-ingredients.png)

Each column will depend on the ingredient_id. All rows with the same recipe_id belongs to that recipe.

Instructions table:

![ERD design](./markdown-images/erd/2-instructions.png)

Each column will depend on the instruction_id. All rows with the same recipe_id belongs to that recipe.

2.4 Third Normal Form (3NF)

Rules:

The rules of 3NF are the following:

* Table is in 2NF
* Contains only columns that are non-transitively dependent on the primary key.

Users table: No change

The category in recipes table does not uniquely identifies a recipe since multiple recipes can share the same category. So we separate the recipes and categories tables.

Recipes table:

![ERD design](./markdown-images/erd/3-recipes.png)

Categories table:

![ERD design](./markdown-images/erd/3-categories.png)

Ingredients table: No change

Instructions table: No change

### Step 3 - Entity Relationship Diagram (ERD)

#### List of tables and attributes

Some attribute's names are changed for clarity.

Users:

* user_id (primary key)
* email
* password
* name
* is_admin

Categoories:

* category_id (primary key)
* cuisine_name

Recipes:

* recipe_id (primary key)
* title
* description
* preparation_time
* is_public
* date_created
* user_id (foreign key)
* category_id (foreign key)

Ingredients:

* ingredient_id (primary key)
* name
* quantity
* recipe_id (foreign key)

Instructions:

* instruction_id (primary key)
* step_number
* task
* recipe_id (foreign key)

#### Relationships between tables

* Users to recipes table: It has a one-to-many relationship, indicating that a user can create multiple recipes.

* Categories to recipes table: It has a one-to-many relationship, indicating that a category can have many recipes.

* Recipes to ingredients table: It has a one-to-many relationship, indicating that a recipe can have many ingredients.

* Recipes to instructions table: It has a one-to-many relationship, indicating that a recipe can have many instructions.

#### ERD Diagram

![ERD design](./markdown-images/erd/ERD-recipe-api.png)

[Back to Top](#)

### R7: Explain the implemented models and their relationships, including how the relationships aid the database implementation.

#### This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.

During the project development phase, the implemented models and their relationships play a crucial role in defining the structure of the database and ensuring efficient data management. Here’s an overview of the models used in the application and their relationships, leveraging SQLAlchemy for ORM and Marshmallow for serialization.

#### 1. User Model

The User model represents users who interact with the application, including creating and managing recipes.

![Models](./markdown-images/images-models/model-user.png)

* The \__tablename__ specifies the name of the table in the database where instances of this model will be stored ('users').

* The user_id, email, password, name and is_admin are attributes (columns) of the User model mapped to corresponding fields in the database table. Each attribute represents a column with its respective data type (String, Boolean, etc.).

* The recipes is a relationship defined in the User model using SQLAlchemy's relationship function. The Mapped[List['Recipe']] specifies the type of data this relationship will return. It indicates that this relationship will return a list (List) of Recipe objects. The back_populates parameter ensures that changes made to one side of the relationship (either User or Recipe) are automatically reflected on the other side.

#### Category Model

The Category model represents the structure of the categories table in the database.

![Models](./markdown-images/images-models/model-category.png)

* The \__tablename__ specifies the name of the table in the database where instances of this model will be stored ('categories').

* The category_id and cuisine_name are attributes (columns) of the Category model mapped to corresponding fields in the database table. category_id serves as the primary key, ensuring each category has a unique identifier.

* The recipes is a relationship defined in the Category model using SQLAlchemy's relationship function. The Mapped[List['Recipe']] specifies the type of data this relationship will return. The back_populates parameter ensures that changes made to one side of the relationship (either Category or Recipe) are automatically reflected on the other side.

#### Recipe Model

The Recipe model represents the structure of the recipes table in the database.

![Models](./markdown-images/images-models/models-recipe.png)

* The \__tablename__ specifies the name of the table in the database where instances of this model will be stored ('recipes').

* The recipe_id, title, description, is_public, preparation_time and date_created are attributes (columns) of the Recipe model mapped to corresponding fields in the database table.

* The 'user_id' is defined as a foreign key (ForeignKey('users.user_id')) linking to the user_id column in the users table. The 'user' establishes a relationship between the Recipe and User models using SQLAlchemy's relationship function. This represents a one-to-many relationship where each recipe is associated with one user (author).

* The 'category_id' is defined as a foreign key (ForeignKey('categories.category_id')) linking to the category_id column in the categories table. The 'category' establishes a relationship between the Recipe and Category models using SQLAlchemy's relationship function. This represents a many-to-one relationship where multiple recipes can belong to the same category.

* The Recipe model has one-to-many relationships with the Ingredient and Instruction models respectively. Each recipe can have multiple ingredients and instructions associated with it. The "cascade='all, delete-orphan'" option ensures that when a recipe is deleted, all associated ingredients and instructions are also deleted (delete-orphan), maintaining referential integrity.

#### Ingredient Model

The Ingredient model represents the structure of the ingredients table in the database.

![Models](./markdown-images/images-models/model-ingredient.png)

* \__tablename__ specifies the name of the table in the database where instances of this model will be stored ('ingredients').

* The ingredient_id, name and quantity are attributes (columns) of the Ingredient model mapped to corresponding fields in the database table.

* The 'recipe_id' is defined as a foreign key (ForeignKey('recipes.recipe_id')) linking to the recipe_id column in the recipes table. The "relationship(back_populates='ingredients')" establishes a relationship between the Ingredient and Recipe models using SQLAlchemy's relationship function. This defines a many-to-one relationship where multiple ingredients can belong to the same recipe (Recipe model).

#### Instruction Model

The Instruction model represents the structure of the instructions table in the database.

![Models](./markdown-images/images-models/model-instruction.png)

* \__tablename__ specifies the name of the table in the database where instances of this model will be stored ('instructions').

* The instruction_id, step_number and task are attributes (columns) of the Instruction model mapped to corresponding fields in the database table.

* The 'recipe_id' is defined as a foreign key (ForeignKey('recipes.recipe_id')) linking to the recipe_id column in the recipes table. The "relationship(back_populates='instructions')" establishes a relationship between the Instruction and Recipe models using SQLAlchemy's relationship function. This defines a many-to-one relationship where multiple instructions can belong to the same recipe (Recipe model).

#### Examples of querying data using SQLAlchemy relationships

#### 1. Querying user and their recipes

To retrieve a user and all their associated recipes, we can utilize SQLAlchemy's relationship attribute defined in the User model.

![Models](./markdown-images/images-models/query-recipes-user.png)

* `@recipes_bp.route("/<int:recipe_id>` this decorator defines a route for accessing a specific recipe based on its recipe_id. The `<int:recipe_id>` part specifies that recipe_id will be an integer parameter in the URL path.

* The `@jwt_required()` is a decorator ensuring that JWT (JSON Web Token) authentication is required to access this route. The presence of a valid JWT in the request headers is checked before the route function is executed.

* From the statement `recipe = db.get_or_404(Recipe, recipe_id)`, the `db.get_or_404()` retrieves a recipe record from the database based on Recipe model and recipe_id. If no recipe with the specified ID is found, it returns a 404 HTTP error.

* The `current_user_id = get_jwt_identity()` retrieves the current user's ID from the JWT payload.

* The `if current_user_id != recipe.user_id and not current_user_is_admin()` will checks if the current user is either the author of the recipe or an admin. If not authorized, returns a 403 Forbidden error.

* Finally, the `return RecipeSchema().dump(recipe)` serializes the recipe object into a JSON representation. This ensures that only relevant fields defined in RecipeSchema are returned in the response.

#### 2. Deleting a recipe and its associated ingredients and instructions

This Flask route handler (delete_recipe) is designed to delete a recipe from the database. It includes authorization checks to ensure that only the author of the recipe or an admin can perform the deletion.

![Models](./markdown-images/images-models/query-recipes-delete.png)

* `@recipes_bp.route("/<int:recipe_id>, methods=["DELETE"])` defines a route that accepts DELETE requests at `/recipes/<recipe_id>`. The `<int:recipe_id>` part in the route URL specifies that recipe_id is expected as an integer parameter.

* The `@jwt_required()` is a decorator that ensures the request includes a valid JWT token. This means only authenticated users can access this endpoint.

* The `def delete_recipe(recipe_id)` defines the function delete_recipe which takes recipe_id as a parameter, representing the ID of the recipe to be deleted.

* The `try` begins a try block to handle potential errors during the deletion process.

* The `recipe = Recipe.query.filter_by(recipe_id=recipe_id).one()` uses SQLAlchemy's query method to fetch a recipe from the database based on recipe_id. The `.one()` is used assuming that exactly one result is expected; it raises NoResultFound otherwise.

* The `current_user_id = get_jwt_identity()` retrieves the current user's ID from the JWT token. The authorization check verifies if the current user is either the author of the recipe (current_user_id == recipe.user_id) or an admin (current_user_is_admin() function).

* The `db.session.delete(recipe)` marks the recipe object for deletion within the current session.

* The `db.session.commit()` commits the transaction to permanently delete the recipe from the database. Upon successful deletion, returns an empty dictionary {} with an HTTP 200 OK status code. If unauthorized, returns a 403 Forbidden error with an error message.

[Back to Top](#)

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

![Bruno app snapshot](./markdown-images/endpoints/recipes_user-random.png)

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

![Bruno app snapshot](./markdown-images/endpoints/recipes_public-random.png)

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

[Back to Top](#)

### Reference List

Laura, 2010, *How to Organize Recipes You Find Online*, viewed 27 June 2024, https://orgjunkie.com/2010/07/how-to-organize-recipes-you-find-online.html