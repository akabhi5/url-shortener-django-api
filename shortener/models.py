from django.db import models
from django.contrib.auth import get_user_model


class SubmittedUrls(models.Model):
    original_url = models.TextField()
    shorten_url = models.CharField(max_length=1024, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.shorten_url

    class Meta:
        ordering = ["created_on"]
        verbose_name_plural = "Submitted Urls"
        db_table = 'submitted_urls'
