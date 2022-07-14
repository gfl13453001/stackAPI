#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/8


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    '''
    token验证
    '''
    def validate(self, attrs):
        data = super().validate(attrs)
        # print(data)

        refresh = self.get_token(self.user)
        # print(refresh.access_token)

        # data['refresh'] = str(refresh)
        data['token'] = str(refresh.access_token)
        data['id'] = self.user.id
        data['userInfo'] = {
            "username":self.user.username,
            "nickname":self.user.nickname,
            "phone":self.user.phone,
            "email":self.user.email,
            "isSuperuser":self.user.is_superuser,
            "isStaff":self.user.is_staff,
        }
        # data['username'] = self.user.username #这个是你的自定义返回的
        # data['user_id'] = self.user.id #这个是你的自定义返回的
        data.pop('refresh')
        data.pop('access')

        return data

