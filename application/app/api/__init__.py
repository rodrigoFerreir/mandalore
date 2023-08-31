import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
from rest_framework.views import APIView

from app.services import ServiceEntity, ServiceProduct, ServiceOrder


logger = logging.getLogger(__name__)
