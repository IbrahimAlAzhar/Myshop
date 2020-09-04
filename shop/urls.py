from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.product_list,name='product_list'),
    # here slug is category_slug which came form views function through the parameter
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'), # filtering products by category
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'), # here came id and slug from detail function of views file


]

'''
# u can also making the url path using regular expression
urlpatterns = [
     url(r'^$', views.product_list,name='product_list) # here r means regular expression and ^ means start symbol and $ means end symbol.
     url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
     url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]

'''