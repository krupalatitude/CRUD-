from django.shortcuts import render, redirect
from .models import EmployeeData


# Create your views here.



def IndexView(request):
    if request.method=='POST':
        model = EmployeeData()
        model.emp_name = request.POST['emp_name']
        model.emp_address = request.POST['emp_address']
        model.emp_salary = request.POST['emp_salary']
        model.save() 
        return redirect('index')   
    else:
        data = EmployeeData.objects.all()
        context = {
            'data' : data
        }
        return render(request,'index.html', context)

def DeleteView(request, id):
    data = EmployeeData.objects.get(id = id)
    data.delete()
    return redirect('index')

def EditView(request, id):
    data = EmployeeData.objects.get(id = id)
    if request.method=='POST':
        data.emp_name = request.POST['emp_name']
        data.emp_address = request.POST['emp_address']
        data.emp_salary = request.POST['emp_salary']
        data.save()  
        return redirect('index')  
    context = {
        'data' : data
    }
    return render(request, 'edit.html', context)

