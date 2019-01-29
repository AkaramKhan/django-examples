from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def empform(request):
    form = forms.empform()

    if request.method == 'POST':
        form = forms.empform(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name: "+ form.cleaned_data['name'])
            print("Name: "+ form.cleaned_data['email'])
            print("Name: "+ form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form':form})
