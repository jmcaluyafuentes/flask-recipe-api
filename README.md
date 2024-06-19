# API Web Server

Term 2, Assignment 2  
Diploma of IT - Web Development  
Coder Academy

## Purpose

This API web server is an assignment for Term 2 in the Coder Academy Diploma of IT. It aims to provide students with practical experience in developing a fully functional web application backend using modern web development technologies and best practices. My project involves creating a recipe management system that allows users to manage and discover recipes, leveraging Flask for the web framework and PostgreSQL for the relational database management system.

## Description

This API web server, named Flask Recipe API, is designed to manage a recipe application where users can create, save, and browse recipes. Built using Flask, a lightweight Python web framework, this server provides a robust backend for handling user authentication, recipe management, and data persistence using a PostgreSQL database.

1. User Management

    - Admin users can add new users to the system.
    - User authentication and authorization to ensure secure access to the API endpoints.

2. Recipe Management

    - Users can create, update, and delete their own recipes.
    - Recipes can be marked as public or private.
    - Admins have the ability to delete any public recipe.

3. Recipe Discovery

    - Users can browse public recipes.
    - Users can save public recipes to their personal accounts for easy access.
    - Users can filter recipes based on various criteria like cuisine, preparation time, etc.
    - Users can get a random recipe suggestion if unsure of what to cook.

4. Recipe Details

    - Recipes consist of step-by-step instructions that are ordered to ensure clarity.
    - Users can leave personal notes on saved recipes for future reference.

## Github Repository

https://github.com/jmcaluyafuentes/flask-recipe-api

## Requirements

### R1: Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

### R2: Describe the way tasks are allocated and tracked in your project.

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