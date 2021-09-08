import pymysql

F_probability=0.2

conn=pymysql.connect(host='localhost',port=3306,user='root',password='adityabarsainya',db='ai_project')
cursor=conn.cursor()

def insert_db(i_word,i_type):
    try:
        cursor.execute("""INSERT INTO `db` VALUES ('%s','%s','%f','%d')"""%(i_word,i_type,float(0.0),0))
        conn.commit()
    except:
        conn.rollback()
        
    
def find_db(i_word,i_type):
    sql='SELECT word,type FROM `db`;'
    cursor.execute(sql)
    for data in cursor:
        if(i_word==data[0] and i_type==data[1]):
            return True
    return False    

def update_db(i_word,i_type):
    count=0
    temp=0
    prob=0.0
    cursor_temp=conn.cursor()
    sql="SELECT * FROM `db` WHERE word='%s'"
    cursor.execute(sql%i_word)
    for data in cursor:
        temp=temp+data[3]
    temp=temp+1
    cursor.execute(sql%i_word)
    cursor_temp.execute(sql%i_word)    

    for data in cursor:
        count=data[3]
        if(i_type==data[1]):
            count=count+1
        prob=float(count/temp)
        cursor_temp.execute("""UPDATE `db` SET count='%d',p_word=%f WHERE word='%s' AND type='%s' """%(count,prob,data[0],data[1]))
    conn.commit()     
            
def show_db():
    sql='SELECT * FROM `db`;'
    cursor.execute(sql)
    countrow= cursor.execute(sql)
    print("Number of rows: ",countrow)
    for data in cursor:
        print(data)

def correctPos_db(i_word):
    sql="SELECT * from `db` WHERE word='%s'"
    cursor.execute(sql%i_word)
    prob=0.0
    verb=""
    for data in cursor:
        temp=data[2]
        temp1=data[1]
        if(prob<temp):
            prob=temp
            verb=temp1
    return verb    


def close_db():
    cursor.close()
    conn.close()
