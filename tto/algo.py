import pypyodbc as odbc
import pandas as pd
import mysql.connector
import numpy as np

def allocalgo():

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cra",
    )

    conncr = mydb.cursor()

    conncr.execute("SELECT * FROM room")

    df = conncr.fetchall()

    rd = np.array(df)

    records = rd.tolist()


    conncr.execute("SELECT * FROM exam")

    df1 = conncr.fetchall()

    rd1 = np.array(df1)

    records1 = rd1.tolist()


    conncr.execute("SELECT * FROM student")

    df2 = conncr.fetchall()

    rd2 = np.array(df2)

    records2 = rd2.tolist()

    conncr.execute("SELECT * FROM invigilator")

    df3 = conncr.fetchall()

    rd3 = np.array(df3)

    records3 = rd3.tolist()

    conncr.execute("SELECT * FROM timetable")

    df4 = conncr.fetchall()

    rd4 = np.array(df4)

    records4 = rd4.tolist()


    # for i in range(len(records1)):
    #     for j in range(len(records1[0])):
    #         print(records1[i][j],end=' ')
    #     print()


    uni=set()
    for i in range(len(records2)):
        uni.add(records2[i][1])
    nus=len(uni)

    allocated=[]
    mi=0
    # print(records3)
    for k2 in range(len(records1)):
        vis=[False]*len(records2)
        ct=0
        f=0
        for i in range(len(records)):
            if(records[i][2]=="YES" or records[i][2]=='1'):
                z=int(records[i][1])//nus
                for k in range(len(records3)):
                    mi=int(records3[0][2])
                    for k3 in range(len(records3)):
                        mi=min(mi,int(records3[k3][2]))
                    if int(records3[k][2])!=mi:
                        continue
                    for k1 in range(len(records4)):
                        if records3[k][0]==records4[k1][3] :
                            if records4[k1][1]==records1[k2][3] and records4[k1][2]==records1[k2][2]:
                                records3[k][2]=str(int(records3[k][2])+1)
                                sem={}
                                for j in range(len(records2)):
                                    if vis[j] == True :
                                        continue
                                    if records2[j][1] not in sem:
                                        sem[records2[j][1]]=1
                                    if sem[records2[j][1]]<=z:
                                        vis[j]=True
                                        sem[records2[j][1]]=sem[records2[j][1]]+1
                                        ct=ct+1
                                        #print(records3[k][2])
                                        temp=[]
                                        temp.append(records3[k][0])
                                        temp.append(records2[j][0])
                                        temp.append(records[i][0])
                                        temp.append(records1[k2][0])
                                        allocated.append(temp)
                                if(ct>=1):
                                    break
                    if(ct>=1):
                        break
            if(ct==len(records2)):
                break


    # for i in range(len(allocated)):
    #     for j in range(len(allocated[0])):
    #         print(allocated[i][j],end=' ')
    #     print()

    # print(len(allocated))


    sql_insert = '''
        INSERT INTO allocated(ID,USN,Room_no,Course_no)
        VALUES (%s,%s,%s,%s)
    '''

    sql_insert1 = '''
        INSERT INTO invigilator(ID,Email,Invigilation_count,Name)
        VALUES (%s,%s,%s,%s)
    '''

    conncr.execute("SET FOREIGN_KEY_CHECKS=0")

    conncr.execute("TRUNCATE TABLE invigilator")
    conncr.executemany(sql_insert1, records3)
    mydb.commit()

    conncr.execute("TRUNCATE TABLE allocated")
    conncr.executemany(sql_insert, allocated)
    mydb.commit()

    conncr.execute("SET FOREIGN_KEY_CHECKS=1")

    mydb.close()