import pymssql, random, string

def numGenerator():
#set up the db connection
    db = pymssql.connect(host='172.24.182.190', user='sa', password='1', database='myPythonDB')
    cursor = db.cursor()

# create table if not exist
   # cursor.execute('create table if not exists CODE(randCode varchar)')

#clean the data
    cursor.execute('delete from CODE')
    db.commit()

#generate random string
    for i in range(200):
        chars = string.letters + string.digits
        s = ''
        for j in range(9):
            s = s + random.choice(chars)
        cursor.execute('insert into CODE values(%s)', s)

#finnal commit
    db.commit()
    cursor.close()


#call the function
numGenerator()