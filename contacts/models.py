from django.db import models


class ContactStatus(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Statuses"


class Contact(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(null=True, unique=True)
    city = models.CharField(max_length=55)
    status = models.ForeignKey(
        ContactStatus, on_delete=models.PROTECT, related_name="contacts"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"

    class Meta:
        ordering = ["-created_at"]
