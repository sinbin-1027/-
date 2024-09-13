from django.shortcuts import render

# render와 redirect의 차이
# render : 어떤 요청이 왔을 때 페이지를 띄워주겠다.
# redirect : 


# Create your views here.
def index(request):
    # 여기에 로직이 들어감
    return render(request, 'articles/index.html')