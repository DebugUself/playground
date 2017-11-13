import sqlite3

def create_database():
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS FITDATA 
              (TIME    VARCHAR  PRIMARY KEY,
               M1     int,
               M2     int,
               M3     int,
               M4     int,
               M5     int,
               M6     int,
               M7     int,
               M8     int,
               M9     int,
               M10    int);''')
    
    
    c.execute('''CREATE TABLE IF NOT EXISTS FITMOVEMENT
              (ID             int  PRIMARY KEY,
               MOVEMENT       text,
               TIME           int,
               FREQUENCY      int,
               NUMOFGROUPS    int,
               WEIGHT         int,
               DISTANCE       int);''')
    conn.close()

def export_movement():
    record = [] 
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    cursor = c.execute("SELECT *from FITMOVEMENT")
    for row in cursor:
        record.append(row)
    conn.close()
    return record

def export_fitdata():
    record = [] 
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    cursor = c.execute("SELECT *from FITDATA")
    for row in cursor:
        record.append(row)
    conn.close()
    return record
 

def select_movement(fmid):
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM FITMOVEMENT WHERE ID =?''', (fmid,)) 
    result = c.fetchone() 
    conn.close()
    return result

def insert_movemnet(fmid,movement,time,frequency,numofgroups,weight,distance):
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO FITMOVEMENT VALUES(?,?,?,?,?,?,?)",(fmid,movement,time,frequency,numofgroups,weight,distance))
    except:
        c.execute('''UPDATE FITMOVEMENT set MOVEMENT = ?, TIME = ?, FREQUENCY = ?, NUMOFGROUPS = ?, WEIGHT = ?, DISTANCE = ? where ID=?''',(movement,time,frequency,numofgroups,weight,distance,fmid))   
    conn.commit()
    conn.close()

def select_fitdata(time):
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM FITDATA WHERE TIME =?''', (time,)) 
    result = c.fetchone() 
    conn.close()
    return result

def insert_fitdata(time,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10):
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO FITDATA VALUES(?,?,?,?,?,?,?,?,?,?,?)",(time,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10))
    except:
        c.execute('''UPDATE FITDATA set M1 = ?, M2 = ?, M3 = ?, M4 = ?, M5 = ?, M6 = ?, M7 = ?, M8 = ? , M9 = ? , M10 = ?   where time=?''',(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,time))   
    conn.commit()
    conn.close()

def count_movement():
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    c.execute("SELECT *  FROM FITMOVEMENT")
    r = c.fetchall()
    conn.close()

    return len(r)

def count_fitdata():
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    c.execute("SELECT *  FROM FITDATA")
    r = c.fetchall()
    conn.close()

    return len(r)

def Delect_movement():
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    c.execute("DELETE FROM FITMOVEMENT")
    conn.commit()
    conn.close()


def Delect_fit():
    conn = sqlite3.connect('fitlogtest.db')
    c = conn.cursor()
    c.execute("DELETE FROM FITDATA")
    conn.commit()
    conn.close()

def record_movement(movementdata):
    fitdata = []
    fmid = count_movement() + 1
    for data in movementdata.split(","):
        if data != "":
            date,movement,time,frequency,numofgroups,weight,distance = data.split(" ")
            insert_movemnet(fmid,movement,time,frequency,numofgroups,weight,distance)
            fitdata.append(fmid)
            fmid = fmid + 1
    return date,fitdata 

def record_fitdata(date,fitdata):
    m=[]
    result = select_fitdata(date)
    if result == None:
        for i in range(0,10):
            m.append(0)  
        m[0] = fitdata[0]    
    else:
        for index,i in enumerate(result):
            if index != 0:
                m.append(i)

        for index,i in enumerate(m):
            if i == 0:
                m[index] = fitdata[0]
                break	
        
    #print (m)
    insert_fitdata(date,m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9])

def history_fitdata():
    fit_history = []
    record = export_fitdata()
    for fit in record:
        date = fit[0]
        date_fit = []
        #print ("%s运动记录:"%date)
        for j in fit[1:]:
            k = select_movement(j) 
            if k != None:
               date_fit.append(k)
               fit_str = str(k[1])+"  时间:"+str(k[2])+",次数:"+str(k[3])+",组数:"+str(k[4])+",重量:"+str(k[5])+",距离:"+str(k[6])
               #print(fit_str)
        fitlist =[date,date_fit]
        fit_history.append(fitlist)
    return fit_history
         

if __name__ == "__main__":
    create_database()

