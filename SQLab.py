import sqlite3

import pandas as pd
 
pd.options.display.max_columns = 10

connection = sqlite3.connect('books.db')


# Select all authors’ last names from the authors table in descending order. (Take screenshot of output)
authors = pd.read_sql("""SELECT last
                    FROM authors
                    ORDER BY last DESC""",
                  connection,)



# Select all book titles from the titles table in ascending order.
books = pd.read_sql("""SELECT title FROM titles ORDER BY title ASC
""", connection)




# Use an INNER JOIN to select all the books for a specific author. Include the title, copyright year and ISBN. Order the information alphabetically by title.

inner2 = pd.read_sql("""SELECT title, copyright, isbn
                        FROM authors 
                        INNER JOIN author_ISBN USING (id)   
                        INNER JOIN titles USING (isbn)
                        WHERE first = 'Harvey' AND last = 'Deitel'
                        ORDER BY title ASC """, connection)

# Insert a new author into the authors table.
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                                VALUES ('Mat', 'Bakarich')""")
     
mat = pd.read_sql("""SELECT id, first, last FROM authors ORDER BY first ASC
""", connection)


# Insert a new title for an author. 
# Remember that the book must have an entry in the author_ISBN table and an entry in the titles table.

mat_book = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                                VALUES ('0000000000', 'Being a Dummy for Dummies', 2 , '1984')""")
mat_book = cursor.execute("""INSERT INTO author_ISBN (id, isbn)
                                VALUES ('6', '0000000000')""")
mat_book = pd.read_sql("""SELECT title, copyright, isbn
                        FROM authors 
                        INNER JOIN author_ISBN USING (id)   
                        INNER JOIN titles USING (isbn)
                        WHERE first = 'Mat' AND last = 'Bakarich'
                        ORDER BY title ASC """, connection)

#SELECT *
#FROM table1
#JOIN table2 USING (id)
#JOIN table3 USING (id)



#print(authors)
#print(books)
#print(inner2)
#print(mat)
print(mat_book)