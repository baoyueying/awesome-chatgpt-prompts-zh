import json

# 定义转换函数
def transform_json(json_obj):
    result = []
    for obj in json_obj:
        new_obj = {}
        new_obj['cmd'] = obj['act'].replace(' ', '_').lower()
        new_obj['act'] = obj['act']
        new_obj['prompt'] = obj['prompt']
        new_obj['tags'] = ['chatgpt-prompts']
        new_obj['enable'] = True
        result.append(new_obj)
    return result

# 读取第一段JSON
with open('prompts-zh.json', 'r', encoding='utf-8') as f:
    json_str_1 = f.read()

# 转换第一段JSON为Python对象
json_obj_1 = json.loads(json_str_1)

# 转换第一段JSON为第二段JSON形式
json_obj_2 = transform_json(json_obj_1)

# 保存第二段JSON到本地文件
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(json_obj_2, f, ensure_ascii=False, indent=2)
