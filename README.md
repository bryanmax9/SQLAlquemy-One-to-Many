# Section Model for Course Database

This project implements a Section model for a Course database using PostgreSQL and SQLAlchemy. The code was initially provided by the instructor of a Database Fundamentals class, and it already included the Department and Course tables.

However, the Section model was missing, so our group had to create it by adding a Foreign Primary Key from the Course table that would link each Section to a specific Course. To achieve this, we established a one-to-many relationship between the Course and Section tables.

Once the Section model was implemented, we also created a set of functions that allow users to interact with the database. These functions include:

- `add_section`: add a new Section to the database
- `delete_section`: delete an existing Section from the database
- `select_section`: select a specific Section from the database based on its id
- `select_all_sections`: select all Sections from the database

By using these functions, users can easily manage the Sections in the Course database and retrieve the data they need.

![Department Table](https://i.imgur.com/AgmOwjr.png)
![Course Table](https://i.imgur.com/jNIKzRY.png)
![Section Table](https://i.imgur.com/MbdG1Jy.png)

## Getting Started

To use this code, you will need to have PostgreSQL installed on your machine and create a database called "course_db". You will also need to install the psycopg2 and SQLAlchemy libraries by running `pip install psycopg2 sqlalchemy` in your command prompt.

Once you have these prerequisites, you can clone this repository and run the `main.py` file to start using the Section model and its functions.

## Contributors

This project was created by Bryan tineo and Zavier Carr for a Database Fundamentals class. Feel free to use it and modify it as needed for your own projects.

If you have any questions or suggestions, you can contact us at [Your Email Address].
