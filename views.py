from Django.http import HttpResponse
def index(request):
	print('hello world')
	print('hello beijing')
	# 添加一条注释
	# 再添加一条注释
	return HttpResponse('Ok')

