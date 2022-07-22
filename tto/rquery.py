import pypyodbc as odbc
import pandas as pd
import mysql.connector
import numpy as np

def runquery():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cra",
    )

    sql_command = '''SELECT s.USN,s.name,s.Department,s.semester,c.Course_no,a.room_no,c.time_slot,c.exam_date
    FROM allocated a,student s,exam c
    WHERE s.USN=a.USN AND c.Course_no=a.Course_no
    ORDER BY c.exam_date ASC
    '''

    conncr=mydb.cursor()

    conncr.execute(sql_command)

    store=conncr.fetchall()

    mydb.close()

    np.savetxt("media/excel/studentallocationlist.csv", 
           store,
           delimiter =", ", 
           fmt ='% s')