###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

count = 1
dot = ". "

with open(file_name) as file:
    for line in file:
        if job_title in line:
            x = str(count) + ". " + line
            print(x)
            count += 1