# Speed Dating Generator

## Generating fake data:
GLOBAL VARIABLES:
    
    NUMBER_OF_USERS 

Run:

    python fake_users.py

And will generate `users.csv` file with fake users generated by [randomuser API](https://randomuser.me/)

## Generate Speed Dating:
GLOBAL VARIABLES:
    
    CVS_PATH (output file)
    N_PEOPLE_BY_GROUP (groups of n people)
    N_ITERATIONS (iterations)

Run:

    python speed_date.py

And will generate `meetings.txt` with the schedule of the speed datings.

If the number of users is not even the last group will have three people.