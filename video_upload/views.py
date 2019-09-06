from django.shortcuts import render
from django.http import HttpResponse
import os
from django.views.generic import CreateView
from .forms import DocumentForm
from .models import Document
from django.contrib.auth.decorators import login_required
import time
import shutil
import subprocess


from remrunner import runner


# Create your views here.

def index(request):

    # hname = "10.30.124.80" #long shing 
    # username = "administrator"

    # r = runner.Runner(hname, username)

    # rval, stdout, stderr = r.run('C:/Users/Administrator/Desktop/python_script/test.py')#hello world script
    # if rval:
    #     print(stderr)
    # else:
    #     print(stdout)

    # r.close()

    hostname = "10.30.125.20" #long shing
    hostname2 = "10.30.125.125" #york
    hostname3 = "10.30.125.30" #ashley
    hostname4 = "0.0.0.0" #me

    if request.method == 'GET':
        #ping
        response = os.system("ping " + hostname +  " -n 1 -w 1") # ping once at hostname
        response2 = os.system("ping " + hostname2 +  " -n 1 -w 1")
        response3 = os.system("ping " + hostname3 +  " -n 1 -w 1")
        response4 = os.system("ping " + hostname4 +  " -n 1 -w 1")
        print(response, response2, response3, response4)
        form = DocumentForm()
        args = {
            "form": form,
            "response": response,
            "response2": response2,
            "response3": response3,
            "response4": response4
        }
        return render(request, 'video_upload/index.html', args)
        
    if request.method == 'POST':
        #only works for tv1
        #ping
        hostname = "10.30.124.80"
        response = os.system("ping " + hostname +  " -n 1 -w 1") # ping once at hostname
        print(response)
        
        #check ping response
        if response == 0:
            print(hostname, 'is up!')
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid(): 
                form.save()
                print("saved")
                src = r"C:/Users/Administrator/Desktop/Django Projects/BCTC/media/videos/TV1.mp4"
                dst = r"C:/Users/Administrator/Desktop/Django Projects/BCTC/media/RemoteVideos/TV1.mp4"
                shutil.copy(src, dst, follow_symlinks=True)
                print('moved')
                #src = r"C:/Users/Administrator/Desktop/Django Projects/BCTC/media/videos/TV1.mp4"
                #dst = r"C:/Users/Administrator/Desktop/Django Projects/BCTC/media/test/"
            return render(request, 'video_upload/success.html')
        else:
            print(hostname, 'is down!')
            return render(request, 'video_upload/failed.html')
    # else:
    #     form = DocumentForm()
            
def video1(request):
    return render(request, 'video_upload/video1.html')
    
def video2(request):
    return render(request, 'video_upload/video2.html')

def video3(request):
    return render(request, 'video_upload/video3.html')

def video4(request):
    return render(request, 'video_upload/video4.html')


