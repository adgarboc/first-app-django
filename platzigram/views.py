from django.http import HttpResponse, JsonResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')


def hi(request):
    # import pdb
    #  pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'data': sorted_numbers
    }
    return JsonResponse(data, safe=False)
