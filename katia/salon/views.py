# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Описаниеие салона')


# Страница со списком процедур
def salon_info(request):
    return HttpResponse('Краткое описание процедур')


# Страница с информацией о процедуре и запись на процедуру
def salon_turnos(request, pk):
    return HttpResponse(f'Подробное описание и запись на процедуру {pk}') 
