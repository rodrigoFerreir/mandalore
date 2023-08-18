from . import *


class ViewProduct(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.data['user_id'] = int(request.user.id)
            result = ServiceProduct(request.data).create()

        except Exception as error:
            logger.error(f'ViewEntity (post) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def get(self, request):
        try:
            request.data['user_id'] = int(request.user.id)
            result = ServiceProduct(request.data).get()
        except Exception as error:
            logger.error(f'ViewEntity (get) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def put(self, request):
        try:
            result = ServiceProduct(request.data).update()
        except Exception as error:
            logger.error(f'ViewEntity (put) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def delete(self, request):
        try:
            result = ServiceProduct().delete(id=int(request.query_params.get('id')))
        except Exception as error:
            logger.error(f'ViewEntity (delete) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": result}, status=HTTP_201_CREATED)
