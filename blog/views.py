from django.shortcuts import render

posts = [
    {
        'author': 'Joseph Enoch',
        'title': 'Getting started with Django',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil dignissimos eum vero numquam optio aspernatur illum, blanditiis quas quaerat, a mollitia necessitatibus temporibus obcaecati soluta labore voluptate eveniet doloribus odio?',
        'date_posted': "June 3 2022"
    },
    {
        'author': 'Joseph Enoch',
        'title': 'Becoming an Advanced React Dev',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil dignissimos eum vero numquam optio aspernatur illum, blanditiis quas quaerat, a mollitia necessitatibus temporibus obcaecati soluta labore voluptate eveniet doloribus odio?',
        'date_posted': "June 30 2022"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})

# Create your views here.
