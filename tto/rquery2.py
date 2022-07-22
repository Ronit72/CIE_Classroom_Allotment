import pypyodbc as odbc
import pandas as pd
import mysql.connector
import numpy as np

def runquery2():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cra",
    )

    sql_command = '''SELECT DISTINCT(i.ID),i.name,c.Course_no  ,c.Course_name,a.room_no,c.time_slot,c.exam_date
    FROM allocated a,invigilator i,exam c
    WHERE i.ID=a.ID AND c.Course_no=a.Course_no
    ORDER BY c.exam_date ASC
    '''

    conncr=mydb.cursor()

    conncr.execute(sql_command)

    store=conncr.fetchall()

    mydb.close()

    # for i in store:
    #     print(i)

    np.savetxt("media/excel/teacher_alloc.csv", 
            store,
            delimiter =", ", 
            fmt ='% s')