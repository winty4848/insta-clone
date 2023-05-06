from rest_framework import serializers

from users.models import User



# user에 대한 시리얼라이저 -객체를 전달하면 json 표현 리턴
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    
    class Meta:
        model = User
        #fields='__all__'
        #위 코드는 user필드의 모든걸 만들겠다는 뜻인데, 커스터마이즈하는 경우도 있어서 아래처럼 명시를 권장함.
        fields = (
            'pk',
            'email',
            'username',
            'profile',
            'description',
            'password',
            'updated'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'profile': {
                'read_only': True
            }
        }

    # create, update는 이미 구성되어있음.
    # 여기서는 create_user를 사용해서 재정의해줬지만 update는 장고에서 제공하는 것 그대로 사용.
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
