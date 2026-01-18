from rest_framework import viewsets

from api.serializers import ContactSerializer
from contacts.models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

