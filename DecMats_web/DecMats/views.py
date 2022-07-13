from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

# from .helper import Helper
from .models import Decmats
from .forms import InputForm

from django.core.exceptions import ValidationError
import django.core.validators as val
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from django.views.decorators.cache import cache_control
from .utils import Queries



# @cache_control(no_cache=True, no_store=True, max_age=0)
def index(request):
    
    # cache.clear()
    form = InputForm(request.GET)


    context = {'form': form}
    return render(request, 'DecMats/index.html', context)

class OutputView(View):
    form = InputForm

    type = ''
    n = ''
    d = ''

    def input_format(self,input_list):
        input_values = []
        
        for i in input_list:
            val = i.split(': ')
            input_values.append(val[1])
        
        
        return input_values

    def output(self, request): 
        
        self.type = request.GET.get('type')
        self.n = request.GET.get('n')
        self.d = request.GET.get('d')

        query = Queries()

        output_decmat = query.decmats_query(self.type, self.n, self.d)

        input_list = ['type: ' + str(self.type),'n: ' + str(self.n), 'd: '+ str(self.d)]


        context = {'input_list': input_list, 'queryset': output_decmat }

        return render(request, 'DecMats/output.html',context)

    def get(self, request):
        return self.output(request)