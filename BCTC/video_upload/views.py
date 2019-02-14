from django.shortcuts import render
from django.http import HttpResponse
from .forms import DocumentForm 
import os

# Create your views here.
def index(request):
    print(request.method)
    if request.method == 'POST':
        #ping
        hostname = "10.30.126.35" 
        response = os.system("ping -c 1 " + hostname) # ping once at hostname
        
        #check ping response
        if response == 0:
            print(hostname, 'is up!')
        else:
            print(hostname, 'is down!')

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'video_upload/index.html') # placeholder for homepage/index      
    else:
        form = DocumentForm()
        return render(request, 'video_upload/index.html', {
            'form': form
        })

