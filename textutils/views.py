# This is by view made by me
from django.http import HttpResponse
from django.shortcuts import render
#home
def index(request):	
	return render(request,'index.html')


#analyze
def analyze(request):
	djtext=request.POST.get('text','default')
	removepunc=request.POST.get('removepunc','off')
	fullcaps=request.POST.get('fullcaps','off')
	newlineremover=request.POST.get('newlineremover','off')
	space=request.POST.get('space','off')

	#condition
	if removepunc=="on":
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed=""
		for char in djtext:
			if char not in punctuations:
				analyzed=analyzed+char						
		dic={'pourpose':'Remove Puntuation','anlyzed_text':analyzed}
		djtext=analyzed
	if fullcaps=="on":
		analyzed=""
		for char in djtext:
			analyzed=analyzed+char.upper()
		dic={'pourpose':'Changed to Upper Case','anlyzed_text':analyzed}
		djtext=analyzed
	if newlineremover=="on":
		analyzed=""
		for char in djtext:
			if char !="\n" and char!="\r":
				analyzed=analyzed+char
		dic={'pourpose':'New Line Remove','anlyzed_text':analyzed}
		djtext=analyzed
	if space=="on":
		analyzed=""
		for index,char in enumerate(djtext):
			if not(djtext[index] == " " and djtext[index+1]==" "):
				analyzed = analyzed + char
		dic={'pourpose': 'Removed NewLines', 'anlyzed_text': analyzed}
		djtext=analyzed
	#Error			
	if(removepunc != "on" and newlineremover!="on" and space!="on" and fullcaps!="on"):
		return render(request,'error.html')
	return render(request, 'analyze.html',dic)