#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
import pandas as pd
import numpy as np

def separate_w_val(total_w):
    w2 = 0
    w3 = 0
    w4 = 0
    if total_w <=10:
        w1 = total_w
        
    elif total_w >10 and total_w <=25:
        w1 = 10
        w2 = total_w - w1
        
    elif total_w > 25 and total_w <=50:
        w1 = 10
        w2 = 15
        w3 = total_w - (w1 + w2)
        
    else:
        w1 = 10
        w2 = 15
        w3 = 25
        w4 = total_w - (w1 + w2 + w3)
    
    w_list = [w1, w2, w3, w4]
    return w_list


def calc_each_pay(w_list, fee_list):
    pay_list = []
    for w,fee in zip(w_list, fee_list):
        wx_pay = w*fee
        pay_list.append(wx_pay)
    return pay_list

    
def calc_base_fee(pipe_size):
    if pipe_size == 13:
        base_fee = 520
    elif pipe_size == 20:
        base_fee = 950
    return base_fee


def calc_water_charge(pipe_size, amount_used_water):
    fee_list_water = [65,127,156,201]
    fee_list_sewage = [10,105,165,210]   
    range_list = ["1-10", '11-25', "26-50", "51-"]
    w_list = separate_w_val(amount_used_water)
    base_fee = calc_base_fee(pipe_size) + 700
    pay_list_water = calc_each_pay(w_list, fee_list_water)
    pay_list_sewage = calc_each_pay(w_list, fee_list_sewage)
    total_pay = base_fee + sum(pay_list_water) + sum(pay_list_sewage)
    df = pd.DataFrame(list(zip(range_list, fee_list_water, fee_list_sewage, w_list, pay_list_water, pay_list_sewage)),
                      columns = ["Range", "Fee_w", "Fee_s","Water_used","Amount_pay_w", "Amounot_pay_s"])
    
    print("This month's water chage is {}Yen; Water:{} Yen; Sewage{} Yen)".format(total_pay, sum(pay_list_water) , sum(pay_list_sewage) ))
    print(df)


if __name__ == "__main__":
    calc_water_charge(13, 22)



