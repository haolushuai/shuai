from datetime import datetime
import os
from fileinput import filename

from openai import OpenAI
import numpy as np
import pandas as pd
import os

from pyexpat.errors import messages


#读取csv文件
def out_come_csv():
    df = pd.read_csv('exercise.csv')
    return df

#数据写入csv文件
def input_csv(input_type, input_content_nu, input_content,input_output_ye,current_time_tim):
    df = pd.read_csv('exercise.csv')
    last_index = df.index[-1]
    df.loc[last_index, '效果'] = [input_output_ye]
    new_data = pd.DataFrame({
        '训练时间' : [current_time_tim],
        '训练种类' : [input_type],
        '动作数量' : [input_content_nu],
        '训练内容' : [input_content],
        '效果': [None]
    })
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv('exercise.csv', index=False, header=True, encoding='utf-8-sig')
    print(f"已写入 {len(new_data)} 行，文件路径: {os.path.abspath('exercise.csv')}")





#硬编码交互获取训练数据
def tui_jian_hard(current_time,input_lian,current_time_tim):
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
        input_csv(input_type,input_content_nu,input_content,input_output_ye,current_time_tim)
        print("干别的去吧，肌肌涨涨的")

#连接ai
def analysis_ai_connect():
    filename = "key.txt"
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)
    if not os.path.exists(file_path):
        print("不存在")
    with open(file_path, "r", encoding="utf-8") as f_open:
        key = f_open.read().strip()
        print("key存在，连接开始")
    client = OpenAI(
        api_key=key,
        base_url="https://api.deepseek.com"
    )
    return client

#调用，使用
def analysis_ai(df):
    client = analysis_ai_connect()
    data_txt = df.to_string(index=False)
    messages = [
        {"role": "system",
         "content": "你是一位专业健身教练，请根据训练记录分析效果，指出问题并给出改进建议。"},
        {"role": "user",
         "content": f"以下是我的训练记录：\n{data_txt}\n请帮我分析。"}
    ]
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages
    )
    print(response.choices[0].message.content)

if __name__ == '__main__':
    print("当前工作目录:", os.getcwd())
    print("脚本所在目录:", os.path.dirname(os.path.abspath(__file__)))
    current_time = datetime.now()
    current_time_tim = current_time.strftime("%Y-%m-%d %H:%M:%S")
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    weekday_cn = weekdays[current_time.weekday()]
    print(current_time_tim)
    print(weekday_cn)
    input_lian = input("今天练了么？\n回答:")
    tui_jian_hard(current_time, input_lian,current_time_tim)
    input_ai = input("是否使用ai智能分析？\n")
    if "是" in input_ai:
        df = out_come_csv()
        analysis_ai(df)