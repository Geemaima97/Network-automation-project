from dotenv import load_dotenv
import os
import csv

load_dotenv()

userName = os.getenv("NET_USERNAME")
password = os.getenv("NET_PASSWORD")
secret = os.getenv("NET_SECRET")

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


#print(f"Username: {userName}")
#print(f"Password: {password}")
#print(f"Secret: {secret}") 



def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data


    