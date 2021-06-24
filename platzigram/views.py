from django.http import HttpResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')


def hi(request):
    # import pdb
    #  pdb.set_trace()
    numbers = request.GET['numbers']
    return HttpResponse(numbers)
