from django.http import JsonResponse


def test(request):
    return JsonResponse({'status':1})
