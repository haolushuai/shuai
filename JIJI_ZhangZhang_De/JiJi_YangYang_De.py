from datetime import datetime
import os
from openai import OpenAI
import numpy as np
import pandas as pd

#数据写入csv文件
def input_csv(input_type, input_content_nu, input_content,input_output_ye):
    new_data = pd.DataFrame({
        '训练时间' = 
    })

#硬编码交互获取训练数据
def tui_jian_hard(current_time,input_lian):
    if "没" in input_lian:
        print("快去练，肌肌痒痒的")
        jian_shen = ["练胸","练背","练肩"]*2
        if current_time.weekday() < 6:
            jian_plan = jian_shen[current_time.weekday()]
            print(f'今天推荐{jian_plan}')
        else:
            print("今天休息日")
    else:
        input_type = input("今天练的什么？")
        input_content_nu = input("做了几个动作？")
        input_content = input("都做了什么动作？分别几组？每组几次？（推荐依照：平板卧推60kg*4*8的格式写入，中间空格分隔")
        input_output_ye = input("上次训练效果如何？")

        print("干别的去吧，肌肌涨涨的")


if __name__ == '__main__':
    current_time = datetime.now()
    current_time_tim = current_time.strftime("%Y-%m-%d %H:%M:%S")
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekday_cn = weekdays[current_time.weekday()]
    print(current_time)
    print(weekday_cn)
    input_lian = input("今天练了么？\n回答:")