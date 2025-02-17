from django.shortcuts import render
from .models import Visit


def track_visit(request):
    # Получаем или создаем запись о посещении
    visit, created = Visit.objects.get_or_create(id=1)  # Получаем первую запись
    visit.count += 1
    visit.save()

    # Отображаем количество посещений
    return render(request, 'tracker/visit.html', {'count': visit.count})
