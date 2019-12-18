"""
    作者：Auto——LZC
    功能：货币兑换
    版本：Ver:2.0
    日期：17/01/2019
    新增功能：自动货币类型识别
"""

#  汇率
per = 5.6

while True:
    input_currency = input("请输入带单位的金额：")

    if input_currency[0] == "$":
        output_currency = eval(input_currency[1:])*per
        print("美元兑换为人民币金额为："+str(output_currency))

    elif input_currency[0] == "Y":
        output_currency = eval(input_currency[1:])/per
        print("兑换为美元金额为："+str(output_currency))

    else:
        print("输入有误，兑换失败！")

