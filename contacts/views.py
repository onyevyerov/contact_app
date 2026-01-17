from django.shortcuts import render

from .models import Contact


def contact_list(request):
    sort_by = request.GET.get('sort', '-created_at')

    if sort_by not in ['last_name', '-last_name', 'created_at', '-created_at']:
        sort_by = '-created_at'

    contacts = Contact.objects.all().order_by(sort_by)

    return render(request, "contact_list.html", {
        'contacts': contacts,
        'current_sort': sort_by
    })
