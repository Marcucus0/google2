import sqlite3
import littlesFnct as l

def writeIndex(url):
    conn = sqlite3.connect('ma_base.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT PAGETEXT FROM sitesreferences""")

    for i in cursor.fetchall():
        for phrases in i:
            for mot in phrases.split():
            
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
