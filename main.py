##################### Normal Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today =(today_month,today_day)
print(today)
# HINT 2: Use pandas to read the birthdays.csv
df = pd.read_csv("birthdays.csv")
print(df)
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in df.iterrows()}
print(birthdays_dict)
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
PLACEHOLDER = "[NAME]"

if today in birthdays_dict:
    print("SIIIIIII")
    choice_number = random.randint(1,3)
    with open(f"letter_templates/letter_{choice_number}.txt") as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace(PLACEHOLDER,birthdays_dict[today]['name'])
        my_email = "kingreyrey2022@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password="ufdjlfdrothfmmur")
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthdays_dict[today]['email'],
                msg=f"Subject: Happy Birthday!\n\n{new_letter}"
            )
            connection.close()

    print(choice_number)
else:
    print("not today bud")

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



