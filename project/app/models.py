from django.db import models

gender_choices={
    ("Male","Male"),
    ("Female","Female"),
    ("Others","Others"),
}

class basic_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    firstname=models.CharField(max_length=100,null=True)
    lastname=models.CharField(max_length=100,null=True)
    DOB=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=20,choices=gender_choices,default='Female')
    mobile_number=models.CharField(max_length=100,null=True)
    email_address=models.CharField(max_length=100,null=True)

class education_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=100,null=True)
    institute=models.CharField(max_length=100,null=True)
    year=models.IntegerField(null=True)
    percent=models.IntegerField(null=True)
    
class experience_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    company=models.CharField(max_length=100,null=True)
    from_date=models.CharField(max_length=100,null=True)
    to_date=models.CharField(max_length=100,null=True)
    position=models.CharField(max_length=100,null=True)
    reason=models.CharField(max_length=100,null=True)

class other_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    father_name=models.CharField(max_length=100,null=True)
    mother_name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)
    aadhar_number=models.CharField(max_length=100,null=True)
    driving_license=models.CharField(max_length=100,null=True)
    emergency_contact_name=models.CharField(max_length=100,null=True)
    emergency_contact_number=models.CharField(max_length=100,null=True)

class designation_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    date_of_join=models.CharField(max_length=100,null=True)
    salary=models.CharField(max_length=100,null=True)

class salary_details(models.Model):
    employee_id=models.CharField(max_length=100,null=True)
    account_number=models.CharField(max_length=100,null=True)
    IFSC_code=models.CharField(max_length=100,null=True)
    bank_name=models.CharField(max_length=100,null=True)
    bank_address=models.CharField(max_length=100,null=True)




    


    