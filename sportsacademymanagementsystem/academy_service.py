# # Please do not change the skelecton code given here
# # You can add any number of methods and attributes as you required without changing the given template

import student as stu
import utility as ut
import cx_Oracle

db=""
with open('database.properties') as f:
    lines = [line.strip().split("=") for line in f.readlines() if not line.startswith('#') and line.strip()]
    db = {key.strip(): value.strip() for key, value in lines}
   
#Creating Connection String
conn=cx_Oracle.connect(db['DB_USERNAME'],db['DB_PASSWORD'],db['DSN'])
cursor=conn.cursor()




class AcademyService:
    
    def __init__(self):
        self.__student_list=[]
        
    
    
    
    def build_student_details(self, stu_list):
        for i in stu_list:
            s=i.split(":")
            status= ut.validate_admission_number(s[0])
            if status==True:
                date1=ut.validate_admission_numbe




        
        
        
        
        return None  #TODO CHANGE THIS RETURN VALUE
    
    
        
    def add_student_details(self,stu_list):
        # Write your code here
        
        
        
        
        
        
        
        return None  #TODO CHANGE THIS RETURN VALUE
        
        

   
    def search_admission_number(self, admission_number):
        # Write your code here
        
        
        
        
        
        
        
        return True  #TODO CHANGE THIS RETURN VALUE
        
	
	
    def delete_student_details(self,age):
        
	    # Write your code here
        
        
        
        
       
        
        return None  #TODO CHANGE THIS RETURN VALUE
             
               
        
        
        
            
            
        
	    
	
