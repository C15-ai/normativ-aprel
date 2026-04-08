from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Fighter
from .forms import FighterForm

def fighter_list(request):
    fighter = Fighter.objects.all()
    return render(request, 'fighter/fighter_list.html',{'fighter':fighter})

# def fighter_create_form(request):
#     form = FighterForm()
#     return render(request,'fighter/create_fighters',{'form':form})
def fighter_create(request):
    if request.method == "POST":
        form = FighterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fighter_list')
    else:
        form = FighterForm()
    return render(request, 'fighter/create_fighters.html', {'form': form})
def fighter_update_form(request,pk=None):
    fighter = Fighter.objects.filter(id=pk).first()
    form = FighterForm(instance=fighter)
    return render(request, 'fighter/update_fighters.html',{'form':form, 'fighter':fighter})

def fighter_update(request,pk=None):
    fighter = Fighter.objects.filter(id=pk).first()
    form = FighterForm(instance=fighter,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('fighter_list')
    return render(request, 'fighter/update_fighters.html',{'form':form, 'fighter':fighter})

def fighter_delete(request, pk=None):
    Fighter.objects.filter(id=pk).delete()
    return redirect('fighter_list')



