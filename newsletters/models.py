from django.db import models


# credit Master Code Online
class NewsletterUsers(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
