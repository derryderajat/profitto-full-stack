import sqlite3

# Function to connect to the database
def connect_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn

# Function to display the content of the database
def display_database_content(conn):
    cursor = conn.cursor()

    # Query to fetch data from the database
    query = '''
        SELECT u.name, u.country, u.state_province, d.name as domain, w.name as webpage
        FROM university u
        LEFT JOIN uni_domain_pages udp ON u.id = udp.id_uni
        LEFT JOIN domains d ON udp.id_domain = d.id
        LEFT JOIN uni_web_pages uwp ON u.id = uwp.id_uni
        LEFT JOIN webpages w ON uwp.id_web_pages = w.id
    '''

    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the fetched data
    for row in rows:
        print("University:", row[0])
        print("Country:", row[1])
        print("State/Province:", row[2])
        print("Domain:", row[3])
        print("Webpage:", row[4])
        print("------------")

# Connect to the database
database_name = 'university_database.db'
conn = connect_database(database_name)

# Display the content of the database
display_database_content(conn)

# Close the database connection
conn.close()
