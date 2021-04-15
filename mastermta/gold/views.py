from django.shortcuts import render
import mysql.connector
from mysql.connector import Error





def loginpage(request):
    context={}
    if request.method=="POST":
         
        username=request.POST["username"]
        password=request.POST["password"]
        
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='ali',
                                                 user='root',
                                                 password='')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM users where (pName='"+username+"' and pKey = '"+password+"');")


                record = cursor.fetchone()
                print("You're connected to database: ")

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                print("------------------------------------------------")
                if record:
                    print(record["pName"])
                    context=record

   
    return render(request,'loginpage.html',context)