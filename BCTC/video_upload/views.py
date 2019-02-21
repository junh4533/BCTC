from django.shortcuts import render
from django.http import HttpResponse
import os
from django.views.generic import CreateView
from .forms import DocumentForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        #ping
        hostname = "10.30.126.35" #long shing's IP
        response = os.system("ping -c 1 " + hostname) # ping once at hostname
        
        #check ping response
        if response == 0:
            print(hostname, 'is up!')
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # return redirect('index')
                return render(request, 'video_upload/success.html')
        else:
            print(hostname, 'is down!')
            return HttpResponse("<h1>Selected TV is not online</h1>")       
    else:
        form = DocumentForm()
    return render(request, 'video_upload/index.html', {
        'form': form
    })

def video(request):
    return render(request, 'video_upload/video.html')
    # print('hello')





