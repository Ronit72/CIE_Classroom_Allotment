import pypyodbc as odbc
import pandas as pd
import mysql.connector
import numpy as np

def runquery3():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cra",
    )

    sql_command = '''SELECT a.room_no,i.name,s.USN,s.name, c.Course_no,c.Course_name,c.exam_date,c.time_slot
    FROM allocated a,invigilator i,exam c,student s
    WHERE i.ID=a.ID AND c.Course_no=a.Course_no AND s.USN=a.USN
    ORDER BY c.exam_date,s.USN ASC
    '''

    conncr=mydb.cursor()

    conncr.execute(sql_command)

    store=conncr.fetchall()

    mydb.close()

    # for i in store:
    #     print(i)

    np.savetxt("media/excel/alloc.csv", 
            store,
            delimiter =", ", 
            fmt ='% s')