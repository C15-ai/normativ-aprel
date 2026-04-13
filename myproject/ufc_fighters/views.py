from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Fighter
from .forms import FighterForm
from django.db.models import Q
from django.core.paginator import Paginator
def fighter_list(request):
    search = request.GET.get('search', '')
    page_number = request.GET.get('page')
    print(page_number)
    # print(search)
    fighter = Fighter.objects.filter()
    if search:
        fighter = fighter.filter(Q(name__icontains=search) | Q(nickname__icontains=search) | Q(weight_class__icontains=search))
    paginator = Paginator(fighter,3)

    fighter = paginator.get_page(page_number)

    return render(request, 'fighter/fighter_list.html',{'fighter':fighter , 'search' : search})



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
    return render(request, 'fighter/update_fighters.html',{'form':form, 'fighter':fighter , })

def fighter_update(request,pk=None):
    fighter = Fighter.objects.filter(id=pk).first()
    form = FighterForm(instance=fighter,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('fighter_list')
    return render(request, 'fighter/update_fighters.html',{'form':form, 'fighter':fighter})

def fighter_delete(request, pk=None):
    Fighter.objects.filter(id=pk).update(is_active=False)
    return redirect('fighter_list')



