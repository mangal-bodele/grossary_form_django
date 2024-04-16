from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import GrossaryForm
from .models import Grossary

@login_required(login_url='login_url')
def add_grossary(request):
    template_name = 'crud_app/add.html'
    form = GrossaryForm()
    if request.method == "POST":
        form = GrossaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_grossary(request):
    template_name = 'crud_app/show.html'
    grossarys = Grossary.objects.all()
    context = {'grossarys': grossarys}
    return render(request, template_name, context)


def update_grossary(request,pk):
    template_name = 'crud_app/add.html'
    obj=Grossary.objects.get(id=pk)
    form = GrossaryForm(instance=obj)
    if request.method == "POST":
        form = GrossaryForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_grossary(request,pk):
    template_name = 'crud_app/confirm.html'
    obj = Grossary.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
    return render(request, template_name)

