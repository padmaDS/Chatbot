# import
import csv
import uuid

# Function to store query and response in a CSV file
user_question_uuid_map = {}

# Function to store query, response, and UUID in a CSV file
def store_query(query, file_path):
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([uuid.uuid4(), query])

query = """Sir i apply for transfer request but epfo still rejected reason is Break statement
        Rejected reason: Your Claim  Claim Id - X-X-X-X-X  has been rejected due to : 
        1) PAYMENT NOT RECEIVED FOR THE MONTH OF 05/2022 CLARIFY THE SAME 
        So i contact to my Hr he&#39;s given to me Clearfication Letter break statment and also sending Epfo office regarding
        So i request you to Epfo department please approve my transfer
        Please find the attachment pdf file
        Please reply as soon as possible?"""

# Provide the path to the CSV file where you want to store the data
csv_file_path = 'new_query.csv'
store_query(query, csv_file_path)      