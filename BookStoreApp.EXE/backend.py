import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, authur text, year integer, isbn integer )")
    conn.commit()
    conn.close()

def insert(title,authur,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", ((title).title(),(authur).title(),year,isbn)) #create a tuple of all the parameters
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows= cur.fetchall()
    conn.close()
    return rows

def search(title="",authur="",year="",isbn=""): #the empty-string will help stop error if the user didnt input all the parameters
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR authur=? OR year=? OR isbn=?", ((title).title(),(authur).title(),year,isbn))#this helps when the user inputs any of these parameters
    rows= cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,)) #takes the id of the book and deletes the book
    conn.commit()
    conn.close()

def update(id,title,authur,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,authur=?,year=?,isbn=? WHERE id=?", (title.title(),authur.title(),year,isbn,id))
    conn.commit()
    conn.close()


#connect()
#update(3,"Wedding Planner","oliver Renolds", 1985, 993456866)
#insert("Treasure Island ","Oliver Campbel",1994,78956432)
#delete(4)
#print(view())
#print(search(year=1994))
