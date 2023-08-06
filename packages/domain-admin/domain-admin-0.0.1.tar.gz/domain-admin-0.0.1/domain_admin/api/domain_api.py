# -*- coding: utf-8 -*-

from flask import request
from playhouse.shortcuts import model_to_dict

from domain_admin.model import DomainModel, GroupModel
from domain_admin.service import domain_service
from domain_admin.utils import datetime_util
from domain_admin.utils.flask_ext.app_exception import AppException
from domain_admin.utils.peewee_ext import model_util


def add_domain():
    """
    添加域名
    :return:
    """
    domain = request.json.get('domain')
    alias = request.json.get('alias', '')
    group_id = request.json.get('group_id', 0)

    if not domain:
        raise AppException('参数缺失：domain')

    row = domain_service.add_domain({
        'domain': domain,
        'alias': alias,
        'group_id': group_id,
    })

    return {'id': row.id}


def update_domain_by_id():
    """
    更新数据
    id domain alias group_id notify_status
    :return:
    """

    data = request.get_json(force=True)
    domain_id = data.pop('id')

    data['update_time'] = datetime_util.get_datetime()

    DomainModel.update(data).where(
        DomainModel.id == domain_id
    ).execute()


def delete_domain_by_id():
    """
    删除
    :return:
    """
    domain_id = request.json.get('id')

    DomainModel.delete_by_id(domain_id)


def get_domain_list():
    """
    获取域名列表
    :return:
    """
    page = request.json.get('page', 1)
    size = request.json.get('size', 10)
    group_id = request.json.get('group_id')

    query = DomainModel.select()

    if isinstance(group_id, int):
        query = query.where(DomainModel.group_id == group_id)

    lst = query.order_by(
        DomainModel.create_time.asc()
    ).paginate(page, size)

    total = DomainModel.select().count()

    # TODO: N+1 解决问题
    lst = list(map(lambda m: model_to_dict(
        model=m,
        exclude=[DomainModel.detail_raw],
        extra_attrs=[
            'total_days',
            'expire_days',
        ]
    ), lst))

    # append_field(lst, ['group'])

    # domain_service.domain_list_with_group(lst)
    lst = model_util.list_with_relation_one(lst, 'group', GroupModel)

    return {
        'list': lst,
        'total': total
    }


def get_domain_by_id():
    """
    获取
    :return:
    """
    domain_id = request.json['id']

    row = DomainModel.get_by_id(domain_id)

    return model_to_dict(
        model=row,
        exclude=[DomainModel.detail_raw],
        extra_attrs=[
            'total_days',
            'expire_days',
            'detail',
            'group',
        ]
    )


def update_all_domain_cert_info():
    """
    更新所有域名证书信息
    :return:
    """
    domain_service.update_all_domain_cert_info()


def update_domain_cert_info_by_id():
    """
    更新域名证书信息
    :return:
    """
    domain_id = request.json['id']

    row = DomainModel.get_by_id(domain_id)

    domain_service.update_domain_cert_info(row)


def send_domain_info_list_email():
    """
    发送域名证书信息到邮箱
    :return:
    """
    to_addresses = request.json['to_addresses']
    domain_service.send_domain_list_email(to_addresses)


def check_domain_cert():
    """
    检查域名证书信息
    :return:
    """
    # 先更新，再检查
    domain_service.update_all_domain_cert_info()

    domain_service.check_domain_cert()
