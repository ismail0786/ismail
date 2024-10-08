# import necessary modules and packeges here
import re
import invalid_admissionnumber_exception as ia
from datetime import date

def read_file(file):
    # Write your code here
    obj= open(file, "r")
    f_data=obj.read().split("\n")
    data=[]
    for i in f_data:
        s=i.split(":")
        data.append(s)
     
    return data #TODO CHANGE THIS RETURN VALUE


def validate_admission_number(admission_number):
    try:
        # Write your code here
        
        #if admission_number.startswith("DECATHLON/") and admission_number[10: ].isdigit():
        #if re.match("^DECATHLON/\d\d\d\d$", academic_number):
        var=r'DECATHLON/\d{4}'
        result = re.search(var, admission_number)
        if result:
            return True #TODO CHANGE THIS RETURN VALUE
        else:
            raise ia.InvalidAdmissionNumberException("Invalid Admission Number")
    except ia.InvalidAdmissionNumberException as e:
        # Write your code here
        
        

        return e.message #TODO CHANGE THIS RETURN VALUE
    
def convert_date(str_date):
    # Write your code here
    y1,m1,d1=map(int, str_date.split("-"))
    date1=date(y1,m1,d1)
    
    
     
    return date1 #TODO CHANGE THIS RETURN VALUE
