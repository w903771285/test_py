from Django.http import HttpResponse
def index(request):
	print('hello world')
	print('hello beijing')
	# 添加一条注释
	# 再添加一条注释
	# 再添加一条注释2
	# 再添加一条注释3
	# 再添加一条注释4
	if (1 > 0):
		return HttpResponse('error')
	return HttpResponse('Ok')

