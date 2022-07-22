import pandas as pd
import os

def convertfiles():
    #C:\Users\Sagar\Projects\cra\media\excel\room_allocxl.xlsx
    read_file = pd.read_excel (r'media\excel\room_allocxl.xlsx')
    read_file.to_csv (r'media\excel\room.csv', index = None,header=True)
    read_file = pd.read_excel (r'media\excel\exam_list.xlsx')
    read_file.to_csv (r'media\excel\exam.csv', index = None,header=True)
    read_file = pd.read_excel (r'media\excel\student_list.xlsx')
    read_file.to_csv (r'media\excel\student.csv', index = None,header=True)
    read_file = pd.read_excel (r'media\excel\teacher_list.xlsx')
    read_file.to_csv (r'media\excel\teacher.csv', index = None,header=True)
    read_file = pd.read_excel (r'media\excel\ttimetable.xlsx')
    read_file.to_csv (r'media\excel\timetable.csv', index = None,header=True)
    # df = pd.DataFrame(pd.read_csv(r"C:\Users\Sagar\Projects\cra\media\excel\timetable.csv"))
    # print(df)