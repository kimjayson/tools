# -*- coding: utf-8 -*-

import calendar
import datetime,time
import re


ISOTIMEFORMAT = {
    0 : '%Y-%m-%d %X',
    1 : '%Y-%m-%d',
    2 : '%Y年%m月%d日',
    3 : '%Y/%m/%d'
}

def timestamp_to_date(timestamp, mode = 0):
    try:
        # one
        struct_time = time.localtime(timestamp)

        if mode in ISOTIMEFORMAT.keys():
            date = time.strftime(ISOTIMEFORMAT[mode], struct_time)
            return date
        else:
            return ''

        # # two
        # date_time = datetime.datetime.fromtimestamp(timestamp)
        # date = date_time.strftime("%Y年%m月%d日")
        #
        # # three
        # date = "{:%Y-%m-%d %X}".format(date_time)
        # date = "{:%Y-%m-%d}".format(date_time)
        # date = "{:%Y年%m月%d日}".format(date_time)

    except Exception as err:
        return ''


def date_to_timestamp(date):
    try:
        if re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date):
            mode = 0
        elif re.search(r'^\d{4}-\d{2}-\d{2}$', date):
            mode = 1
        elif re.search(r'^\d{4}年\d{2}月\d{2}日$', date):
            mode = 2
        elif re.search(r'^\d{4}/\d{2}/\d{2}$', date):
            mode = 3
        else:
            return ''

        # datetime.datetime.strptime(date, ISOTIMEFORMAT[mode])

        struct_time = time.strptime(date, ISOTIMEFORMAT[mode])
        timestamp = int(time.mktime(struct_time))

        return timestamp
    except Exception as err:
        return ''


def get_today():
    """获取今天0点时间戳"""
    today_s = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    timestamp = int(time.mktime(today_s.timetuple()))
    return timestamp


def get_someday_timestamp(delta = 0):
    """获取某天0点-24点时间戳"""
    delta = datetime.timedelta(days = delta)
    someday_s = datetime.datetime.combine(datetime.date.today() + delta, datetime.time.min)
    s = int(time.mktime(someday_s.timetuple()))
    return s


def get_today_tuple():
    """获取今天0点时间戳"""
    today_s = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_e = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    s = int(time.mktime(today_s.timetuple()))
    e = int(time.mktime(today_e.timetuple()))
    return s,e


def get_someday_timestamp_tuple(delta = 0):
    """获取某天0点-24点时间戳"""
    delta = datetime.timedelta(days = delta)
    yest_s = datetime.datetime.combine(datetime.date.today() + delta, datetime.time.min)
    yest_e = datetime.datetime.combine(datetime.date.today() + delta, datetime.time.max)
    s = int(time.mktime(yest_s.timetuple()))
    e = int(time.mktime(yest_e.timetuple()))
    return s,e



'''日期list转换成时间戳list'''
def given_time_list(date, need_title = True):
    timeCondition = []
    for i in date:
        st = date_to_timestamp(i)
        et = st + 86400 - 1
        if need_title:
            timeCondition.append((i, st, et))
        else:
            timeCondition.append((st, et))
    return timeCondition


'''给定起始日期,返回每天时间戳'''
def times_list(s, e):
    st = date_to_timestamp(s)
    et = date_to_timestamp(e)
    times = []
    while st <= et:
        day = time.strftime("%Y-%m-%d", time.localtime(st))
        times.append([day, st, st + 86400 - 1])
        st += 86400
    return times


def date_diff(date1,date2):
    try:
        if re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', date1):
            mode = 0
        elif re.search(r'^\d{4}-\d{2}-\d{2}$', date1):
            mode = 1
        elif re.search(r'^\d{4}年\d{2}月\d{2}日$', date1):
            mode = 2
        elif re.search(r'^\d{4}/\d{2}/\d{2}$', date1):
            mode = 3
        else:
            return ''

        dt1 = datetime.datetime.strptime(date1, ISOTIMEFORMAT[mode])
        dt2 = datetime.datetime.strptime(date2, ISOTIMEFORMAT[mode])

        delta = (dt2 - dt1).total_seconds()

        return delta
    except Exception as err:
        return ''


def last_month():
    month = (datetime.datetime.now() - datetime.timedelta(days=time.localtime().tm_mday)).strftime("%Y-%m")
    return month


def this_week():
    today = datetime.date.today()
    sunday = today + datetime.timedelta(6 - today.weekday())
    return sunday


def get_month_list(year, mode=1):
    if isinstance(year,int):
        year = [year]
    FORMAT = "{}-{:0>2}-{:0>2} {}:{}:{}"

    months = []
    for y in year:
        for m in range(1, 13):
            d = calendar.monthrange(y, m)
            st = FORMAT.format(y, m, 1, '00', '00', '00')
            et = FORMAT.format(y, m, d[1], '23', '59', '59')

            st = date_to_timestamp(st)
            et = date_to_timestamp(et)
            months.append(['{}-{:0>2}'.format(y,m), st, et])

    return months


if __name__ == '__main__':
    print(1)