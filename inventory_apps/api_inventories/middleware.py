import logging
import time
from django.utils.deprecation import MiddlewareMixin
from rest_framework.views import APIView
from rest_framework.response import Response

# Get an instance of a logger for API request/response logging
logger = logging.getLogger('api_logger')

class DRFLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Log the incoming request
        request.start_time = time.time()  # Save the start time when the request is received
        logger.info(f"Request: {request.method} {request.path} - {request.body}")
        return None

    def process_response(self, request, response):
        # Calculate the response time based on the start time recorded in process_request
        if hasattr(request, 'start_time'):
            response_time = time.time() - request.start_time
        else:
            response_time = 0

        # Log the outgoing response
        logger.info(f"Response: {request.method} {request.path} - {response.status_code} - Time taken: {response_time:.4f}s")
        return response
