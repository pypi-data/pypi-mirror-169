# encoding: utf-8
"""
@project: djangoModel->group_api
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 分组api
@created_time: 2022/9/5 11:48
"""
from rest_framework.views import APIView

from xj_user.services.user_service import UserService
from ..services.group_service import GroupService, GroupTreeService
from ..utils.custom_response import util_response
from ..utils.model_handle import parse_data


class GroupAPIView(APIView):
    def get_user_from_list(self, *args, **kwargs):
        params = parse_data(self)
        group_id = params.get("user_group_id") or kwargs.get("user_group_id") or 0
        if not group_id:
            return util_response(err=1000, msg="user_group_id 必传")
        data, err = GroupService.get_user_from_group(group_id)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def tree(self, **kwargs):
        params = parse_data(self)
        token = self.META.get('HTTP_AUTHORIZATION', None)
        token_srv, error_text = UserService.check_token(token)
        if error_text:
            return util_response(err=1000, msg=error_text)
        user_group_id = params.get("user_group_id") or kwargs.get("user_group_id") or 0
        data, err = GroupTreeService.group_tree(user_group_id)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    # 分组树 ==> 角色列表
    def group_tree_role(self):
        params = parse_data(self)
        data, err = GroupService.group_tree_role(params)
        return util_response(data=data)

    # 分组树 ==> 用户列表
    def group_tree_user(self):
        params = parse_data(self)
        data, err = GroupService.group_tree_user(params)
        return util_response(data=data)

    def group_user_list(self):
        group_id = self.GET.get("group_id", None)
        page = self.GET.get("page", 1)
        size = self.GET.get("size", 10)
        data, err = GroupService.group_user_list(group_id, page, size)
        if err:
            return util_response(err=2000, msg=err)
        return util_response(data=data)

    def group_user_detail(self):
        user_id = self.GET.get("user_id", None)
        data, err = GroupService.group_user_detail(user_id)
        if err:
            return util_response(err=2000, msg=err)
        return util_response(data=data)

    def group_user_add(self):
        data, err = GroupService.group_user_add(self.POST)
        if err:
            return util_response(err=2000, msg=err)
        return util_response(data=data)

    def list(self, **kwargs):
        # 用户组 列表接口
        params = parse_data(self)
        data, err = GroupService.group_list(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def put(self, request, **kwargs):
        # 用户组 修改接口
        params = parse_data(request)
        params.setdefault("id", kwargs.get("user_group_id", None))
        data, err = GroupService.edit_group(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def post(self, request, **kwargs):
        # 用户组 添加接口
        params = parse_data(request)
        data, err = GroupService.add_group(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    def delete(self, request, **kwargs):
        # 用户组 删除接口
        id = parse_data(request).get("id", None) or kwargs.get("user_group_id")
        if not id:
            return util_response(err=1000, msg="id 必传")
        data, err = GroupService.del_group(id)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    def bind_user_group(self, **kwargs):
        # 用户组 修改接口
        user_id = self.POST.get("user_id", None)
        group_list = self.POST.get("group_list", None)
        data, err = GroupService.bind_user_group(user_id, group_list)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
