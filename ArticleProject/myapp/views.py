from django.shortcuts import render
from myapp.models import ArticleModel
# Create your views here.
def display_index(request):
    submitted = False
    if request.method == 'POST':
        submitted = True
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ArticleModel.objects.create(name = name, desc = desc)
        
    return render(request, 'html/index.html', {'submitted':submitted})


def display_articles(request):
    all_article = ArticleModel.objects.all()
    
    return render(request, 'html/display.html',{'data':all_article})


def spec_article(request,id):
    specific_data = ArticleModel.objects.get(id=id)
    print(specific_data.name)
    print(specific_data.desc)
    return render(request, 'html/specific.html',{'data':specific_data})