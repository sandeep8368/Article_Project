from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.display_index, name='home'),
    path('allarticle/', views.display_articles, name='allart'),
    path('specarticle/<int:id>', views.spec_article, name = 'specific'),
]