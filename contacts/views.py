from django.shortcuts import render, redirect
from .forms import ContactForm
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


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'contact_create.html', {'form': form})