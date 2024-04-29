import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sudhiksha@2004",
    database="backendexam",
    port=3306
)

cursor = conn.cursor()

query = """
SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name AS country_name
FROM locations l
INNER JOIN countries c ON l.country_id = c.country_id
WHERE c.country_name = 'Canada';
"""

cursor.execute(query)

print("#----------------Query for retriving data with using JOIN STATEMENT--------------#")
results = cursor.fetchall()

if results:
    for row in results:
        location_id, street_address, city, state_province, country_id = row
        print(f"Location ID: {location_id}")
        print(f"Street Address: {street_address}")
        print(f"City: {city}")
        print(f"State/Province: {state_province}")
        print(f"Country ID: {country_id}")
        print("-" * 10)
else:
    print("No addresses found for Canada.")

print("\n")
query = """
SELECT location_id, street_address, city, state_province, 'Canada'
FROM locations l
WHERE l.country_id = (
    SELECT country_id
    FROM countries c
    WHERE c.country_name = 'Canada'
)
"""

cursor.execute(query)

print("#------------Query for retriving data without using JOIN STATEMENT--------#")
res = cursor.fetchall()

if res:
    for row in results:
        location_id, street_address, city, state_province, country_id = row
        print(f"Location ID: {location_id}")
        print(f"Street Address: {street_address}")
        print(f"City: {city}")
        print(f"State/Province: {state_province}")
        print(f"Country ID: {country_id}")  # Country ID instead of country name
        print("-" * 30)  # Separator for each address
else:
    print("No addresses found for Canada.")

conn.close()
