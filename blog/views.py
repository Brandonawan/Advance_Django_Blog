from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'COreyMs',
        'title': 'BLog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'Brandon',
        'title': 'BLog Post 2',
        'content': 'First Post content',
        'date_posted': 'August 27, 2018',
    },
]
def home(request):
    context = {
        'posts':posts
    }
 
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
