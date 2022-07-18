from django.shortcuts import render
from .models import Post

# Dummy Data.
# posts = [
#     {
#         'author': 'Brandon',
#         'title': 'BLog Post 1',
#         'content': 'First Post content',
#         'date_posted': 'August 27, 2018',
#     },
#     {
#         'author': 'Brandon',
#         'title': 'BLog Post 2',
#         'content': 'First Post content',
#         'date_posted': 'August 27, 2018',
#     },
#     {
#         'author': 'Awan',
#         'title': 'BLog Post 2',
#         'content': 'First Post content',
#         'date_posted': 'August 27, 2018',
#     },
# ]
def home(request):
    context = {
        'posts':Post.objects.all()
    }
 
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
