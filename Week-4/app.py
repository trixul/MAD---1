from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('Agg')
import csv

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        return render_template('index.html')


    with open('data.csv', newline='') as csvfile:
            reader=csv.reader(csvfile)
    
            if request.method == 'POST':
                student_course = []
                course_marks = []

                select_id = request.form.get('ID')
                value_id = request.form.get('id_value')

                if select_id == 'student_id':
                    total=0
                    for row in reader:
                        if value_id in row[0]:
                            total+=int(row[2].strip())
                            student_course.append(row)
                    if student_course ==[]:
                        return render_template('wrong.html')
                    else:
                        return render_template('student data.html',student_course = student_course, total=total)
                
                elif select_id == "course_id":
                    for row in reader:
                        if value_id in row[1]:
                            course_marks.append(int(row[2].strip()))
                    if course_marks == []:
                        return render_template('wrong.html')
                    else:
                        Average_Marks=sum(course_marks)/len(course_marks)
                        Maximum_Marks=max(course_marks)
                        x = course_marks
                        plt.clf()
                        plt.hist(x)
                        plt.savefig('static/hist.png')
                        return render_template('course-data.html',Average_Marks=Average_Marks, Maximum_Marks=Maximum_Marks)




        
app.run(debug = False)