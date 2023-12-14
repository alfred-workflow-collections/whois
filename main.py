#! /bin/python3
# -*- coding: utf-8 -*-

import sys
import whois
import json
import socket


def get_whois_info(domains):
    domain = whois.query(domains)
    name = domain.name
    registrar = domain.registrar
    registrant = domain.registrant
    emails = ";".join(domain.emails)
    creation = domain.creation_date.strftime("%Y年%m月%d %H:%M:%S")
    expiration = domain.expiration_date.strftime("%Y年%m月%d %H:%M:%S")
    ip = socket.gethostbyname(domains)

    items = [{
        "title": name,
        "subtitle": "一级域名",
        "arg": name,
        'icon': {'path': 'www.png'},
        "valid": "True"
    }, {
        "title": registrar,
        "subtitle": "域名代理商",
        "arg": registrar,
        'icon': {'path': 'www-2.png'},
        "valid": "True"
    }, {
        "title": registrant or "********",
        "subtitle": "域名申请人",
        "arg": registrant or "********",
        'icon': {'path': 'people.png'},
        "valid": "True"
    }, {
        "title": emails or "********",
        "subtitle": "域名申请人邮箱",
        "arg": emails or "********",
        'icon': {'path': 'email.png'},
        "valid": "True"
    }, {
        "title": creation,
        "subtitle": "域名申请时间",
        "arg": creation,
        'icon': {'path': 'time.png'},
        "valid": "True"
    }, {
        "title": expiration,
        "subtitle": "域名到期时间",
        "arg": expiration,
        'icon': {'path': 'tixing.png'},
        "valid": "True"
    }, {
        "title": ip,
        "subtitle": "域名解析的地址",
        "arg": ip,
        'icon': {'path': 'IP.png'},
        "valid": "True"
    }
    ]

    return json.dumps({'items': items})


def exit_error(domains):
    items = [{
        "title": "域名类型错误",
        "subtitle": domains,
        "arg": '',
        'icon': {'path': 'error.png'},
        "valid": "True"
    }]

    return json.dumps({'items': items})


if __name__ == '__main__':
    query = sys.argv[1]
    try:
        res = get_whois_info(query)
        print(res)
    except:
        res = exit_error(query)
        print(res)
