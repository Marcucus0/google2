import sqlite3
import littlesFnct as l

url = "test4"
mot = "test"

conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

cursor.execute("""SELECT MOTS FROM indexInverse WHERE MOTS = ?""", (mot,))
conn.commit()
result = cursor.fetchone()

if result:
    # format: {url: nb}
    
    cursor.execute("""SELECT URLS FROM indexInverse WHERE MOTS = ?""", (mot,))
    output = cursor.fetchall()
    output = (l.turpleToString(output[0]))
    res = l.stringToDict(output)
    
    if (url in output):
        # url déja dedans:
        res[url] += 1
    else:
        # url pas dedans:
        res[url] = 1

    cursor.execute("""UPDATE indexInverse SET URLS = ? WHERE MOTS = ?""", (str(res), mot))

else:
    # pas dedans 
    urlFormat = {url: 1}
    cursor.execute("""INSERT INTO indexInverse (MOTS, URLS) VALUES(?, ?)""", (mot,str(urlFormat)))

conn.commit()
conn.close()