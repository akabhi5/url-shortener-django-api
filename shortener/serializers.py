from shortener.utils import generate_short_link
from shortener.models import SubmittedUrls
from rest_framework import serializers


class SubmittedUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedUrls
        fields = '__all__'

    def create(self, validated_data):
        user = None if self.context.is_anonymous else self.context
        while generated_url := generate_short_link():
            if not SubmittedUrls.objects.filter(shorten_url=generated_url).exists():
                break
        return SubmittedUrls.objects.create(shorten_url=generated_url, user=user, **validated_data)
