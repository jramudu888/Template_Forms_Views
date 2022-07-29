from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
from django.views.generic import TemplateView,FormView
from app.forms import SchoolForm, StudentForm
from app.views import *
class Cbv_template(TemplateView):
    template_name='Cbv_template.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['name']='Ashu'
        #context['age']=2
        sf=StudentForm()
        context['sf']=sf
        return context
    def post(self,request):
        fd=StudentForm(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))


class Cbv_form(FormView):
    template_name='Cbv_form.html'
    form_class=StudentForm

    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))

class Cbv_SchoolForm(FormView):
    template_name='Cbv_SchoolForm.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('data is inserted ')
