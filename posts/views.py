from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]


# Create your views here.
def list_posts(request):
    content = []
    for post in posts:
        content.append(f'<p><strong>{post["name"]}</strong></p>'
                       f'<p><small>{post["user"]} - <i>{post["timestamp"]}</i></small></p>'
                       f'<figure><img src="{post["picture"]}"/></figure>')
    return HttpResponse('<br>'.join(content))
