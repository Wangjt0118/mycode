# coding=UTF-8
import xlrd
import xlwt
import time
import os
import pymongo
from dateutil.parser import parse
from datetime import date, timedelta
from xlutils.copy import copy
import datetime


for_filename = (date.today() + timedelta(days=-1)).strftime("%m%d")  # 昨天日期
# start_date = (date.today() + timedelta(days=-2)).strftime("%Y-%m-%d")  # 前天日期
# end_date = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")  # 昨天日期
today = date.today().strftime("%Y-%m-%d")  # 今天日期

start_date = '2021-06-26'
end_date = '2021-06-30'

# DQ_mongo配置
DQ_client = pymongo.MongoClient(host='localhost', port=27071)
# DQ_mongo_db = DQ_client.saas_dq
PPJ_mongo_db = DQ_client.saas_ppj
# ssh -N -L 27071:192.168.2.152:27017 hex@116.214.33.35 -p 2637


# 查询mongo数据库
def getOrderTicketIdsByTimeFromMongo(db_name, begin_query_tag, start, end):
    result = []

    query = {
        "{}".format(begin_query_tag): {"$gte": parse(start), "$lte": parse(end)},
        # "payload.body.item_count": {"$gte": 3},
        # "payload.body.item_count": 1,
        # "payload.body.items.item_id": {"$in": ["9902369", "9902374", "9902376", "9902377", "9902655", "9902654", "9902653", "9902652", "9902651", "9902650", "9902649", "9902648", "9902647", "9902646", "9902645", "9902644", "TC0001", "TC0003", "TC0005", "TC0006", "TC0007", "TC0008", "TC0009", "TC0010", "TC0011", "TC0014", "TC0015", "TC0016", "TC0017", "TC0018", "TC0019", "TC0025", "TC0026", "TC0027", "TC0028", "TC0029", "TC0030", "TC0032", "TC0033", "TC0034", "TC0035", "TC0036", "TC0037", "TC0038", "TC0039", "TC0040", "TC0041", "TC0042", "TC0043", "TC0044", "TC0045", "TC0046", "TC0047", "TC0048", "TCC0049", "TC0050", "TC0051", "TC0052", "TC0049", "TC0054", "TC0055", "TC0056", "TC0057", "TC0058", "TC0059", "TC0060", "TC0061", "TC0062", "TC0063", "TC0064", "TC0065", "TC0067", "TC0067", "TC0068", "TC0069", "TC0070", "TC0071", "TC0079", "TC0080", "TC0081", "TC0082", "TC0083", "TC0084", "TC0085", "TC0086", "TC0087", "TC0088", "TC0089", "TC0090", "TC0091", "TC0092", "TC0093", "TC0094", "TC0095", "TC0096", "TC0097", "TC0098", "TC0099", "TC0100", "TC0101", "TC0102", "TC0103", "TC0104", "TC0105", "TC0106", "TC0107", "TC0108", "TC0109", "TC0110", "TC0111", "TC0112", "TC0113", "TC0114", "TC0115", "TC0116", "SPU000000", "TC0123", "TC0144", "TC0152", "TC0153", "TC0190", "TC0191", "TC0192", "TC0193", "TC0197", "TC0198", "TC0199", "TC0203", "TC0204", "TC0205", "TC0206", "TC0219", "TC0230", "TC0242", "TC0243", "TC0244", "TC0245", "TC0246", "TC0247", "TC0248", "TC0251", "TC0252", "TC0253", "TC0254", "TC0255", "TC0256", "TC0257", "TC0283", "TC0285", "TC0286", "TC0287", "TC0288", "TC0289", "TC0296", "TC0306", "TC0330", "TC0379", "TC0404", "TC0420", "TC0421", "TC0430", "TC0435", "TC0436", "TC0447", "TC0457", "TC0461", "TC0465", "TC0505", "TC0508", "TC0509", "TC0510", "TC0521", "TC0541", "TC0551", "TC0553", "TC0591", "TC0592", "TC0596", "TC0615", "TC0664", "TC0666", "TC0667", "TC0668", "TC0669", "TC0670", "TC0671", "TC0672", "TC0673", "TC0674", "TC0675", "TC0676", "TC0677", "TC0678", "TC0679", "DP00191", "DP00192", "DP00193", "DP00194", "DP00195", "DP00296", "DP00466", "DP00735", "DP00766", "DP00833", "DP00454", "DP00455", "DP00456", "DP00457", "9902110", "9902111", "9902628", "9902629", "DP00108", "DP00109", "DP00110", "DP00111", "DP00317", "DP00458", "DP00465", "DP00483", "DP00701", "9902375", "DP00512", "DP00521", "DP00251", "DP00297", "DP00298", "DP00299", "9900349", "9900488", "9900492", "9900501", "9900496", "9901859", "9901824", "9901860", "9901861", "9901864", "9901862", "9901878", "9901863", "9901875", "9901876", "9901880", "9901881", "9901879", "9901877", "9901882", "9901887", "9901884", "9901883", "9901886", "9902001", "9902002", "9901888", "9901885", "9902666", "9902667", "DP00048", "DP00049", "DP00141", "DP00142", "DP00291", "DP00334", "DP00692"]},
        # "payload.body.items.item_id": {"$in": ["TC0853"]},
        # "payload.body.payments.tender_name": "招行积分"
        # "payload.body.item_count": {"$gte": 2}
        # "payload.body.hex_discount_list.name": {"$in": ["防疫情关怀加做一份", "堂食防疫情关怀"]},
        # "payload.body.is_cancel": True,
        # "payload.body.hex_discount_list.name": "复苏买一送一",
        # "store_name": "肇嘉浜店"
        # "store_name": "上海宝山安信店",
        # "store_type": "DRS",
        # "payload.body.hex_discount_list.code": {"$in": ["201907301", "202007150", "202002051", "202001311", "202001312",
        #                                                 "202001314", "202001315", "202001313", "D201712066"]},
        # "payload.body.items.category.name": "轻食",
        # "payload.body.items.category.id": {"$in": ["4420171020030214144", "4001386192770830337", "3942172690725117953", "3987859053276573697", "4420218594342764544"]}
    }
    mongoret = db_name.pos.find(query, {"store_name": 1, "payload.body.order_no": 1, "sales_date": 1,
                                        "terminal_open_time": 1, "created": 1,
                                        "payload.body.is_cancel": 1,
                                        "payload.body.order_unique_no": 1, "payload.body.dept_class_name": 1,
                                        "payload.body.pos_name": 1, "payload.body.payments": 1,
                                        "payload.body.items.amount": 1,
                                        "payload.body.items.dis_amount": 1,
                                        "payload.body.items.hex_dis_amount": 1,
                                        "payload.body.items.hex_net_amount": 1,
                                        "payload.body.items.item_id": 1,
                                        "payload.body.items.item_key_id": 1,
                                        "payload.body.items.name": 1,
                                        "payload.body.items.qty": 1,
                                        "payload.body.hex_discount_list": 1
                                        })

    for r in mongoret:
        # print(r)
        sales_date = r.get("sales_date", {})
        store_name = r.get("store_name", {})
        terminal_open_time = r.get("terminal_open_time", {})
        created = r.get("created", {})
        if created:
            upload_time = created + datetime.timedelta(hours=8)
        is_cancel = r.get("payload", {}).get("body", {}).get("is_cancel", "")
        if is_cancel:
            is_cancel = '撤销订单'
        else:
            is_cancel = '销售'
        ticket_id = r.get("payload", {}).get("body", {}).get("order_unique_no", "")
        ticket_no = r.get("payload", {}).get("body", {}).get("order_no", "")
        pos_name = r.get("payload", {}).get("body", {}).get("pos_name", "")
        dept_class_name = r.get("payload", {}).get("body", {}).get("dept_class_name", "")
        product_info_list = r.get("payload", {}).get("body", {}).get("items", "")
        sales_date_list = []
        sales_date_list.append(sales_date)
        store_name_list = []
        store_name_list.append(store_name)
        ticket_id_list = []
        ticket_id_list.append(ticket_id)
        ticket_no_list = []
        ticket_no_list.append(ticket_no)
        pos_name_list = []
        pos_name_list.append(pos_name)
        dept_class_name_list = []
        dept_class_name_list.append(dept_class_name)

        product_no_list = []
        product_id_list = []
        product_name_list = []
        product_item_count = []
        product_price_list = []
        discount_trans_list = []
        product_dis_list = []
        product_net_amount_list = []
        if len(product_info_list) > 0:
            for i in range(len(product_info_list)):
                if product_info_list[i].get('item_id'):
                    product_no_list.append(product_info_list[i]['item_id'])
                else:
                    product_no_list.append('')
                if product_info_list[i].get('item_key_id'):
                    product_id_list.append(product_info_list[i]['item_key_id'])
                else:
                    product_id_list.append('')
                if product_info_list[i].get('name'):
                    product_name_list.append(product_info_list[i]['name'])
                else:
                    product_name_list.append('')
                if product_info_list[i].get('qty'):
                    product_item_count.append(product_info_list[i]['qty'])
                else:
                    product_item_count.append('')
                if product_info_list[i].get('amount'):
                    product_price_list.append(product_info_list[i]['amount'])
                else:
                    product_price_list.append('')
                if product_info_list[i].get('dis_amount'):
                    product_dis_list.append(product_info_list[i]['dis_amount'])
                else:
                    product_dis_list.append('')

                # 转换后
                if product_info_list[i].get('hex_dis_amount'):
                    discount_trans_list.append(product_info_list[i]['hex_dis_amount'])
                else:
                    discount_trans_list.append('')
                #   结束

                if product_info_list[i].get('hex_net_amount'):
                    product_net_amount_list.append(product_info_list[i]['hex_net_amount'])
                else:
                    product_net_amount_list.append('')
        discounts = r.get("payload", {}).get("body", {}).get("hex_discount_list", "")
        discount_code_list = []
        discount_name_list = []
        discount_amount_list = []
        if len(discounts) > 0:
            for n in range(len(discounts)):
                discount_code_list.append(discounts[n].get('code'))
                if discounts[n].get('name'):
                    discount_name_list.append(discounts[n].get('name'))
                else:
                    discount_name_list.append('')
                if discounts[n].get('amount'):
                    discount_amount_list.append(discounts[n].get('amount'))
                else:
                    discount_amount_list.append('')

        pay_tenders = r.get("payload", {}).get("body", {}).get("payments", "")
        pay_tender_name_list = []
        pay_tender_id_list = []
        real_pay_list = []
        change_list = []
        trans_discount_amount_list = []
        if len(pay_tenders) > 0:
            for j in range(len(pay_tenders)):
                if pay_tenders[j].get('tender_name'):
                    pay_tender_name_list.append(pay_tenders[j].get('tender_name'))
                else:
                    pay_tender_name_list.append('')
                if pay_tenders[j].get('tender_id'):
                    pay_tender_id_list.append(pay_tenders[j].get('tender_id'))
                else:
                    pay_tender_id_list.append('')
                if pay_tenders[j].get('amount'):
                    real_pay_list.append(pay_tenders[j].get('amount'))
                else:
                    real_pay_list.append('')
                if pay_tenders[j].get('change'):
                    change_list.append(pay_tenders[j].get('change'))
                else:
                    change_list.append('')
                if pay_tenders[j].get('hex_trans_discount_amount'):
                    trans_discount_amount_list.append(pay_tenders[j].get('hex_trans_discount_amount'))
                else:
                    trans_discount_amount_list.append('')

        # 比较折扣和支付
        pp = len(pay_tenders)
        qq = len(discounts)
        if pp < qq:
            d = qq - pp
            for f in range(d):
                pay_tender_name_list.append('')
                pay_tender_id_list.append('')
                real_pay_list.append('')
                change_list.append('')
                trans_discount_amount_list.append('')
        if pp > qq:
            h = pp - qq
            for n in range(h):
                discount_code_list.append('')
                discount_name_list.append('')
                discount_amount_list.append('')

        w = len(product_info_list)
        # print('w的长度是{}'.format(w))
        pp = len(pay_tender_name_list)
        # print('pp的长度是{}'.format(pp))
        if pp < w:
            d = w - pp
            for f in range(d):
                # print('d长度{}'.format(d))
                pay_tender_name_list.append('')
                pay_tender_id_list.append('')
                real_pay_list.append('')
                change_list.append('')
                trans_discount_amount_list.append('')
                discount_code_list.append('')
                discount_name_list.append('')
                discount_amount_list.append('')
        if pp > w:
            h = pp - w
            # print('h长度{}'.format(h))
            for n in range(h):
                product_no_list.append('')
                product_id_list.append('')
                product_name_list.append('')
                discount_trans_list.append('')
                product_item_count.append('')
                product_price_list.append('')
                product_dis_list.append('')
                product_net_amount_list.append('')

        for k in range(len(product_id_list)):
            if len(product_no_list) == len(product_id_list) == len(product_name_list) == len(product_item_count) \
                    == len(product_price_list) == len(product_dis_list) == len(discount_trans_list) == \
                    len(discount_code_list) == len(discount_name_list) == len(discount_amount_list) == \
                    len(pay_tender_name_list):
                final_res = str(sales_date) + '#' + str(terminal_open_time) + '#' + str(upload_time) + '#' + str(store_name) + '#' + str(is_cancel) + '#' + str(
                    ticket_id) + '#' + \
                            str(ticket_no) + '#' \
                            + str(dept_class_name) + '#' + str(pos_name) + '#' + str(product_no_list[k]) + '#' + \
                            str(product_id_list[k]) + '#' + str(product_name_list[k]) + '#' \
                            + str(product_item_count[k]) + '#' + str(product_price_list[k]) + '#' \
                            + str(product_dis_list[k]) + '#' + str(discount_trans_list[k]) + '#' \
                            + str(discount_code_list[k]) + '#' + str(discount_name_list[k]) + '#' \
                            + str(discount_amount_list[k]) + '#' + str(pay_tender_name_list[k]) + '#' \
                            + str(pay_tender_id_list[k]) + '#' + str(real_pay_list[k]) + '#' + str(
                    change_list[k]) + '#' + str(trans_discount_amount_list[k])
                # + '#' + str(trans_discount_amount_list[k]
                # + '#' + str(real_pay_list[k]) + '#' + str(change_list[k]
                # print(final_res)
                result.append(final_res)
            else:
                print('***************************************************')
                print(str(store_name) + '#' + str(ticket_no) + '#' + str(ticket_id))
                # print(ticket_no)
                # print(ticket_id)
                print('列表长度不相等')

    return result


