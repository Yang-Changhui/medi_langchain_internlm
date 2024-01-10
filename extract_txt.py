# 定义要读取的原始txt文件路径
input_file = "data/2020.txt"

# 定义要保存的目标txt文件路径
output_file = "data/2020_part.txt"

try:
    # 打开原始txt文件进行读取
    with open(input_file, 'r',encoding='utf-8') as file:
        content = file.read()

    # 将原始txt文件的内容写入到目标txt文件中
    with open(output_file, 'a') as file:
        file.write(content[:1000000])

    print("成功保存txt文件！")
except FileNotFoundError:
    print("未找到指定的txt文件！")
except Exception as e:
    print("发生错误：", str(e))