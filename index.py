"""
CSE110 Module 2 Team assignment
Slack Channel: #rock-cse110-fall2022
Creators: Robbie Platt and Robert Boyd 
Date: Sept. 20, 2022
"""


def main():
    first_name = input("What is your first name:  ")
    last_name = input("What is your last name: ")
    job_title = input("What is your job title? ")
    id = input("What is your id number? ")
    email = input("What is your email? ")
    phone = input("What is your phone number? ")
    hair = input("What is your hair color? ")
    eyes = input("What is your eye color? ")
    month = input("What is your birth month?: ")
    license = input("Are you licensed? If yes what kind of license?: ")

    capped_last = last_name.upper()
    cap_job = job_title.capitalize()
    email_lower = email.lower()


    print(f"""
    ----------------------------------------
    {capped_last}, {first_name}
    {cap_job}
    ID: {id}

    {email}
    {phone}

    Hair: {hair}           Eyes: {eyes}
    Month: {month}      License Type: {license}
    ----------------------------------------
    """)

if __name__== "__main__":
    main()
