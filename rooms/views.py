from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.



def main_page(request):
    variables = RequestContext(request,{})
    return render_to_response('main_page.html', variables)
