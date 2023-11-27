import mysql.connector

def show_films(cursor, title):


    # Construct the SQL query.
    query = """
        SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS Studio_Name
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """

    # Execute the SQL query.
    cursor.execute(query)

    # Fetch all the results from the cursor.
    films = cursor.fetchall()

    # Format the output label.
    print("\n  -- DISPLAYING FILMS AFTER DELETE --".format(title))

    # Iterate over the results and display them.
    for film in films:
        print(f"\nFilm Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre Name: {film[2]}")
        print(f"Studio Name: {film[3]}")

# Connect to the database.
conn = mysql.connector.connect(host="localhost", user="movies_user", password="popcorn", database="movies")

# Create a cursor object.
cursor = conn.cursor()

# Display the selected contents of the film table.
show_films(cursor, "All Films")

# Display the selected contents of the film table where the genre is equal to "Horror".

# Close the cursor and connection.
cursor.close()
conn.close()
