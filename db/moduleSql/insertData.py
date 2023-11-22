import sqlite3
import requests
class University:
    def __init__(self, name, country, state_province, web_pages, domains):
        self.name = name
        self.country = country
        self.state_province = state_province
        self.web_pages = web_pages
        self.domains = domains

# Function to insert University instance into the database
def insert_university_into_database(conn, university):
    cursor = conn.cursor()

    # Insert data into the university table
    cursor.execute('''
        INSERT INTO university (name, country, state_province) 
        VALUES (?, ?, ?)
    ''', (university.name, university.country, university.state_province))
    conn.commit()

    # Get the last inserted university ID
    university_id = cursor.lastrowid

    # Insert data into the domains table and uni_domain_pages table
    for domain in university.domains:
        cursor.execute('''
            INSERT INTO domains (name) 
            VALUES (?)
        ''', (domain,))
        conn.commit()

        domain_id = cursor.lastrowid

        cursor.execute('''
            INSERT INTO uni_domain_pages (id_uni, id_domain) 
            VALUES (?, ?)
        ''', (university_id, domain_id))
        conn.commit()

    # Insert data into the webpages table and uni_web_pages table
    for webpage in university.web_pages:
        cursor.execute('''
            INSERT INTO webpages (name) 
            VALUES (?)
        ''', (webpage,))
        conn.commit()

        webpage_id = cursor.lastrowid

        cursor.execute('''
            INSERT INTO uni_web_pages (id_uni, id_web_pages) 
            VALUES (?, ?)
        ''', (university_id, webpage_id))
        conn.commit()

# Example JSON data
# json_data = [{'country': 'Indonesia', 'web_pages': ['http://www.akfarmitseda.ac.id/'], 'state-province': None, 'name': 'Akademi Farmasi Mitra Sehat Mandiri Sidoarjo', 'domains': ['akfarmitseda.ac.id'], 'alpha_two_code': 'ID'}]
# ============
def get_json_from_api(api_url):
    try:
        # Sending an HTTP GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            json_data = response.json()
            return json_data
        else:
            # If the request was not successful, print the status code
            print(f"Error: {response.status_code}")
            return None

    except requests.RequestException as e:
        # Print any exception that occurred during the request
        print(f"Request Exception: {e}")
        return None

# Example usage:
api_url = "http://test-profitto-api.s3.ap-southeast-1.amazonaws.com/university.json"  # Replace with your API endpoint
json_data = get_json_from_api(api_url)[:5]

if json_data:
    print("JSON data:")
    data = json_data[0]
    print(json_data[:1])
    
else:
    print("Failed to retrieve JSON data from the API.")

# ==============

# Connect to the database
database_name = 'university_database.db'
def connect_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn

conn = connect_database(database_name)

# Iterate over the JSON data and insert each University instance into the database
for entry in json_data:
    university = University(
        name=entry['name'],
        country=entry['country'],
        state_province=entry['state-province'],
        web_pages=entry['web_pages'],
        domains=entry['domains']
    )

    insert_university_into_database(conn, university)
    print("SUCCESS menyimpan")

# Close the database connection
conn.close()