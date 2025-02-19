import mysql.connector


def get_connectors(setup_data):
    try:
        conn = mysql.connector.connect(
            host=setup_data["DB_HOST"],
            user=setup_data["DB_USER"],
            password=setup_data["DB_PASS"],
            database=setup_data["DB_NAME"],
            autocommit=True
        )

        if conn.is_connected():
            print("Connected to the database!")

        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return conn, cursor


def close_connectors(cursor, conn):
    cursor.close()
    conn.close()
    return "Connection closed."
