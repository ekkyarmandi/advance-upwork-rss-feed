# import sqlite libraries
import sqlite3
import json
from datetime import datetime

# import Objects
from Entry import Entry


def create_table(database: str, table: str) -> None:
    '''
    Create a new table
    :param database: str, database path
    :param table: str, table name
    '''
    
    # connect to database and create a table
    con = sqlite3.connect(database)
    cur = con.cursor()
    cmd = f"""
    CREATE TABLE {table} (
        hash TEXT UNIQUE,
        title TEXT,
        description TEXT,
        link TEXT,
        budget TEXT,
        timestamp INTEGER,
        category TEXT,
        tags TEXT,
        country TEXT,
        printed INTEGER
    )
    """
    cur.execute(cmd)
    con.commit()
    con.close()

def insert(database: str, entry: dict) -> None:
    ''' Insert data into database '''

    # load the blacklist data
    forbidden_category = json.load(open("data/blacklist-category.json"))
    forbidden_text = json.load(open("data/blacklist-description.json"))

    # connect to the database
    con = sqlite3.connect(database)
    cur = con.cursor()
    if entry['category'] not in forbidden_category and all([t not in entry['description'] for t in forbidden_text]):
        cmd = """INSERT or IGNORE INTO jobs VALUES (?,?,?,?,?,?,?,?,?,?)"""
        cur.execute(cmd, (
            entry['hash'],
            entry['title'],
            entry['description'],
            entry['link'],
            entry['budget'],
            entry['timestamp'],
            entry['category'],
            entry['tags'],
            entry['country'],
            0
        ))
        cur.execute("UPDATE jobs SET budget = NULL WHERE budget = 'null'")
        cur.execute("UPDATE jobs SET tags = NULL WHERE tags = 'null'")
        con.commit()
    con.close()

def query_all(database: str, table: str = "jobs", time_constrain: int = 3) -> list:
    '''
    Query all entries
    :param database: str, database path
    :param table: str, table name
    :param time_constrain: int, maximum hours
    :return entries: list, of results
    '''
    
    # connect to the database
    now = datetime.now()
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute(f"SELECT timestamp,hash,printed FROM {table} ORDER BY timestamp DESC")
        data = cur.fetchall()
        
    # filter the query results
    results = []
    for i in data:
        entry = {
            "posted_on": int((now.timestamp()-i[0])/3600),
            "hash": i[1],
            "printed": i[2]
        }
        
        # filter based on time constrain variable
        if entry['posted_on'] <= time_constrain:
            cur.execute(f"SELECT * FROM {table} WHERE hash=?",(entry['hash'],))
            result = cur.fetchone()
            results.append(Entry(result))
        
        # delete the post if the post is outdated
        elif entry['posted_on'] > time_constrain:
            cur.execute(f"DELETE FROM {table} WHERE hash=?",(entry['hash'],))

    # commit the changes and then close the database
    con.commit()
    con.close()

    # return the results
    return results

def clear(database: str, table: str = "jobs") -> None:
    '''Clear database'''

    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(f"DELETE FROM {table};")
    con.commit()
    con.close()

def reset(database: str, table: str = "jobs") -> None:
    '''Set printed column into 0 or false'''

    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(f"UPDATE {table} SET printed = 0;")
    con.commit()
    con.close()

if __name__ == "__main__":

    # reset("data/jobs.db")
    # data = query_all("data/jobs.db")
    # print(data[-1])
    clear("data/jobs.db")