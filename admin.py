import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pranay@@2005",
    database="railway"
)
cursor = conn.cursor()

def create_table():
    cursor.execute('''create table trains ( number int(5), name varchar(20))''')
    cursor.execute('''create table stations( id int,tno varchar(6), station varchar(50))''')
#initially this method is run or queries executed  while creating database 
#just to create tables trains,stations 




def add_train():
    try: 
        y=int(input("Enter train number : "))
        z=input("Enter train name : ")
        cursor.execute('''insert into trains values (%s,%s)''',(y,z))
        #train number and name inserted into trains table

        a = 't' + str(y)        
        b = int(input("Enter number of stations: "))
        i = 1
        while i <=b:
            c = input("Enter station " + str(i) + ": ")
            cursor.execute('''insert into stations values (%s, %s, %s)''', (i, a, c))
            i += 1
        #station names are inserted into stations table along with ids, ids are used in next 
        #fir train number 12712  t12712 is inserted because in next step we cannot create table with name 12712

        cursor.execute(f'''create table {a} (id int,source varchar(100),destination varchar(100),CC INT,S2 INT )''')
        #table is created with t+train number

        cc=int(input("Enter number of CC tickets :  "))
        s2=int(input("Enter number of 2S tickets :  "))
        cursor.execute(f'''select station from stations where tno = '{a}'  ''') 
        aa=cursor.fetchall()
        l=[p[0] for p in aa]
        for i in range(0,len(l)):
            for j in range(i+1,len(l)):
                x=(i+1)*b+j+1
                cursor.execute(f'''insert into {a} values (%s,%s,%s,%s,%s)''',(x,l[i],l[j],cc,s2))
                #all possible combination of journeys for that train are inserted into that train table along with tickets count
                #combination of journey ids are (id of source)*total nunber of stations +(id of destination)
                #i,j starts from 0 but ids start from 1 so (i+1)*b+j+1


        conn.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as error:
        print(f"Failed to work with MySQL: {error}")



def find_trains(s,d):
    cursor.execute(f'''
    SELECT t1.tno
    FROM stations t1
    JOIN stations t2 ON t1.tno = t2.tno 
    WHERE t1.station = '{s}' AND t2.station = '{d}' and t1.id < t2.id''')
    x=cursor.fetchall()
    l=[p[0] for p in x]
    l=[int(p[1:]) for p in l]
    print(l)
    #finds trains available for our desired journey






def book_ticket():
    try:
        s=input("Enter source : ")
        d=input("Enter destination : ")
        find_trains(s,d)
        t='t' + input("Enter train number : ")
        x=int(input("Enter 1 for CC and 2 for 2S : "))
        if x==1:
            y='CC'
        elif x==2:
            y='S2'
        else:
            print("Enter valid number !!")
        

        cursor.execute(f'''select max(id) from stations where tno = '{t}' ''')
        m= cursor.fetchone()[0]
        cursor.execute(f'''select id from stations where tno = '{t}' and station = '{s}' ''')
        ss=cursor.fetchone()[0]
        cursor.execute(f'''select id from stations where tno = '{t}' and station = '{d}' ''')
        dd= cursor.fetchone()[0]
        a=ss*m+dd      #combination of our jouney id , this id is used for tracking number of tickets 
        cursor.execute(f'''select {y} from {t} where id= {a} ''')
        b=cursor.fetchone()[0]
        print("Number of tickets available for your journey : " ,b)


        n=int(input("Enter number of tickets : "))

        cursor.execute(f'''select station from stations where tno = '{t}' ''')
        r=cursor.fetchall()
        l=[p[0] for p in r]
        for i in range(l.index(d)):
            for j in range(l.index(s)+1,len(l)):
                x=(i+1)*m+j+1
                cursor.execute(f'''update {t} set {y} ={y}-{n}  where id = {x} ''')      #in our selected train table and jouney id , tickets are updated
        conn.commit()
    except mysql.connector.Error as error:
        print(f"Failed to work with MySQL: {error}")


add_train()
book_ticket()
