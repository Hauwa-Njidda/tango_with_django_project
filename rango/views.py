from django.shortcuts import render
from django.http import HttpResponse 
from rango.models import Category
from rango.models import Page




def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list =Page.objects.order_by('-views')[:5]
    context_dict = {'blodmessage':'Crunchy, creamy, cookie, candy, cupcake!','categories':category_list,'pages':page_list}
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    return HttpResponse("Rango says here is the about page"+'<a href="/rango/">Index</a>')
def show_category(request,category_name_slug):
    context_dict ={}
    try:
        category = Category.objects.get(slug = category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages']=pages
        context_dict['category']=category
    except Category.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']=None
    return render(request, 'rango/category.html',context=context_dict)