# Codebase for testing the system developed in the master thesis "A Gamified Design of a Collaborative Project-based Platform"

## Usage instructions

After having started the system, by initializing the backend (https://github.com/vallout/master_thesis_backend) and frontend (https://github.com/vallout/master_thesis_frontend.git), these files can be used to execute the scenario-tests presented in the thesis.

In the test-cases, the tests have been executed on python 3.9.1

Install the needed packages as follows: \
`pip install selenium`\
`pip install pymongo`\
`pip install bson`

To start the tests for scenario 1 run:

`python fill_database.py` (to initialize the database)\
`python database_eval_scenario1.py` (to start the mongoDB monitoring)\
`python selenium_scenario1.py` (to start the automated UI-interaction)

To start the tests for scenario 2 run:

`python fill_database_2.py` (to initialize the database)\
`python database_eval_scenario2.py` (to start the mongoDB monitoring)\
`python selenium_scenario2.py` (to start the automated UI-interaction)
