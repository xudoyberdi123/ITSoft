from collections import OrderedDict
from contextlib import closing

from django.db import connection

from ITUnisoft.settings import PER_PAGE
from base.db import dictfetchall, dictfetchone
from base.sqlpaginator import SqlPaginator


def get_list(requests, type, slug=None):
    try:
        page = int(requests.GET.get('page', 1))
    except:
        page = 1
    offset = (page - 1) * PER_PAGE

    if type == "project" and slug:
        sql = """
            select pro.* from sayt_project pro
            inner join sayt_category ctg on ctg.slug=%s 
            order by pro.id
            limit %s offset %s
        """
    else:
        sql = f"""
            select * from sayt_{type}
            order by id
            limit %s offset %s
        """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [PER_PAGE, offset])
        result = dictfetchall(cursor)

    with closing(connection.cursor()) as cursor:
        if type == "project" and slug:
            cursor.execute(f"select count(1) as cnt from sayt_{type} inner join sayt_category ctg on ctg.slug='{slug}'")
        else:
            cursor.execute(f"select count(1) as cnt from sayt_{type}")
        row = dictfetchone(cursor)

    if row:
        count_records = row.get('cnt', 0)
    else:
        count_records = 0

    paginator = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=count_records)
    pagging = paginator.get_paginated_response()
    return OrderedDict([
        ('items', result),
        ('meta', pagging)
    ])


def get_one(type, key, value):
    sql = f"select * from sayt_{type} where {key}=%s "

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [value])
        result = dictfetchone(cursor)
    return result


def get_services(requests):
    try:
        page = int(requests.GET.get('page', 1))
    except:
        page = 1
    offset = (page - 1) * PER_PAGE

    sql = f"""
    select ss.*, array_to_json(array_agg(row_to_json(ss2))) as uslug from sayt_services ss 
    left join sayt_servicesuslugi ss2 on ss2.service_id = ss.id
    group by ss.id
    order by ss.id
    limit %s offset %s
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [PER_PAGE, offset])
        result = dictfetchall(cursor)

    with closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(1) as cnt from sayt_services ")
        row = dictfetchone(cursor)

    if row:
        count_records = row.get('cnt', 0)
    else:
        count_records = 0

    paginator = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=count_records)
    pagging = paginator.get_paginated_response()
    return OrderedDict([
        ('items', result),
        ('meta', pagging)
    ])


def _format_servise(data):
    if data['uslug']:
        uslugi = [i['uslugi'] for i in data['uslug']]

    else:
        uslugi = None

    return OrderedDict([
        ('id', data['id']),
        ('title', data['title']),
        ('description', data['description']),
        ('img', data['img']),
        ('uslugi', uslugi)
    ])
