# -*- coding: utf-8 -*-

import xlrd
import xlsxwriter


def read_source_data_single(filename, mode = True):
    """
    默认原excel有title,单sheet文件

    """
    workbook = xlrd.open_workbook(filename)
    sheet2 = workbook.sheet_by_index(0)  # sheet索引从0开始
    total_rows = sheet2.nrows  # 总行数

    if mode:
        head = sheet2.row_values(0)  # 获取第一行字段内容
        start = 1
    else:
        head = None
        start = 0

    data = []
    for row in range(start, total_rows):
        rows = sheet2.row_values(row)
        data.append(rows)

    return head,data


def read_source_data(filename, sh = 0, mode=1):
    """
    默认原excel有title,多sheet读取，从0开始
    :param filename:
    :param sh: sheet名字或下标
    :param mode: 是否要title
    :return:

    """
    workbook = xlrd.open_workbook(filename)
    count = len(workbook.sheets())  # sheet数量
    data = []
    for i in range(count):
        sheet2 = workbook.sheet_by_index(i)  # sheet索引从0开始
        total_rows = sheet2.nrows  # 总行数

        if mode:
            head = sheet2.row_values(0)  # 获取第一行字段内容
            start = 1
        else:
            head = None
            start = 0

        for row in range(start, total_rows):
            rows = sheet2.row_values(row)
            data.append(rows)

    return head,data


def _set_title_format(workbook,title_format=None):
    # 标题格式
    title_format = title_format or {
        'bold': 1,
        'border': 1,
        'font_size': 12,
#        'font_color': '636363',
        'bg_color': 'c0c0c0'
    }
    tf = workbook.add_format(title_format)
    tf.set_align('center')  # 设置水平居中对齐
    tf.set_align('vcenter')  # 设置垂直居中对齐
    return tf

def _set_row_format(workbook, row_format=None):
    # 文本格式
    row_format = row_format or {
        'bold': 0,
        'border': 1,
        'font_size': 10,
    }
    rf = workbook.add_format(row_format)
    rf.set_align('center')
    rf.set_align('vcenter')
    return rf


def write_target_xlsx(filename, title, data,
                      sheets = None, title_format_type = None,
                      row_format_type = None, path = '../data',
                      direction = 1):
    """
    Create a new Excel.

    Args:
        filename: ....
        title: ['日期','xxx']
        data:[[],[],[],[]]
        sheets:['aaa','aaa','bbb']
        title_format_type: {'bold': 0,'border': 1,...}
        row_format_type: {'bold': 0,'border': 1,...}
        path: directory name
        direction : 1 row  2 col

    Returns:

    """
    book = xlsxwriter.Workbook(path + '/' + filename)

    tf = _set_title_format(book)
    rf = _set_row_format(book)

    if isinstance(sheets,list):
        for sheet_name in sheets:
            sheet = book.add_worksheet(sheet_name)
            if direction == 1:
                sheet.write_row(0, 0, title, tf)
            else:
                sheet.write_column(0, 0, title, tf)
            _write_data(sheet, data, rf, direction)
    else:
        sheet = book.add_worksheet()
        if direction == 1:
            sheet.write_row(0, 0, title, tf)
        else:
            sheet.write_column(0, 0, title, tf)
        _write_data(sheet,data,rf,direction)
    book.close()

def _write_data(sheet,data,format_type,direction=1):
    if direction == 1:
        row = 1
        for lines in data:
            for cols in range(len(lines)):
                sheet.write(row, cols, lines[cols], format_type)
            row += 1
            print('write line number: {}'.format(row))
    else:
        col = 1
        for lines in data:
            for row in range(len(lines)):
                sheet.write(row, col, lines[row], format_type)
            col += 1
            print('write line number: {}'.format(col))


if __name__ == '__main__':
    print(1)
