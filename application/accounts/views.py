import logging
from webbrowser import get
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
from rest_framework.views import APIView
from .services import ServiceUser


logger = logging.getLogger(__name__)


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    swagger_schema = None
    service = ServiceUser()

    def post(self, request):
        try:
            request.data['user_id'] = int(request.user.id)  # add user in dict data
            result = self.service.create(request.data)

        except Exception as error:
            logger.error(f'UserView (post) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": result}, status=HTTP_201_CREATED)

    def get(self, request):
        try:
            user_filter_id = request.GET.get('user_id')
            result = self.service.get(user_request_id=int(request.user.id), user_filter_id=user_filter_id)

        except Exception as error:
            logger.error(f'UserView (post) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(
                {"message": f"Resultado da busca: {len(result) if type(result) == list else ''} usuarios encontrados",
                 "data": result},
                status=HTTP_200_OK)

    def put(self, request):
        try:
            request.data['user_id'] = int(
                request.user.id)  # add user in dict data
            result = self.service.update(request.data)

        except Exception as error:
            logger.error(f'UserView (put) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": result}, status=HTTP_202_ACCEPTED)

    def delete(self, request):
        try:
            user_request_id: int = int(request.user.id)
            user_id: int = int(request.data['user_id'])
            result = self.service.delete(user_request_id, user_id)
        except Exception as error:
            logger.error(f'UserView (put) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": result}, status=HTTP_202_ACCEPTED)
