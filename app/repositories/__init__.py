from app.database.connection import get_connection


def get_all_pets():
    # 1. Connect to MariaDB
    connection = get_connection()
    cursor = connection.cursor()


    # 2. Query the pets table
    cursor.execute("""
        SELECT
            id,
            name,
            type,
            breed,
            age,
            owner_name
        FROM pets
        ORDER BY id
    """)


    # 3. Get all rows
    pets = cursor.fetchall()


    # 4. Close database resources
    cursor.close()
    connection.close()


    # 5. Return the pets
    return pets
