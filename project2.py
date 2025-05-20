import random

def generate_fake_job_title():
    adjectives = ['Senior', 'Junior', 'Lead', 'Assistant', 'Chief', 'Head', 'Certified', 'Experienced', 'Expert', 'Skilled']
    roles = ['Developer', 'Engineer', 'Designer', 'Manager', 'Analyst', 'Consultant', 'Coordinator', 'Technician', 'Specialist', 'Administrator']
    suffixes = ['I', 'II', 'III', 'Supervisor', 'Officer', 'Associate', 'Executive', 'Advisor', 'Agent', 'Representative']

    adjective = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)

    fake_title = f"{adjective} {role} {suffix}"
    print(f"Your fake job title is: {fake_title}")

    while True:
        another = input("Would you like another job title? (yes/no): ").strip().lower()
        if another == 'yes':
            adjective = random.choice(adjectives)
            role = random.choice(roles)
            suffix = random.choice(suffixes)
            fake_title = f"{adjective} {role} {suffix}"
            print(f"Your new fake job title is: {fake_title}")
        elif another == 'no':
            print("Thanks for playing! Stay creative!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    generate_fake_job_title()
