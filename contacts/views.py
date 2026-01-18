import csv
import io

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import ContactForm
from .models import Contact, ContactStatus


def contact_list(request):
    query = request.GET.get("q")
    sort_by = request.GET.get("sort", "-created_at")

    contacts = Contact.objects.all()

    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
        )

    if sort_by in ["last_name", "-last_name", "created_at", "-created_at"]:
        contacts = contacts.order_by(sort_by)

    return render(
        request,
        "contact_list.html",
        {"contacts": contacts, "current_sort": sort_by, "query": query},
    )


def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()

    return render(request, "contact_create.html", {"form": form})


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)

    return render(
        request,
        "contact_edit.html",
        {"form": form, "contact": contact, "is_edit": True},
    )


@require_POST
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect("contact_list")


def import_contacts_csv(request):
    if request.method == "POST":
        csv_file = request.FILES.get("file")

        if not csv_file or not csv_file.name.endswith(".csv"):
            messages.error(request, "Please upload the correct file .csv")
            return redirect("contact_list")

        try:
            data_set = csv_file.read().decode("UTF-8")
            io_string = io.StringIO(data_set)
            next(io_string)

            for row in csv.reader(io_string, delimiter=",", quotechar='"'):
                # row: [first_name, last_name, phone, email, city, status_name]
                status_obj, _ = ContactStatus.objects.get_or_create(name=row[5])

                Contact.objects.update_or_create(
                    email=row[3],
                    defaults={
                        "first_name": row[0],
                        "last_name": row[1],
                        "phone_number": row[2],
                        "city": row[4],
                        "status": status_obj,
                    },
                )
            messages.success(request, "Import completed successfully!")
        except Exception as e:
            messages.error(request, f"Error while importing: {e}")

        return redirect("contact_list")

    return render(request, "import_form.html")
