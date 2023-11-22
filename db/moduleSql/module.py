import sqlite3

# Fungsi untuk membuat tabel university
def create_university_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS university (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            country TEXT,
            state_province TEXT
        )
    ''')
    conn.commit()

# Fungsi untuk membuat tabel domains
def create_domains_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')
    conn.commit()

# Fungsi untuk membuat tabel webpages
def create_webpages_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS webpages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')
    conn.commit()

# Fungsi untuk membuat tabel uni_web_pages
def create_uni_web_pages_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uni_web_pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_web_pages INTEGER,
            id_uni INTEGER,
            FOREIGN KEY (id_web_pages) REFERENCES webpages (id),
            FOREIGN KEY (id_uni) REFERENCES university (id)
        )
    ''')
    conn.commit()

# Fungsi untuk membuat tabel uni_domain_pages
def create_uni_domain_pages_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uni_domain_pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_uni INTEGER,
            id_domain INTEGER,
            FOREIGN KEY (id_uni) REFERENCES university (id),
            FOREIGN KEY (id_domain) REFERENCES domains (id)
        )
    ''')
    conn.commit()

# Fungsi untuk terhubung ke database
def connect_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn

# Membuat dan mengelola database
database_name = 'university_database.db'
conn = connect_database(database_name)
create_university_table(conn)
create_domains_table(conn)
create_webpages_table(conn)
create_uni_web_pages_table(conn)
create_uni_domain_pages_table(conn)

# Menutup koneksi database
conn.close()
