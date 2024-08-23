import csv
from datetime import datetime
import re
import random
# Define the keyword categories with regular expressions
categories = {
    'Analytics': [r'\bPython\b', r'\bPandas\b', r'\bJupyter\b', r'\bPolars\b'],
    'BI': [r'\bPower BI\b', r'\bpowerbi\b', r'\bPOWERBI\b', r'\bPowerBI\b', r'\bpower bi\b', r'\bSnowflake\b', r'\bDynamics 365\b', r'\bD365\b', r'\bDashboard\b', r'\bdashboard\b', r'\bDAX\b', r'\bdax\b', r'\bPower Query\b', r'\bPowerQuery\b', r'\bpowerquery\b', r'\bpower query\b'],
    'Cloud': [r'\bAzure Fabric\b', r'\bAzureFabric\b', r'\bazure\b', r'\bBigQuery\b', r'\bBig Query\b', r'\bSynapse\b', r'\bAWS\b', r'\bData Factory\b'],
    'Machine Learning': [r'\bScikit-Learn\b', r'\bScikit Learn\b', r'\bScikitLearn\b', r'\bR\b', r'\bR Language\b', r'\bR Programming\b', r'\bAutoML\b', r'\bColab\b', r'\bTensorFlow\b', r'\bKeras\b']
}

# Function to categorize the cured_name
# Function to categorize the cured_name
def categorize(cured_name):
    print(f"Categorizing: {cured_name}")  # Debugging statement
    for category, keywords_list in categories.items():
        for keyword in keywords_list:
            if re.search(keyword, cured_name, re.IGNORECASE):
                print(f"Match found: {cured_name} -> {category}")  # Debugging statement
                return category
    # Randomly assign a category if no match is found
    random_category = random.choice(list(categories.keys()))
    print(f"No match found. Randomly assigning category: {cured_name} -> {random_category}")
    return random_category

# Function to calculate days ago
def calculate_days_ago(lastmod):
    if lastmod:  # Check if lastmod is not empty
        lastmod_date = datetime.strptime(lastmod, "%Y-%m-%d")
        current_date = datetime.now()
        delta = current_date - lastmod_date
        return delta.days
    return None  # Return None if lastmod is empty

# Process the CSV data
input_file = 'data/article_blog.csv'
output_file = 'processed_data.csv'

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['daysAgo', 'state', 'field']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        row['daysAgo'] = calculate_days_ago(row['lastmod'])
        row['state'] = "Uncategorized"
        row['field'] = categorize(row['cured_name'])
        writer.writerow(row)

print(f"Data processed and saved to {output_file}")
