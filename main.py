import sqlite3
from fastapi import FastAPI

app = FastAPI()

# koneksi ke database
def connect_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn

# fungsi menampilan data dari database,
def get_university_data(conn):
    cursor = conn.cursor()

    # Query get data
    query = '''
        SELECT u.name, u.country, u.state_province, d.name as domain, w.name as webpage
        FROM university u
        LEFT JOIN uni_domain_pages udp ON u.id = udp.id_uni
        LEFT JOIN domains d ON udp.id_domain = d.id
        LEFT JOIN uni_web_pages uwp ON u.id = uwp.id_uni
        LEFT JOIN webpages w ON uwp.id_web_pages = w.id
    '''

    cursor.execute(query)
    # ambil semua data
    rows = cursor.fetchall()

    # Code dibawah adalah mempersiapkan payload seperti yang ada diformat kedalam array of object
    university_data = []

    for row in rows:
        university_data.append({
            "country": row[1],
            "web_pages": [row[4]],  # 
            "state-province": row[2],
            "name": row[0],
            "domains": [row[3]],
            "alpha_two_code": "ID" 
        })
    return university_data

# Endpoint to get university data
@app.get("/university")
async def get_university():
    database_name = 'university_database.db'
    conn = connect_database(database_name)
    university_data = get_university_data(conn)
    # Close the database connection
    conn.close()
    return university_data
