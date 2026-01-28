from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Health check endpoint
@api_view(["GET"])
def health_check(request):
    return Response({
        "status": "ok",
        "message": "Backend is running"
    })

# Additional example view with authentication
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({
        "username": request.user.username,
        "email": request.user.email,
    })