def get_format_data(ticket_info_list):
    final_value = []
    print('-----------------------------------------------------------------------')
    print(len(ticket_info_list))
    for ticket_info in ticket_info_list[:]:
        new_ticket_info = ticket_info.split('#')
        # 剔除支付方式为奥斯卡的空单,经测可用
        if new_ticket_info[18] == '奥斯卡2' and new_ticket_info[8] == '' and new_ticket_info[19] == '':
            ticket_info_list.remove(ticket_info)
            continue
        try:
            if isinstance(new_ticket_info, list):
                if new_ticket_info[12]:
                    product_num = int(new_ticket_info[12])
                    del new_ticket_info[12]
                    new_ticket_info.insert(12, product_num)
                if new_ticket_info[13]:
                    product_price = float(new_ticket_info[13])
                    del new_ticket_info[13]
                    new_ticket_info.insert(13, product_price)
                if new_ticket_info[14]:
                    product_discount = float(new_ticket_info[14])
                    del new_ticket_info[14]
                    new_ticket_info.insert(14, product_discount)
                if new_ticket_info[15]:
                    product_trans = float(new_ticket_info[15])
                    del new_ticket_info[15]
                    new_ticket_info.insert(15, product_trans)
                if new_ticket_info[17]:
                    discount_amount = float(new_ticket_info[17])
                    del new_ticket_info[17]
                    new_ticket_info.insert(17, discount_amount)
                if new_ticket_info[20]:
                    real_pay = float(new_ticket_info[20])
                    del new_ticket_info[20]
                    new_ticket_info.insert(20, real_pay)
                if new_ticket_info[21]:
                    change = float(new_ticket_info[21])
                    del new_ticket_info[21]
                    new_ticket_info.insert(21, change)
                if new_ticket_info[22]:
                    pay_trans_dis = float(new_ticket_info[22])
                    del new_ticket_info[22]
                    new_ticket_info.insert(22, pay_trans_dis)
                final_value.append(new_ticket_info)

        except:
            final_value.append(new_ticket_info)
    return final_value


