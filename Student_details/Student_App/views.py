from django.shortcuts import render
from django.http import JsonResponse
import json
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction
# Create your views here.

@csrf_exempt
def Student_details_add(request):
    if request.method == 'POST':
        try:
            js = json.loads(request.body)
            name = js["name"]
            roll_no = js["rollNo"]
            DOB = js["DOB"]
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO student_list_table (Name,Roll_No,DOB) VALUES (%s,%s,%s)",(name,roll_no,DOB))
                response = {"status":"success","message":"Details added successfully"}
                return JsonResponse(response)
        except Exception as e:
            response = {"status":"failure","message":str(e)}
            return JsonResponse(response)

@csrf_exempt
def Student_details_list(request):
    if request.method =="GET":
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM student_list_table")
                row = cursor.fetchall()
                List_details=[]
                for i in row:
                    res = {"StudentId":i[0],"StudentName":i[1],"StudentRollNo":i[2],"DOB":i[3]}
                    List_details.append(res)
                response = {"status":"success","List_details":List_details}
                return JsonResponse(response)

        except Exception as e:
            response = {"status":"failure","message":str(e)}
            return JsonResponse(response)


@csrf_exempt
def Student_mark_add(request,a):
    if request.method == 'POST':
        try:
            js = json.loads(request.body)
            std_id = a
            mark = js["mark"]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO student_mark_table (Student_id,Mark) VALUES (%s,%s)",(std_id,mark))
                response = {"status":"success","message":"Mark added successfully"}
                return JsonResponse(response)
        except Exception as e:
            response = {"status":"failure","message":str(e)}
            return JsonResponse(response)


@csrf_exempt
def Student_mark_data(request,a):
    if request.method =="GET":
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM student_mark_table where Student_id =%s",(a))
                row = cursor.fetchall()                
                cursor.execute("SELECT * FROM student_list_table where id =%s",a)
                row1=cursor.fetchall()                
                response = {"status":"success","StudentId":row[0][0],"Student_Name":row1[0][1],"Student_Roll_No":row1[0][2],"DOB":row1[0][3],"Mark":row[0][1]}
                return JsonResponse(response)

        except Exception as e:
            response = {"status":"failure","message":str(e)}
            return JsonResponse(response)


@csrf_exempt
def Student_result(request):
    if request.method =="GET":
        try:
            with connection.cursor() as cursor:
                # cursor.execute("SELECT * FROM student_mark_table")
                # row = cursor.fetchall() 
                # for i in row               
                cursor.execute("SELECT * FROM student_mark_table")
                row1=cursor.fetchall()  
                print(row1,"11111111111111111111")  
                A =[]
                B=[]
                C=[]
                D=[]
                E=[]
                F=[]            
                for i in row1:
                    print((i[1]),"3333333333333")
                    # i[1]=int(i[1])
                    if i[1] in range(91, 100):
                    
                        print("44444444444")
                        A.append(i[1])
                    elif i[1] in range(81, 90):
                    
                        B.append(i[1])
                    elif i[1] in range(71, 80):
                    
                        C.append(i[1])
                    elif i[1] in range(61, 70):
                    
                        D.append(i[1])
                    elif i[1] in range(55, 61):
                    
                        E.append(i[1])
                    else:
                        F.append(i[1])
                        
                response = {"status":"Success","Total no of students":len(row1),"No of student in A grade":len(A),"No of student in B grade":len(B),"No of student in C grade":len(C),"No of student in D grade":len(D),"No of student in E grade":len(E),"No of student in F grade":len(F),"Distinction":(len(A)/len(row1))*100,"First Class":((len(B)+len(C))/len(row1))*100,"Pass":((len(row1)-len(F))/len(row1))*100}
                print(A,"222222222222222222")
                return JsonResponse(response)

        except Exception as e:
            response = {"status":"failure","message":str(e)}
            return JsonResponse(response)


       


