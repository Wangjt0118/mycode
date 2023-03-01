def t(l):
    product_info_map = {'1234': {'qty': 1, 'refund_qty': 0}, '81010293':  {'qty': 1, 'refund_qty': 0}}


    for i in l:
      product_info = product_info_map.get(i.get('extPid'))
      if product_info:
        qty = product_info.get("qty", 0)
        refund_qty = product_info.get("refund_qty", 0)

        product_info['refund_qty'] = refund_qty + i.get('num')

    print(product_info_map)


l = [
            {
                "extPid":"1234",
                "refundIndex":1,
                "price":5,
                "pname":"芒果酪酪-乐",
                "num":1,
                "refundPrice":5
            },
            {
                "extPid":"81010293",
                "refundIndex":2,
                "price":20,
                "pname":"薄荷津津柠檬茶",
                "num":1,
                "refundPrice":20
            },
            {
                "extPid":"81010295",
                "refundIndex":3,
                "price":22,
                "pname":"祁红津津柠檬茶",
                "num":1,
                "refundPrice":22
            }
        ]
t(l)