from django.urls import path,include

from sales.views import (
    index
)
app_name = 'sales'
urlpatterns = [
    path('',index,name='index'),
]