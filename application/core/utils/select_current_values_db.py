from django.db import connection


def get_current_user_database():
    with connection.cursor() as cursor:
        cursor.execute("SELECT current_user")
        row = cursor.fetchone()
    return row[0]


def get_current_date_time_database():
    with connection.cursor() as cursor:
        cursor.execute("SELECT localtimestamp")
        row = cursor.fetchone()
    return row[0]
