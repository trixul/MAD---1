from jinja2 import Template
import csv
import matplotlib.pyplot as plt
import sys

def max_marks(L):
    maximum = 0
    for i in range(len(L)):
        if int(L[i]) > maximum:
            maximum = int(L[i])
    return(maximum)

def average(L):
    avg = 0
    total = 0
    for i in range(len(L)):
        total += int(L[i])
    avg = total/(len(L)) 
    return avg






with open('data.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    student_details = [ ]
    course_marks = [ ]
    input_list = sys.argv 
    print(input_list)  
    total = 0
    AVG = 0
    M_MARKS = 0
    if input_list[1] == "-s":
        for row in reader:
            if input_list[2] == row[0].strip():
                total += int(row[2].strip())
                student_details.append(row)
        print(student_details)
    


        if student_details == []:
            data = """ <h1> Wrong Inputs </h1>
                <p> Something went wrong </p>
            """
            File = open("output.html","w")
            File.write(data)
            File.close()


        else:
            text = """
            <h1> Student Details </h1>
                <table border = "2"> 
                <tr>
                    <th> Student id </th>
                    <th> Course id </th>
                    <th> Marks </th>
                </tr>
                {% for row in student_details %}
                <tr>
                    <td>{{row[0].strip()}} </td>
                    <td>{{row[1].strip()}} </td>
                    <td>{{row[2].strip()}} </td>
                </tr>
                {%endfor%}
                <tr> 
                    <td colspan = "2"> Total Marks </td>
                    <td> {{total}} </td> 
                </tr>
                </table>
            """
            temp = Template(text)
            output2 = temp.render(total = total, student_details = student_details)
            File = open("output.html", "w")
            File.write(output2)
            File.close()
    else:
        if input_list[1] == "-c":
            for row in reader:
                if input_list[2] == row[1].strip():
                    course_marks.append(row[2])
            print(course_marks)
            
            if course_marks == []:
                data = """ <h1> Wrong Inputs </h1>
                <p> Something went wrong </p>
                """
                File = open("output.html","w")
                File.write(data)
                File.close()
            
            else: 
                AVG = average(course_marks)
                M_MARKS = max_marks(course_marks)

                text2 = """
                        <h1> Course Details </h1>
                        <table border = "2">
                            <tr>
                                <th> Average Marks </th>
                                <th> Maximum Marks </th>
                            </tr>
                            <tr>
                                <td>{{AVG}} </td>
                                <td>{{M_MARKS}} </td>
                            </tr>
                        </table>
                        <img src = "hist.png">

                        """
                plt.hist(course_marks)
                plt.savefig('hist.png')

                temp2 = Template(text2)
                output3 = temp2.render(AVG=AVG,M_MARKS=M_MARKS)
                File = open("output.html","w")
                File.write(output3)
                File.close()

        



        






