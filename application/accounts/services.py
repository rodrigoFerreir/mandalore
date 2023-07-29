
from organization.models import Organization
from .models import User
from .serializers import UserSerializer, UpdateUserSerializer


class ServiceUser():
    def create(self, data: dict):
        try:
            if User.objects.get(id=data['user_id']).is_admin:
                Organization.objects.get()
                User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
            else:
                raise Exception('Apenas usuarios admin podem criar novos usuarios')
        except Exception as err:
            raise Exception(f"Error on create users {err}")
        else:
            return 'Novo usuario adicionado com sucesso!'

    def get(self, user_request_id: int, user_filter_id: int = None):
        try:
            if User.objects.get(id=user_request_id).is_admin:
                if user_filter_id:
                    user_data = User.objects.get(id=user_filter_id)
                    return UserSerializer(user_data)
                else:
                    user_data = User.objects.filter(is_active=True).order_by('id')
                    return UserSerializer(user_data, many=True)
            else:
                raise Exception('Apenas usuarios admin podem listar usuarios')
        except Exception as error:
            raise Exception(f"Error on get user(s) {error}")

    def update(self, data: dict):
        try:
            serializer = UpdateUserSerializer()
            if User.objects.get(id=data['user_id']).is_admin:  # request user login
                if user_instance := User.objects.get(id=data['id']):
                    serializer.update(instance=user_instance, validated_data=data)
                else:
                    raise Exception(f"Usuario não encontrado")
            else:
                raise Exception(f"Apenas usuarios admin podem criar novos usuarios")
        except Exception as err:
            raise Exception(f"Error on update user {err}")
        else:
            return 'Usuario atualizado com sucesso!'

    def delete(self, user_request_id: int, user_id: int):
        try:
            if User.objects.get(id=user_request_id).is_admin:
                user = User.objects.get(id=user_id)
                user.is_active = False
                user.save()
            else:
                raise Exception('Apenas usuarios admin podem deletar usuarios')
        except Exception as err:
            raise Exception(f"Error on delete users {err}")
        else:
            return 'Usuario atualizado com sucesso!'
