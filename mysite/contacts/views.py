from django.shortcuts import render
from .models import Contacts
# Create your views here.
def contacts(request):
    contact = Contacts.objects.all()
    context = {
        'contacts': contact,
        'title': 'Список контактов'
    }

    return render(request, 'contacts/contacts.html', context)