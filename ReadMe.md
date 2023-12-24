# Case Study at MEINSTADT

## Introduction
Create a python script which downloads as much drinks as possible from following
page: https://www.thecocktaildb.com/api.php

Create a relational database in sqlite for the downloaded data, under the assumption
that your database could grow to over 10 million datasets.

Extend your script (from point 1) to insert the data in your database. Please insert
just data which has German instructions.

Which are the SQL queries for following questions:
1. Which alcoholic drinks can be mixed with lemon and whiskey?
2. Which drink(s) can be mixed with just 15g of Sambuca?
3. Which drink has the most ingredients?

## My Approach
I've implemented a simple pipeline for handling drinks data. The process begins with the management of the database schema, ensuring any existing schema is dropped before setting up a new one based on SQL queries.

Upon schema setup, the pipeline proceeds to extract drinks data from a Cocktail API endpoint. The extraction is performed systematically, fetching data based on each letter of the alphabet for a thorough dataset, and extracted data for each letter undergoes specific transformations, such as converting measures to grams. This transformed data is then loaded into corresponding database tables.

During the loading phase, duplicate handling is managed using the 'ON CONFLICT' clause. There are some drinks which contains duplicated ingredients, they are not taken into account to reduce data redundacy. The pipeline takes into account the efficiency of the loading process, working in batches to ensure smooth execution.

Following the successful loading of data, the pipeline concludes with the execution of analytical queries. These queries are designed based on above asked questions to extract meaningful insights from the loaded data.

Note: The values defined in the dictionary for the measure conversion to grams may not be precisely accurate, the primary purpose is to show the approach to come up with a solution for the problem.

## Technical Setup
To run the code you need to have Python 3.6+ installed.
Please install all the required libraries via: pip install -r requirements.txt
You can execute the code via this command: python main.py --reset-db

# Final Remark

In case of questions or issues, please do not hesitate to contact me.