from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    data_dict = {'access_records':webpages_list}
    my_dict = {'insert_me':'i am from views.py from app'}
    return render(request, 'firstapp/data.html', context=data_dict)
