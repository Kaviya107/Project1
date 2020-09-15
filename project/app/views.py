from django.shortcuts import render, redirect
from .models import*
from .forms import*

def home(request):
    return render(request,'view.html')


def role(request):
    return render(request,'role.html')


def forms(request,id=0):
    if (request.method=="GET"):
        if(id == 0):
            form=basic_details_form()
            form_1=others_form()
        else:
            id_value=basic_details.objects.get(id=id)
            id_value_1=other_details.objects.get(id=id)
            form=basic_details_form(instance = id_value)
            form_1=others_form(instance = id_value_1)
        return render(request,'forms.html',{"form":form,"form_1":form_1})
    else:
        if(id == 0):
            form=basic_details_form(request.POST)
            form_1=others_form(request.POST)
        else:
            id_value=basic_details.objects.get(id=id)
            id_value_1=other_details.objects.get(id=id)
            form=basic_details_form(request.POST,instance = id_value)
            form_1=others_form(request.POST,instance = id_value_1)
        if(form.is_valid()==True and form_1.is_valid()==True):
            form.save()
            form_1.save()
        all_data=basic_details.objects.all()
        all_data_1=other_details.objects.all()
        for i in range(1,(int(request.POST["totallength"]))+1):
            aa=education_details(qualification=request.POST["qualification"+str(i)],institute=request.POST["institute"+str(i)],year=request.POST["year"+str(i)],percent=request.POST["percent"+str(i)])
            aa.save()
        for i in range(1,(int(request.POST["totallength_1"]))+1):
            aa=experience_details(company=request.POST["company"+str(i)],from_date=request.POST["from_date"+str(i)],to_date=request.POST["to_date"+str(i)],position=request.POST["position"+str(i)],reason=request.POST["reason"+str(i)])
            aa.save()
        return redirect('/designation/')

def designation(request,id=0):
    if (request.method=="GET"):
        if(id == 0):
             form_2=designation_details_form()
             form_3=salary_details_form()
        else:
            id_value_2=designation_details.objects.get(id=id)
            id_value_3=salary_details.objects.get(id=id)
            form_2=designation_details_form(instance = id_value_2)
            form_3=salary_details_form(instance = id_value_3)
        return render(request,'designation.html',{"form_2":form_2,"form_3":form_3})
    else:
        if(id == 0):
             form_2=designation_details_form(request.POST)
             form_3=salary_details_form(request.POST)
        else:
            id_value_2=designation_details.objects.get(id=id)
            id_value_3=salary_details.objects.get(id=id)
            form_2=designation_details_form(request.POST,instance = id_value_2)
            form_3=salary_details_form(request.POST,instance = id_value_3)
        if(form_2.is_valid()==True and form_3.is_valid()==True):
            form_2.save()
            form_3.save()
        all_data_2=designation_details.objects.all()
        all_data_3=salary_details.objects.all()
        return render(request,'designation.html',{"form_2":form_2,"form_3":form_3,"designation_details":all_data_2,"salary_details":all_data_3})
        #return redirect('/role/')








