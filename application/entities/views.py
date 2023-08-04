import logging
from unittest import result
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
from rest_framework.views import APIView

from .services import ServiceOrganization


logger = logging.getLogger(__name__)


class OrganizationView(APIView):
    permission_classes = [IsAuthenticated]
    service = ServiceOrganization()

    def post(self, request):
        try:
            request.data['user_id'] = int(request.user.id)  # add user in dict data
            result = self.service.create(request.data)
        except Exception as error:
            logger.error(f'OrganizationView (post) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def get(self, request):
        try:
            request.data['user_id'] = int(request.user.id)  # add user in dict data
            result = self.service.get()
        except Exception as error:
            logger.error(f'OrganizationView (get) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def put(self, request):
        try:
            result = self.service.update(request.data)
        except Exception as error:
            logger.error(f'OrganizationView (put) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def delete(self, request):
        try:
            result = self.service.delete(id=int(request.query_params.get('organization')))
        except Exception as error:
            logger.error(f'OrganizationView (delete) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": result}, status=HTTP_201_CREATED)
