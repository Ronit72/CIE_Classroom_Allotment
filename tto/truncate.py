import pypyodbc as odbc
import pandas as pd
import mysql.connector
import numpy as np

def truncate():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cra",
    )

    conncr=mydb.cursor()

    conncr.execute("TRUNCATE TABLE allocated")
    mydb.commit()

    sql_command = ''' SELECT count(*)
    FROM tto_excel
    WHERE title='student'
    '''

    sql_command1 = ''' SELECT count(*)
    FROM tto_excel
    WHERE title='teacher'
    '''

    sql_command2 = ''' SELECT count(*)
    FROM tto_excel
    WHERE title='exam'
    '''

    sql_command3 = ''' SELECT count(*)
    FROM tto_excel
    WHERE title='room'
    '''

    sql_command4 = ''' SELECT count(*)
    FROM tto_excel
    WHERE title='ttimetable'
    '''
    conncr.execute(sql_command)
    store=conncr.fetchall()
    z=list(store[0])

    if(z[0]==0):
        conncr.execute("SET FOREIGN_KEY_CHECKS=0")
        conncr.execute("TRUNCATE TABLE student")
        conncr.execute("SET FOREIGN_KEY_CHECKS=1")
    mydb.commit()

    conncr.execute(sql_command1)
    store1=conncr.fetchall()
    z1=list(store1[0])

    if(z1[0]==0):
        conncr.execute("SET FOREIGN_KEY_CHECKS=0")
        conncr.execute("TRUNCATE TABLE invigilator")
        conncr.execute("SET FOREIGN_KEY_CHECKS=1")
    mydb.commit()

    conncr.execute(sql_command2)
    store2=conncr.fetchall()
    z2=list(store2[0])

    if(z2[0]==0):
        conncr.execute("SET FOREIGN_KEY_CHECKS=0")
        conncr.execute("TRUNCATE TABLE exam")
        conncr.execute("SET FOREIGN_KEY_CHECKS=1")
    mydb.commit()

    conncr.execute(sql_command3)
    store3=conncr.fetchall()
    z3=list(store3[0])

    if(z3[0]==0):
        conncr.execute("SET FOREIGN_KEY_CHECKS=0")
        conncr.execute("TRUNCATE TABLE room")
        conncr.execute("SET FOREIGN_KEY_CHECKS=1")
    mydb.commit()

    conncr.execute(sql_command4)
    store4=conncr.fetchall()
    z4=list(store4[0])

    if(z4[0]==0):
        conncr.execute("SET FOREIGN_KEY_CHECKS=0")
        conncr.execute("TRUNCATE TABLE timetable")
        conncr.execute("SET FOREIGN_KEY_CHECKS=1")
    mydb.commit()

    mydb.close()