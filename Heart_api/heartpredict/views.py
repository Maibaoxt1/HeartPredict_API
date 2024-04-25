from django.shortcuts import render

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets

# Create your views here.
from .models import info
from .serializers import InfoSerializer
import joblib # type: ignore
import numpy as np

class InfoViewSet(viewsets.ModelViewSet):
    model = info
    queryset = info.objects.all()
    serializer_class = InfoSerializer
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)

        input_data = serializer.validated_data

        # Biến đổi từ điển thành mảng NumPy
        input_data_array = np.array(list(input_data.values())).reshape(1, -1)

    
        try:
            model = joblib.load("./saved_model.joblib")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        prediction = model.predict(input_data_array)

        # Customize the response data as needed
        response_data = {
            'message': 'Successfully',
            'data': prediction
        }
        
        # Return the customized response
        return Response(response_data, status=status.HTTP_201_CREATED)