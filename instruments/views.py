from django.shortcuts import render
from .models import Instrument

def instrument_list(request):
    instruments = Instrument.objects.all().order_by('-created_at')
    return render(request, 'instruments/list.html', {'instruments': instruments})
