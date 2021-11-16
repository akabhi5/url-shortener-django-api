from shortener.permissions import WriteOnly
from shortener.serializers import SubmittedUrlsSerializer
from shortener.models import SubmittedUrls
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class URLShortenerList(APIView):
    permission_classes = [WriteOnly | IsAuthenticated]

    def get(self, request):
        urls = SubmittedUrls.objects.filter(user=request.user)
        serializer = SubmittedUrlsSerializer(urls, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = SubmittedUrlsSerializer(
            data=request.data, context=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLShortenerDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, link):
        try:
            urls = SubmittedUrls.objects.get(shorten_url=link)
            serializer = SubmittedUrlsSerializer(urls)
            return Response(serializer.data)
        except SubmittedUrls.DoesNotExist:
            return Response({'message': 'Link does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, link):
        url = SubmittedUrls.objects.get(shorten_url=link)
        if request.user == url.user:
            url.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You are not authorized to delete this URL'})
