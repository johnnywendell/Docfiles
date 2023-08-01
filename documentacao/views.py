from django.shortcuts import render
from .models import Departamento
from .forms import DepartamentoForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView

def dept_create(request):
    template_name = 'dept_create.html'
    dept_form = Departamento()
    objects = Departamento.objects.all()
    if request.method == 'POST' and request.POST.get('edit-form'):
        pk = request.POST.get('edit-form')
        dept = request.POST.get('main-dept')
        cod = request.POST.get('main-cod')
        Departamento.objects.filter(pk=pk).update(dept=dept,cod=cod)
        url = '#'
        return HttpResponseRedirect(url)
    elif request.method == 'POST':
        form=DepartamentoForm(request.POST, instance=dept_form, prefix='main')
        if form.is_valid():
            form=form.save()
            url='#'
            return HttpResponseRedirect(url)
    else:
        form=DepartamentoForm(instance=dept_form, prefix='main')
    context={'form':form,'objects_list': objects}
    return render(request, template_name, context)

class DepartamentoList(ListView):
    model = Departamento
    template_name = 'dept_list.html'
    context_object_name = 'objects_list'
    