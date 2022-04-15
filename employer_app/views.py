from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def employee_list(request):
    modelget = Employee.objects.all()
    return render(request,'employee_register/employee_list.html',{'modelget':modelget})

def employee_form(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request,'employee_register/employee_form.html',{'form':form})
    else:
        request.method == 'POST'
        form =EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')
    

def employee_update(request, id):
    updateget= Employee.objects.get(pk=id)
    updateform = EmployeeForm(instance=updateget)
    if request.method == 'POST':
        updateform = EmployeeForm(request.POST, instance=updateget)
        if updateform.is_valid():
            updateform.save()
        return redirect('list')
    return render(request,'employee_register/employee_update.html',{'updateget':updateget, 'updateform':updateform })

def employee_delete(request,id):
    deleteget= Employee.objects.get(pk=id)
    deleteget.delete()
    return redirect ('/list')