from rest_framework import serializers

from contacts.models import ContactStatus, Contact


class ContactStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactStatus
        fields = ["id", "name"]


class ContactSerializer(serializers.ModelSerializer):
    status = ContactStatusSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "city",
            "status",
            "created_at",
        ]
