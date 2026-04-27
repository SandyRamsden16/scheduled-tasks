# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

MY_EMAIL = "sandy16ramsden@gmail.com" # password is "@Becker6Robbo!"
MY_PASSWORD = "gjdv wlgz tana ykuu"

with open("birthdays.csv") as dob_file:
    birthdays_df = pandas.read_csv(dob_file)        # this is a pandas DataFrame
    birthdays_dict = birthdays_df.to_dict(orient="records")
    for i in range(0, len(birthdays_dict)):
        birth_month = birthdays_dict[i]['month']
        birth_day = birthdays_dict[i]['day']

        if birth_month == today_month and birth_day == today_day:
            letter_number = random.randint(1, 3)

            with open(f"./letter_templates/letter_{letter_number}.txt") as letter_file:
                draft_text = letter_file.read()
                final_text = draft_text.replace("[NAME]", birthdays_dict[i]['name'])
                email = birthdays_dict[i]['email']

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=email,
                                        msg=f"Subject: Happy Birthday!\n\n{final_text}")
