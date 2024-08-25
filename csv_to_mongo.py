import csv
from pymongo import MongoClient
import urllib.parse


username = urllib.parse.quote_plus('sitemap') #has to be removed for production
password = urllib.parse.quote_plus('H9DrhdSR1PodXOUA') #has to be removed for production
cluster = 'site.heckbaa.mongodb.net/' #has to be removed for production


csv_file_path = 'processed_data.csv'


connection_string = f'mongodb+srv://{username}:{password}@{cluster}'
client = MongoClient(connection_string)

db = client['blue-sitemaps']
collection = db['data']

# Read CSV and insert into MongoDB
def csv_to_mongodb(csv_file_path):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                print(row)  # Print the current row
                collection.insert_one(row)
        print("Data insertion completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the insertion
csv_to_mongodb(csv_file_path)
