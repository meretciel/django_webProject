from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.



def main_page(request):
    variables = RequestContext(request,{})
    return render_to_response('main_page.html', variables)


from .forms import SearchForm_Newport

def search_page_newport(request):
    # initialize variables

    form = None
    show_results = False
    list_results = None
    if request.method == 'POST':
        form = SearchForm_Newport(request.POST)
        if form.is_valid():
            show_results = True
            list_results = []
            for key, val in form.cleaned_data.items():
                list_results.append(val)
            print 'ok'

        else:
            #TODO: add a error flag
            print 'invalid form'
            form = SearchForm_Newport()
    else:
        form = SearchForm_Newport()


    variables = RequestContext(request, {
        'form': form,
        'list_results':  list_results,
        'show_results': show_results,
    })
    return render_to_response('search_newport.html', variables)
