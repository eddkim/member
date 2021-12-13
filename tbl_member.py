import sqlite3

def getconn():
    conn = sqlite3.connect('./memberdb.db')
    return conn

def create_table():
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE member(
        mid CHAR(5) PRIMARY KEY,
        passwd CHAR(8) NOT NULL,
        name TEXT NOT NULL,
        age INTEGER,
        regDate TIMESTAMP DATE DEFAULT (datetime('now','localtime'))
    );
    """
    cur.execute(sql)
    conn.commit()
    print("member 테이블 생성")
    conn.close()

def drop_table():
    conn = getconn()
    cur = conn.cursor()
    sql = "DROP TABLE member"
    cur.execute(sql)  # SQL 실행
    conn.commit()     #DB에서 커밋 완료
    conn.close()

def insert_member ():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(mid,passwd,name,age) VALUES(?,?,?,?)"
    cur.execute(sql,('cloud','m123456@','구름',100))
    conn.commit()
    print("멤버추가")
    conn.close()

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()   #db에서 반환 된 자료
    print(rs)
    for i in rs:
        print(i[0])
    conn.close()

#create_table()  # 호출
insert_member() #자료 삽입
select_member()
#drop_table()