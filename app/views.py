from django.shortcuts import render
from .models import Avtomobil
from django.views.generic import ListView
 
from .utils import searchProjects
from .utils import paginateProjects
 
 
 
def main(request):
    if request.method == "POST":
        search = request.POST['qidiruv']
        posts = Avtomobil.objects.filter(nomi__icontains=search)
        return render(request, 'blog/search.html', {"posts": posts})
    contex = {
        'main': Avtomobil.objects.all(),
        'all_avto': Avtomobil.objects.all(),
    }
    return render(request, 'blog/basic.html', contex)
 
 
class AvtoViews(ListView):
    model = Avtomobil
    context_object_name = 'all_avto'
    template_name = 'blog/avtolar.html'
    paginate_by = 8
 
 
def avto_haqida(request, id):
    avto = Avtomobil.objects.get(id=id)
 
    return render(request, 'blog/avto_batafsil.html', {"avto": avto})
 
 
# perpage uchun
def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)
 
    context = {'projects': projects,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'blog/avtolar.html', context)