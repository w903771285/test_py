from Django.http import HttpResponse
def index(request):
	print('hello world')
	print('hello beijing')
	# 添加一条注释
	# 再添加一条注释
	# 添加一条注释2
	# 添加一条注释3f
	return HttpResponse('Ok')

