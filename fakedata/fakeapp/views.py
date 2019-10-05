from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Employee
import faker

# Create your views here.
f = faker.Faker()
def EmployeeList(request):
    for i in range(100):
        name = f.name()
        email = f.email()
        address = f.random_element(elements=('Hyderabad','Pune','Banglore','Odisha','Rajasthan','Delhi'))
        dob = f.date_time()
        salary = f.random_element(elements=(25000.50,45000.99,65000.76,11000.00,78000.19,35000.67))

        data = Employee(
            name = name,
            email = email,
            address = address,
            dob = dob,
            salary = salary,
            )
        data.save()
    return HttpResponse('Data Inserted Successfully...')

def DisplayList(request):
    e_data = get_list_or_404(Employee)
    return render(request,'display_list.html',{'e_data':e_data})
        
