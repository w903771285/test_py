from Django.http import HttpResponse
def index(request):
	print('hello world')
	print('hello beijing')
	return HttpResponse('Ok')