def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False


def get_all_file(all_file_path):
    filename_list = []
    # 获取目标文件夹的路径
    meragefiledir = all_file_path
    # 获取当前文件夹中的文件名称列表
    filenames = os.listdir(meragefiledir)
    for filename in filenames:
        filepath = meragefiledir + '\\'
        filepath = filepath + filename
        filename_list.append(filepath)
    return filename_list


def write_data_to_excel(ticket_info_list, filename, mkpath):
    # book_name_xls = '{}/{}.xls'.format(mkpath, filename)
    sheet_name_xls = filename
    value_title = [["营业日期",
                    "交易时间",
                    "小票上传时间",
                    "门店名称",
                    "销售类型",
                    "订单ID",
                    "交易编号",
                    "交易类型",
                    "POS机",
                    "商品编码",
                    "商品ID",
                    "商品名称",
                    "商品数量",
                    "商品总价",
                    "单品折扣",
                    "转换后",
                    "折扣编号",
                    "折扣方式",
                    "折扣金额",
                    "支付方式",
                    "支付编码",
                    "实际支付",
                    "找零",
                    "支付转折扣"], ]

    # 写入
    final_result_data = get_format_data(ticket_info_list)
    # print(final_result_data)
    # 170000
    print(len(final_result_data))
    if len(final_result_data) > 65500:
        final_result_data1 = final_result_data[:65500]
        final_result_data2 = final_result_data[65500:]  # 87228
        book_name_xls = '{}/{}_1.xls'.format(mkpath, filename)
        write_excel_xls(book_name_xls, sheet_name_xls, value_title)
        write_excel_xls_append(book_name_xls, final_result_data1)

        if len(final_result_data2) > 65500:
            final_result_data3 = final_result_data2[:65500]
            final_result_data4 = final_result_data2[65500:]  # 21728
            book_name_xls = '{}/{}_2.xls'.format(mkpath, filename)
            write_excel_xls(book_name_xls, sheet_name_xls, value_title)
            write_excel_xls_append(book_name_xls, final_result_data3)
            if len(final_result_data4) > 65500:
                final_result_data5 = final_result_data4[:65500]
                final_result_data6 = final_result_data4[65500:]
                book_name_xls = '{}/{}_3.xls'.format(mkpath, filename)
                write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                write_excel_xls_append(book_name_xls, final_result_data5)

                if len(final_result_data6) > 65500:
                    final_result_data7 = final_result_data6[:65500]
                    final_result_data8 = final_result_data6[65500:]
                    book_name_xls = '{}/{}_4.xls'.format(mkpath, filename)
                    write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                    write_excel_xls_append(book_name_xls, final_result_data7)
                    if len(final_result_data8) > 65500:
                        final_result_data9 = final_result_data6[:65500]
                        final_result_data10 = final_result_data6[65500:]
                        book_name_xls = '{}/{}_5.xls'.format(mkpath, filename)
                        write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                        write_excel_xls_append(book_name_xls, final_result_data9)
                        if len(final_result_data10) > 65500:
                            final_result_data11 = final_result_data6[:65500]
                            final_result_data12 = final_result_data6[65500:]
                            book_name_xls = '{}/{}_6.xls'.format(mkpath, filename)
                            write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                            write_excel_xls_append(book_name_xls, final_result_data11)
                            if len(final_result_data12) > 65500:
                                final_result_data13 = final_result_data6[:65500]
                                final_result_data14 = final_result_data6[65500:]
                                book_name_xls = '{}/{}_7.xls'.format(mkpath, filename)
                                write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                write_excel_xls_append(book_name_xls, final_result_data13)
                                if len(final_result_data14) > 65500:
                                    final_result_data15 = final_result_data6[:65500]
                                    final_result_data16 = final_result_data6[65500:]
                                    book_name_xls = '{}/{}_8.xls'.format(mkpath, filename)
                                    write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                    write_excel_xls_append(book_name_xls, final_result_data15)
                                    if len(final_result_data16) > 65500:
                                        final_result_data17 = final_result_data6[:65500]
                                        final_result_data18 = final_result_data6[65500:]
                                        book_name_xls = '{}/{}_9.xls'.format(mkpath, filename)
                                        write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                        write_excel_xls_append(book_name_xls, final_result_data17)
                                        if len(final_result_data18) > 65500:
                                            final_result_data19 = final_result_data6[:65500]
                                            final_result_data20 = final_result_data6[65500:]
                                            book_name_xls = '{}/{}_10.xls'.format(mkpath, filename)
                                            write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                            write_excel_xls_append(book_name_xls, final_result_data19)
                                            if len(final_result_data20) > 65500:
                                                final_result_data21 = final_result_data6[:65500]
                                                final_result_data22 = final_result_data6[65500:]
                                                book_name_xls = '{}/{}_11.xls'.format(mkpath, filename)
                                                write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                                write_excel_xls_append(book_name_xls, final_result_data21)
                                                if len(final_result_data22) > 65500:
                                                    final_result_data23 = final_result_data6[:65500]
                                                    final_result_data24 = final_result_data6[65500:]
                                                    book_name_xls = '{}/{}_12.xls'.format(mkpath, filename)
                                                    write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                                    write_excel_xls_append(book_name_xls, final_result_data23)
                                                    if len(final_result_data24) > 65500:
                                                        final_result_data25 = final_result_data6[:65500]
                                                        final_result_data26 = final_result_data6[65500:]
                                                        book_name_xls = '{}/{}_13.xls'.format(mkpath, filename)
                                                        write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                                        write_excel_xls_append(book_name_xls, final_result_data25)
                                                        if len(final_result_data26) > 65500:
                                                            final_result_data27 = final_result_data6[:65500]
                                                            final_result_data28 = final_result_data6[65500:]
                                                            book_name_xls = '{}/{}_14.xls'.format(mkpath, filename)
                                                            write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                                            write_excel_xls_append(book_name_xls, final_result_data27)
                                else:
                                    book_name_xls = '{}/{}_8.xls'.format(mkpath, filename)
                                    write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                    write_excel_xls_append(book_name_xls, final_result_data14)
                            else:
                                book_name_xls = '{}/{}_7.xls'.format(mkpath, filename)
                                write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                                write_excel_xls_append(book_name_xls, final_result_data12)
                        else:
                            book_name_xls = '{}/{}_6.xls'.format(mkpath, filename)
                            write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                            write_excel_xls_append(book_name_xls, final_result_data10)
                    else:
                        book_name_xls = '{}/{}_5.xls'.format(mkpath, filename)
                        write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                        write_excel_xls_append(book_name_xls, final_result_data8)
                else:
                    book_name_xls = '{}/{}_4.xls'.format(mkpath, filename)
                    write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                    write_excel_xls_append(book_name_xls, final_result_data6)
            else:
                book_name_xls = '{}/{}_3.xls'.format(mkpath, filename)
                write_excel_xls(book_name_xls, sheet_name_xls, value_title)
                write_excel_xls_append(book_name_xls, final_result_data4)
        else:
            book_name_xls = '{}/{}_2.xls'.format(mkpath, filename)
            write_excel_xls(book_name_xls, sheet_name_xls, value_title)
            write_excel_xls_append(book_name_xls, final_result_data2)
    else:
        book_name_xls = '{}/{}.xls'.format(mkpath, filename)
        write_excel_xls(book_name_xls, sheet_name_xls, value_title)
        write_excel_xls_append(book_name_xls, final_result_data)


def main():
    # 创建目录
    # 定义要创建的目录
    # mkpath = "/Users/yjq/Desktop/work/DQ_ticket_info/" + for_filename + "/"
    mkpath = "/Users/yjq/Desktop/work/PPJ_ticket_info/" + for_filename + "/"
    # 调用函数
    mkdir(mkpath)

    # 拿到数据并写入文件
    # 将全门店电子小票信息写入文件
    # ticket_info_list = getOrderTicketIdsByTimeFromMongo(DQ_mongo_db, "sales_date", '{}T16:00:00'.format(start_date),
    #                                                                 '{}T16:00:00'.format(end_date))
    ticket_info_list = getOrderTicketIdsByTimeFromMongo(PPJ_mongo_db, "sales_date", '{}T16:00:00'.format(start_date),
                                                        '{}T16:00:00'.format(end_date))

    # filename = 'DQ全门店特定电子小票信息{}'.format(for_filename)
    filename = 'PPJ全门店特定电子小票信息{}'.format(for_filename)
    write_data_to_excel(ticket_info_list, filename, mkpath)


if __name__ == '__main__':
    main()
