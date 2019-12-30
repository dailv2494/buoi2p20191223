from django.shortcuts import render,HttpResponse
import json

def index(request):

    return render(request,'index1.html')
def test(request):
    return HttpResponse(json.dumps({'message':'Hello'}),content_type='application/json')
