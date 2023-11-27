import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                     config["database"]))

    # **Query 1: Select all fields from the studio table**
    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio ORDER BY studio_name")
    studios = cursor.fetchall()

    # Print the results
    print("\n-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("\nStudio ID:", studio[0])
        print("Studio Name:", studio[1])

    # Query 2: Select all fields from the genre table
    cursor.execute("SELECT * FROM genre ORDER BY genre_id ASC")
    genres = cursor.fetchall()

    # Print the results
    print("\n-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("\nGenre ID:", genre[0])
        print("Genre Name:", genre[1])

    # Query 3: Select the movie names for those movies that have a run time of less than two hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120 ORDER BY film_name")
    movies = cursor.fetchall()

    # Print the results
    print("\n-- DISPLAYING Short Film RECORDS --")
    for movie in movies:
        print("\nFilm Name:", movie[0])
        print("Runtime:", movie[1])

    # Query 4: Get a list of film names and directors ordered by director
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films_and_directors = cursor.fetchall()

    # Print the results
    print("\n-- DISPLAYING Director RECORDS in Order --")
    for film_and_director in films_and_directors:
        print("\nFilm Name:", film_and_director[0])
        print("Director:", film_and_director[1])

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()