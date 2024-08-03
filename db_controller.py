import sqlite3
import json
import eel

def create_connection():
    # Connecting to sqlite
    conn = sqlite3.connect('data.db')
    
    # cursor object
    cursor = conn.cursor()
    
    # Drop the EMOTIONS table if already exists.
    cursor.execute("DROP TABLE IF EXISTS EMOTIONS")

    # Creating table
    table = """ CREATE TABLE EMOTIONS ( 
                Emotion_Type CHAR(25) NOT NULL,
                Link VARCHAR(255) NOT NULL,
                File_Format CHAR(25) NOT NULL
            ); """
    
    cursor.execute(table)
    
    print("Table is Ready")
    
    # Close the connection
    conn.close()

# create_connection() 

def insert_data():
    # Connecting to sqlite 
    conn = sqlite3.connect('data.db') 

    # Creating a cursor object
    cursor = conn.cursor() 

    # Queries to INSERT records. 
    cursor.execute('''INSERT INTO EMOTIONS VALUES ('Happy', 'https://www.youtube.com/embed/veZOrXVHf7U?si=c_dx9V3Ts_k89ct9', 'Video')''')
    cursor.execute('''INSERT INTO EMOTIONS VALUES ('Happy', 'https://www.youtube.com/embed/_0a998z_G4g?si=6dpNml6PmC7bunkQ', 'Video')''')
    cursor.execute('''INSERT INTO EMOTIONS VALUES ('Happy', 'https://www.youtube.com/embed/6Lsil8253GI?si=wHALvjSx98w06DF1', 'Video')''')
    cursor.execute('''INSERT INTO EMOTIONS VALUES ('Happy', 'https://www.youtube.com/embed/qi2m4V21bw4?si=1D8ukYPRl4Lcc0p8', 'Video')''')
    cursor.execute('''INSERT INTO EMOTIONS VALUES ('Happy', 'https://www.youtube.com/embed/jHlhosC9IJ0?si=rqJMe_Zt6y3-zpHe', 'Video')''')
    cursor.execute('''INSERT INTO EMOTIONS VALUES ('Happy', 'https://www.youtube.com/embed/6n9ESFJTnHs?si=E6bGd0M_5xBOk-5n', 'Video')''')
    cursor.execute('''INSERT INTO EMOTIONS VALUES ('Happy', 'https://www.youtube.com/embed/JYNyQcblzgI?si=bX9n1F1ilFVwYxqw', 'Video')''')
    cursor.execute('''INSERT INTO EMOTIONS VALUES ('Happy', 'https://www.youtube.com/embed/o9NfXIXzgnA?si=ZOl6pcNJWtDP9cEN', 'Video')''')

    # Display data inserted 
    print("Data Inserted in the table: ") 
    data=cursor.execute('''SELECT * FROM EMOTIONS''') 
    for row in data: 
        print(row) 

    # Commit your changes in the database	 
    conn.commit() 

    # Closing the connection 
    conn.close()

# insert_data()

@eel.expose
def get_data():
    # Connecting to sqlite 
    conn = sqlite3.connect('data.db') 

    # Creating a cursor object
    cursor = conn.cursor()
    # Display data inserted 
    # print("Data Inserted in the table: ") 
    data=cursor.execute('''SELECT * FROM EMOTIONS''') 
    # print(type(data))
    data_dict = {}
    i = 0

    for row in data: 
        data_dict["img-" + str(i)] = row[1]
        i += 1
    # print(lst_data)
    # Closing the connection 
    conn.close()

    # data_json = json.dumps(data_dict)
    # print(data_json)
    return data_dict
# get_data()