from django.shortcuts import render

def blog_list(request):
    return render(request,'App_blog/blog_list.html', context={})
