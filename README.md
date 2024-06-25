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
    - User authentication and authorization to ensure secure access to the API endpoints.

2. Recipe Management

    - Users can create, update, and delete their own recipes.
    - Recipes can be marked as public or private.
    - Admins have the ability to delete any public recipe (e.g., if it did not comply with the guidelines).

3. Recipe Discovery

    - Users can browse public recipes.
    - Users can save public recipes to their personal accounts for easy access.
    - Users can filter recipes based on various criteria like cuisine, preparation time, etc.
    - Users can get a random recipe suggestion if unsure of what to cook.

4. Recipe Details

    - Recipes consist of step-by-step instructions that are ordered to ensure clarity.
    - Users can leave personal notes on saved recipes for future reference.

## Requirements

### R1: Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

In our busy lives, many people, including my family, often struggle in planning meals planning and managing recipes. One of the problems that this app solves is the lack of organization in managing recipes. The abundance of recipes from diverse sources and blogs on the internet often overwhelms and confuses us when trying to find cooking ideas. The app offers user accounts, allowing individuals to consolidate and manage their recipes in a single, centralized location. This feature enables users to conveniently access their preferred recipes whenever they need them.

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