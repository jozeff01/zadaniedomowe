from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hit
from .serializers import HitSerializer
from django.shortcuts import get_object_or_404


def root_view(request):
    return render(request, 'index.html')



class HitListCreateView(APIView):
    def get(self, request):
        hits = Hit.objects.all().order_by('-created_at')[:20]  
        serializer = HitSerializer(hits, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class HitDetailView(APIView):
    def get(self, request, title_url):
        hit = get_object_or_404(Hit, title_url=title_url)
        serializer = HitSerializer(hit)
        return Response(serializer.data)

    def put(self, request, title_url):
        hit = get_object_or_404(Hit, title_url=title_url)
        serializer = HitSerializer(hit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, title_url):
        hit = get_object_or_404(Hit, title_url=title_url)
        hit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)