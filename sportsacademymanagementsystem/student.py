# Please do not change the skelecton code given here.
# Write your code only in the provided places alone


class Student:
    
    # Define the parameterized constructor here

    def __init__(self, admission_number, student_name, admission_date, sports_name, student_age):
        self.__admission_number=admission_number
        self.__student_name=student_name
        self.__admission_date=admission_date
        self.__sports_name=sports_name
        self.__student_age=student_age
        self.__academic_fee=0.0


        
    def get_admission_number(self):
        return self.__admission_number

    def set_admission_number(self, admission_number):
        self.__admission_number = admission_number

    def get_student_name(self):
        return self.__student_name

    def set_student_name(self, student_name):
        self.__student_name = student_name

    def get_admission_date(self):
        return self.__admission_date

    def set_admission_date(self, admission_date):
        self.__admission_date = admission_date

    def get_sports_name(self):
        return self.__sports_name

    def set_sports_name(self, sports_name):
        self.__sports_name = sports_name
        
    
    def get_student_age(self):
        return self.__student_age

    def set_student_age(self, student_age):
        self.__student_age = student_age

    def get_academic_fee(self):
        return self.__academic_fee

    def set_academic_fee(self, academic_fee):
        self.__academic_fee = academic_fee
    
    
    
    
    def calculate_academic_fee(self):
        # Write your code here
        if self.__student_age>=5 and self.__student_age<=10:
            if self.__sports_name=="Cricket":
                self.__academic_fee=5000
            if self.__sports_name=="Hockey":
                self.__academic_fee=6000
            if self.__sports_name=="Football":
                self.__academic_fee=5500
        else:
            if self.__sports_name=="Cricket":
                self.__academic_fee=7000
            if self.__sports_name=="Hockey":
                self.__academic_fee=8100
            if self.__sports_name=="Football":
                self.__academic_fee=8600
        #set_academic_fee(self, self.__academic_fee)
        #self.__academic_fee=self.__academic_fee 
        
        
        