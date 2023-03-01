# -*- coding: utf-8 -*-
from copy import deepcopy
import json
from set_meal import meal

def get_order_product_db_map(order_info):
    """
    本次开发修改内容：
    1、在此把套餐结构转化为单品，此后所有逻辑都不需要改动
    2、套餐内属性分别加在  每个  "propertyMemo":"drink"的⼦项上
    3、套餐内加料放在  第一个  "propertyMemo":"drink"的⼦项上
    4、分摊金额，最后一个子项调整尾差
    5、在修改后的子项转单品上新增 set_meal_id 记录原套餐ID，在部分退时找商品时用
    
    property_adding_product举例:
    {"10001":{"property":[{"pid":610172,"items":[{"uid":2428177,"name":"冷","nameEn":"","nameTw":"","price":0,
    "realTimePrice":0,"editType":0,"isStandardType":False,"itemType":3,"weight":0,"mealFee":0,"mulMealFee":0,
    "part":0,"selectNum":1,"num":1,"bizType":0,"materialCost":0,"totalPrice":0}],"type":3,"editType":0,
    "propertyMemo":""}],"adding":[{"index":0,"totalPrice":0,"mealFee":0,"uid":800941492,"weight":0,
    "itemProduct":{"extMappingType":0,"pid":0,"extId":"83910039"},"bizType":0,"isStandardType":true,"price":0,
    "editType":0,"name":"不加料","num":1,"nameTw":"","mulMealFee":0,"materialCost":0,"part":0,"realTimePrice":0,
    "nameEn":"","itemType":1}],"drink":[{"uid":2428180,"name":"大口草莓","nameEn":"",
    "nameTw":"","price":0,"realTimePrice":0,"editType":0,"isStandardType":False,"itemType":2,"weight":0,"mealFee":0,
    "mulMealFee":0,"part":0,"selectNum":2,"num":2,"bizType":0,"materialCost":0,"totalPrice":0}],
    "other":[{"pid":610174,"items":[{"uid":2428182,"name":"牛角包","nameEn":"",
    "nameTw":"","price":0,"realTimePrice":0,"editType":0,"isStandardType":False,"itemType":2,"weight":0,"mealFee":0,
    "mulMealFee":0,"part":0,"selectNum":1,"num":1,"bizType":0,"materialCost":0,"totalPrice":0}],"type":2,
    "editType":0,"propertyMemo":"bread"}]}}
    """
    new_products = []
    fix_products = deepcopy(order_info.get('products', []))
    # 先取出套餐内的属性和加料
    property_addition_product = {}
    for index, product in enumerate(fix_products):
        if product.get('nameTw') == 'Set':
            default_key = product.get('extId') + '_' + str(index)
            property_addition_product.setdefault(default_key, {})
            # 记录所有单品加料的总价格
            property_addition_product[default_key].setdefault('single_product_all_price', 0)
            for lr in product.get('listRequirements'):
                for pr in lr.get('propertys'):
                    property_addition_product[default_key].setdefault('property', [])
                    property_addition_product[default_key].setdefault('addition', [])
                    property_addition_product[default_key].setdefault('drink', [])
                    property_addition_product[default_key].setdefault('other', [])
                    # 属性
                    if pr.get('propertyMemo') == 'property':
                        property_addition_product[default_key]['property'].append(pr)
                    # 加料
                    elif pr.get('propertyMemo') == 'addition':
                        for inner_product in pr.get('items'):
                            property_addition_product[default_key]['addition'].append(inner_product)
                            property_addition_product[default_key]['single_product_all_price'] += \
                                round(inner_product.get('price') * inner_product.get('num'), 2)
                    # 饮品,餐道：一个套餐内可能有多个drink,每个drink里可能有多个单品
                    elif pr.get('propertyMemo') == 'drink':
                        for inner_product in pr.get('items'):
                            property_addition_product[default_key]['drink'].append(inner_product)
                            property_addition_product[default_key]['single_product_all_price'] += \
                                round(inner_product.get('price') * inner_product.get('num'), 2)
                    # 面包以及其他,先放在一起
                    else:
                        for inner_product in pr.get('items'):
                            property_addition_product[default_key]['other'].append(inner_product)
                            property_addition_product[default_key]['single_product_all_price'] += \
                                round(inner_product.get('price') * inner_product.get('num'), 2)
    print('--' * 10)
    print(json.dumps(property_addition_product))
    print('--' * 10)
    for index, product in enumerate(fix_products):
        if not product.get('nameTw'):
            # 单品直接添加
            new_products.append(product)
        elif product.get('nameTw') == 'Set':
            # 套餐特殊处理
            default_key = product.get('extId') + '_' + str(index)
            set_meal_price = set_meal_price_copy = product.get('totalPrice') / product.get('num')  # 单个套餐价格
            single_product_all_price = property_addition_product.get(default_key).\
                get('single_product_all_price')
            # 设置一个序列，在退款时按照此序列在最后一个单品补尾差
            seq_id = 0
            # 先处理drink以外的单品
            for other_product in property_addition_product.get(default_key).get('other'):
                single_price = round((other_product.get('price') * 1.0 / single_product_all_price)
                                     * set_meal_price, 2)
                # 考虑到一个套餐内可能有相同单品，减去倍数值
                set_meal_price_copy -= (single_price * other_product.get('num'))
                new_products.append({
                    'extId': other_product.get('itemProduct', {}).get('extId'),
                    'num': other_product.get('num') * product.get('num'),
                    'name': other_product.get('name'),
                    'realTimePrice': single_price,
                    'realTimeTotalPrice': single_price * other_product.get('num') * product.get('num'),
                    # 以下字段是字部分退款时需要
                    'set_meal_id': default_key,
                    'set_seq_id': seq_id,
                    'set_meal_price': set_meal_price,
                    'set_single_rate': other_product.get('num'),
                    'set_refund_qty': 0,
                    'set_meal_qty': product.get('num')
                })
                seq_id += 1
            drink_len = len(property_addition_product.get(default_key).get('drink'))
            for index, drink_product in enumerate(property_addition_product.get(default_key).get('drink')):
                # 加料只在第一个单品添加，属性全部都有
                list_requirements = deepcopy([{
                    'propertys': property_addition_product.get(default_key).get('property') or [],
                    'num': drink_product.get('num') * product.get('num')
                }])
                if index == 0:
                    for add_product in property_addition_product.get(default_key).get('addition'):
                        add_price = round(add_product.get('realTimePrice') * 1.0 /
                                          single_product_all_price * set_meal_price, 2)
                        add_product['realTimePrice'] = add_price
                        list_requirements[0]['propertys'].append({
                            'items': [add_product]
                        })
                        # 考虑到一个套餐内可能有相同加料，减去倍数值
                        set_meal_price_copy -= (add_price * add_product.get('num'))
                if index == (drink_len - 1):
                    single_price = round(set_meal_price_copy / drink_product.get('num'), 2)
                else:
                    single_price = round((drink_product.get('price') * 1.0 / single_product_all_price)
                                         * set_meal_price, 2)
                    # 考虑到一个套餐内可能有相同单品，减去倍数值
                    set_meal_price_copy -= (single_price * drink_product.get('num'))
                new_products.append({
                    'extId': drink_product.get('itemProduct', {}).get('extId'),
                    'num': drink_product.get('num') * product.get('num'),
                    'name': drink_product.get('name'),
                    'realTimePrice': single_price,
                    'realTimeTotalPrice': single_price * drink_product.get('num') * product.get('num'),
                    'listRequirements': list_requirements,
                    # 以下字段是字部分退款时需要
                    'set_meal_id': default_key,
                    'set_seq_id': seq_id,
                    'set_meal_price': set_meal_price,
                    'set_single_rate': drink_product.get('num'),
                    'set_refund_qty': 0,
                    'set_meal_qty': product.get('num')
                })
                seq_id += 1

        else:
            logging.info('报文商品结构既不是单品也不是套餐: %s' % product)
            raise DataValidationException(ErrorCode.DataNotValid, error_msg="商品结构有误！")
    order_info['products'] = new_products
    print(json.dumps(order_info))



meal = json.loads(meal)
get_order_product_db_map(meal.get('data'))
