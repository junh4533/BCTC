from django.shortcuts import render
from django.http import HttpResponse
import os
from django.views.generic import CreateView
from .forms import DocumentForm
from .models import Document
import time

# Create your views here.
def index(request):
    # if request.is_ajax():
    #     #do something
    #     request_data = request.POST
    #     print("ok")
    if request.method == 'GET':
        #ping
        hostname = "10.30.126.22" #long shing's IPv4
        hostname2 = "10.30.125.125"
        response = os.system("ping " + hostname +  " -n 1 -w 1") # ping once at hostname
        response2 = os.system("ping " + hostname2 +  " -n 1 -w 1") # ping once at hostname
        
        form = DocumentForm()
        args = {
            "form": form,
            "response": response,
            "response2": response2
        }
        return render(request, 'video_upload/index.html', args)
        # form = DocumentForm()
        # return render(request, 'video_upload/index.html', {
        #     'form': form
        # })
        
    if request.method == 'POST':
        #ping
        hostname = "10.30.124.80" #long shing's IPv4
        response = os.system("ping " + hostname +  " -n 1 -w 1") # ping once at hostname
        
        #check ping response
        if response == 0:
            print(hostname, 'is up!')
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid(): 
                form.save()
                return render(request, 'video_upload/success.html')
        else:
            print(hostname, 'is down!')
            return HttpResponse("<h1>Selected TV is not online</h1>")
    # else:
    #     form = DocumentForm()
    
# def index(request):
#     if request.method == 'POST':
#         form = Document()
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             tv == request.POST.get('TV1')
            
#             hostname = "10.30.126.35"
#             response = os.system("ping -c 1 " + hostname) #ping once

#             if response == 0:
#                 print(hostname, 'is up!')
#                 form.save()
#                 return render(request, 'video_upload/success.html')
#             else:
#                 print(hostname, 'is down!')
#                 return HttpResponse("<h1>Selected TV is not online</h1>")
#     else:
#         form = Document()
#     return render(request, 'video_upload/index.html',{
#         'form': form
#     })
            
def video1(request):
    return render(request, 'video_upload/video1.html')
    
def video2(request):
    return render(request, 'video_upload/video2.html')

def video3(request):
    return render(request, 'video_upload/video3.html')

def video4(request):
    return render(request, 'video_upload/video4.html')





