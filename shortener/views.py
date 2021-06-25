from shortener.serializers import SubmittedUrlsSerializer
from shortener.models import SubmittedUrls
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_urls(request):
    urls = SubmittedUrls.objects.filter(user=request.user)
    serializer = SubmittedUrlsSerializer(urls, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def generate_url(request):
    user = request.user
    serializer = SubmittedUrlsSerializer(
        data=request.data, context=user)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_original_url(request, link):
    try:
        urls = SubmittedUrls.objects.get(shorten_url=link)
        serializer = SubmittedUrlsSerializer(urls)
        return Response(serializer.data)
    except SubmittedUrls.DoesNotExist:
        return Response({'message': 'Link does not exist'}, status=status.HTTP_404_NOT_FOUND)
