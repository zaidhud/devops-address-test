import os
import time
import psycopg2


DB_HOST = os.getenv("DB_HOST", "address-db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "addresses")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

OUTPUT_FILE = "/var/www/html/index.html"


def connect_to_database():
    for attempt in range(10):
        try:
            return psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
        except Exception as error:
            print(f"Database not ready yet. Attempt {attempt + 1}/10")
            print(error)
            time.sleep(3)

    raise Exception("Could not connect to the database after 10 attempts")


def fetch_addresses():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT first_name, last_name, address, city, state, zipcode, country, valid
        FROM addresses
        ORDER BY id;
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows


def generate_html(rows):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Address Validation Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                padding: 30px;
            }
            h1 {
                color: #1f2937;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                background: white;
            }
            th {
                background: #111827;
                color: white;
                padding: 10px;
            }
            td {
                border: 1px solid #ddd;
                padding: 8px;
            }
            tr:nth-child(even) {
                background: #f9fafb;
            }
            .valid {
                color: green;
                font-weight: bold;
            }
            .invalid {
                color: red;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>Address Validation Report</h1>
        <table>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Address</th>
                <th>City</th>
                <th>State</th>
                <th>Zipcode</th>
                <th>Country</th>
                <th>Valid</th>
            </tr>
    """

    for row in rows:
        first_name, last_name, address, city, state, zipcode, country, valid = row

        if valid:
            status = "<span class='valid'>Valid</span>"
        else:
            status = "<span class='invalid'>Not Checked</span>"

        html += f"""
            <tr>
                <td>{first_name}</td>
                <td>{last_name}</td>
                <td>{address}</td>
                <td>{city}</td>
                <td>{state}</td>
                <td>{zipcode}</td>
                <td>{country}</td>
                <td>{status}</td>
            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    with open(OUTPUT_FILE, "w") as file:
        file.write(html)


if __name__ == "__main__":
    addresses = fetch_addresses()
    generate_html(addresses)
    print(f"Generated HTML file: {OUTPUT_FILE}")
