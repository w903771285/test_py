from Django.http import HttpResponse
def index(request):
	print('hello world')
	return HttpResponse('Ok')
