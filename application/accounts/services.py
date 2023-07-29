
from .models import User
from django.db.models import Q


class ServiceUser():
    def create(self, data: dict):
        try:
            if User.objects.get(id=data['user_id']).is_admin:
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
                    user_data = User.objects.filter(Q(id=user_filter_id)).last()
                    return {
                        "id": user_data.id,
                        "email": user_data.email,
                        "username": user_data.username,
                        "is_admin": user_data.is_admin,
                        "is_staff": user_data.is_staff,
                    }
                else:

                    return [
                        {
                            "id": user_data.id,
                            "email": user_data.email,
                            "username": user_data.username,
                            "is_admin": user_data.is_admin,
                            "is_staff": user_data.is_staff,
                        } for user_data in User.objects.all()
                    ]
            else:
                raise Exception('Apenas usuarios admin podem listar usuarios')
        except Exception as error:
            raise Exception(f"Error on get user(s) {error}")

    def update(self, data: dict):
        try:
            if user := User.objects.get(id=data['user_id']):
                user.username = data.get('username', user.username)
                user.email = data.get('email', user.email)
                user.save()
            else:
                raise Exception(f"Usuario não encontrado {err}")
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
