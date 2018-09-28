from Django.http import HttpResponse
def index(request):
	print('hello world')
	print(test')
	return HttpResponse('Ok')
