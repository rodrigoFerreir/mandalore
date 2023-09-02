from . import *


class ViewOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.data['user_id'] = int(request.user.id)
            result = ServiceOrder(request.data).create()

        except Exception as error:
            logger.error(f'ViewOrder (post) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def get(self, request):
        try:
            request.data['user_id'] = int(request.user.id)
            result = ServiceOrder(request.data).get()
        except Exception as error:
            logger.error(f'ViewOrder (get) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def put(self, request):
        try:
            request.data['order_id'] = request.data['id']
            result = ServiceOrder(request.data).update()
        except Exception as error:
            logger.error(f'ViewOrder (put) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"data": result}, status=HTTP_201_CREATED)

    def delete(self, request):
        try:
            result = ServiceOrder(request.data).delete(id=int(request.query_params.get('id')))
        except Exception as error:
            logger.error(f'ViewOrder (delete) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": result}, status=HTTP_201_CREATED)



class ViewAddItemToOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.data['order_id'] = int(request.query_params.get('order_id'))
            result = ServiceOrder(request.data).add_item()
        except Exception as error:
            logger.error(f'ViewOrder (delete) error {error}')
            return Response({"message": f"{error}"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": result}, status=HTTP_201_CREATED)