import pypyodbc as odbc
import pandas as pd
import mysql.connector 
from timetable.models import Timetable
from invigilator.models import Invigilator

def loadsql():
    df=pd.read_csv(r'media\excel\room.csv')
    df1=pd.read_csv(r'media\excel\exam.csv')
    df2=pd.read_csv(r'media\excel\student.csv')
    df3=pd.read_csv(r'media\excel\teacher.csv')
    df4=pd.read_csv(r'media\excel\timetable.csv')
    #print(df2)

    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cra",
    )

    coloumns=['Room_no','Capacity','Status']
    df_data=df[coloumns]
    records = df_data.values.tolist()

    coloumns1=['Course_no','Course_name','Time_slot','Exam_date']
    df_data1=df1[coloumns1]
    records1 = df_data1.values.tolist()

    coloumns2 = ['USN','SEMESTER','DEPARTMENT','NAME']
    df_data2 = df2[coloumns2]
    records2 = df_data2.values.tolist()


    coloumns3 = ['ID','Email','Invigilation_count','Name']
    df_data3 = df3[coloumns3]
    records3 = df_data3.values.tolist()

    #print(records3)

    coloumns4 = ['ID','On_Date','Free_time']
    df_data4 = df4[coloumns4]
    records4 = df_data4.values.tolist()


    sql_insert = '''
    INSERT INTO room(Room_no,Capacity,Avaliability_status)
    VALUES (%s,%s,%s)
    '''

    sql_insert1 = '''
    INSERT INTO exam(Course_no,Course_name,Time_slot,Exam_date)
    VALUES (%s,%s,%s,%s)
    '''


    sql_insert2 = '''
    INSERT INTO student(USN,SEMESTER,DEPARTMENT,NAME)
    VALUES (%s,%s,%s,%s)
    '''


    sql_insert3 = '''
    INSERT INTO invigilator(ID,Email,Invigilation_count,Name)
    VALUES (%s,%s,%s,%s)
    '''

    conncr=mydb.cursor()

    conncr.execute("SET FOREIGN_KEY_CHECKS=0")

    conncr.execute("TRUNCATE TABLE room")
    conncr.executemany(sql_insert, records)
    mydb.commit()

    conncr.execute("TRUNCATE TABLE exam")
    conncr.executemany(sql_insert1, records1)
    mydb.commit()

    conncr.execute("TRUNCATE TABLE student")
    conncr.executemany(sql_insert2, records2)
    mydb.commit()

    conncr.execute("TRUNCATE TABLE invigilator")
    conncr.executemany(sql_insert3, records3)
    mydb.commit()

    for _, row in df4.iterrows():
        on_date = row['On_Date']
        free_time = row['Free_time']
        invigilator = Invigilator.objects.get(id = row['ID'])
        Timetable.objects.get_or_create(on_date=on_date, free_time=free_time, invigilator = invigilator)

    conncr.execute("SET FOREIGN_KEY_CHECKS=1")

    mydb.close()
    # print(mydb)