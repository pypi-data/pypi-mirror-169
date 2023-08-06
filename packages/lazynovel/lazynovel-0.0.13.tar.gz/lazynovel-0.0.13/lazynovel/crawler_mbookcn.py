#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from lazysdk import lazyrequests


def get_user_role_list(
        token
):
    """
    获取子账号列表
    :param token:
    :return:
    """
    url = 'https://admin.mbookcn.com/prod-api/v3/open/mng/role/getUserRoleList'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Authorization": f"Bearer {token}",
        "Connection": "keep-alive",
        "Cookie": f"sidebarStatus=0; Admin-Token={token}",
        "Host": "admin.mbookcn.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        return_json=True
    )


def update_user_role_list(
        token,
        app_id
):
    """
    更新当前的子账号为目标账号
    :param token:
    :param app_id:
    :return:
    """
    url = 'https://admin.mbookcn.com/prod-api/v3/open/mng/role/updateUserRoleList'
    params = {
        'appId': app_id
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Authorization": f"Bearer {token}",
        "Connection": "keep-alive",
        "Cookie": f"sidebarStatus=0; Admin-Token={token}",
        "Host": "admin.mbookcn.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        params=params,
        return_json=True
    )


def make_scheduled_msg(
        token,

        msg_name: str,
        msg_type: int,
        text_content: str,
        send_time: int,

        picture_url: str = None,
        openid: str = "",
        graphic_title: str = None,
        graphic_text: str = None,
        description: str = None,
):
    """
    新建客服消息
    :param token:

    :param msg_name: 【必填】名称（标题）
    :param msg_type: 【必填】消息类型，0：文字消息，1：单条图文
    :param text_content: 消息正文（文字消息）
    :param send_time: 预约发送 时间，13位时间戳，默认时间戳*1000
    :param openid: 测试openid
    :param picture_url: 图片（地址）
    :param graphic_text: 消息正文（图文消息）
    :param description: 【非必填】消息描述（图文消息）
    :param graphic_title: 【非必填】标题（图文消息）

    :return:
    """
    url = 'https://admin.mbookcn.com/prod-api/v3/open/mng/scheduled-msg'
    data = {
        "msgType": msg_type,  # 消息类型，0：文字消息
        "msgName": msg_name,  # 名称（标题）
        "sendTime": send_time,  # 预约发送时间，13位时间戳，默认时间戳*1000
        "openid": openid,  # 测试openid
        "rule": {
            "sex": -1,
            "op": -1,
            "recharge": -1,
            "coinType": -1,
            "subStart": -1,
            "subEnd": -1,
            "prefer": -1,
            "coinAmount": -1,
            "isVip": -1,
            "times": []
        },  # 设置标签
        "sendCount": 0,
        "status": 0
    }
    if msg_type == 0:
        data['title'] = text_content  # 消息正文
    elif msg_type == 1:
        data['picture_url'] = picture_url
        data['url'] = graphic_text
        data['description'] = description
        data['title'] = graphic_title  # 标题
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Authorization": f"Bearer {token}",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": f"sidebarStatus=0; Admin-Token={token}",
        "Host": "admin.mbookcn.com",
        "Origin": "https://admin.mbookcn.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"
    }
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        headers=headers,
        data=data,
        return_json=True
    )


def get_scheduled_msg(
        token,
        current_page: int = 1,
        page_size: int = 10,
        page_type: int = 1

):
    """
    获取客服消息列表
    :param token:
    :param current_page:  # 当前页码
    :param page_size:  # 每页条数
    :param page_type:

    :return:
    """
    url = 'https://admin.mbookcn.com/prod-api/v3/open/mng/scheduled-msg/_mget'
    params = {
        "currentPage": current_page,
        "pageSize": page_size,
        "type": page_type
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Authorization": f"Bearer {token}",
        "Connection": "keep-alive",
        "Cookie": f"sidebarStatus=0; Admin-Token={token}",
        "Host": "admin.mbookcn.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        params=params,
        return_json=True
    )
