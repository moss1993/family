# file: example1.py
'''首页'''
from app import auth, login_manager
from flask import json, request, flash
from app.dbModel.dal.UserDal import UserDal
from flask_login import (LoginManager, login_required, login_user,
                            current_user, logout_user, UserMixin)
from app.dbModel.models.DB_UserModel import User
from app.core.model.AppReturnDTO import AppReturnDTO
from app.core.Fun import Fun
from app.core.model.LogingModel import LogingModel


@login_manager.user_loader
def load_user(user_id):
    ''' 获取用户信息 '''
    user = UserDal.SingleUser(user_id)
    return user

@auth.route('/token', methods=['GET', 'POST'])
def token():
    '''用户登录'''
    # user = User()
    # login_user(user)
    print(request.data)
    a = request.get_data()
    print(a)
    j_data =  json.loads(a) #-----load将字符串解析成json

    class MyClass(object):
        loginName="1"
        password=""
    myclass=MyClass()
    myclass.__dict__=j_data;

    print('JSON:')
    print(myclass.loginName)
    print(myclass.password)
    re_ent = AppReturnDTO(False, '登录超时')
    json_str = Fun.convert_to_dict(re_ent)
    re_str = json.dumps(json_str, ensure_ascii=False)
    return re_str

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    '''退出登录'''
    flash(u'You have been signed out')
    re_ent = AppReturnDTO(False, U'登录超时')
    return json.dumps(Fun.convert_to_dict(re_ent))

@auth.route('/UserLogin', methods=['GET', 'POST'])
def user_login():
    '''用户登录'''
    j_data = json.loads(request.get_data())#-----load将字符串解析成json
    (err, ent) = UserDal.UserLogin(j_data)
    if err.IsSuccess:
        return json.dumps(Fun.convert_to_dict(ent))
    else:
        return json.dumps(Fun.convert_to_dict(err))