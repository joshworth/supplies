
import MySQLdb


db = MySQLdb.connect("127.0.0.1","root","root","mccapp" )
def getWholeChapter(book,chapter):

    cursor = db.cursor()
    sql = "SELECT txt FROM KJV WHERE book=%s and chapter=%s"
    params=(book,chapter)

    cursor.execute(sql,params)
    res = cursor.fetchall()
    verses=[]

    for row in res:
        #add to list
        verses.append(row[0])
    db.close()

    return verses

    