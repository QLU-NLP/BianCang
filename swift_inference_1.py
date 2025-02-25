import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

from swift.llm import (
    get_model_tokenizer, get_template, inference, ModelType
)
from swift.utils import seed_everything

model_type = ModelType.qwen2_5_7b_instruct
template_type = 'qwen'

model_id_or_path = 'BianCang-Qwen2.5-7B-Instruct'
model, tokenizer = get_model_tokenizer(model_type, model_id_or_path=model_id_or_path, model_kwargs={'device_map': 'auto'})
model.generation_config.max_new_tokens = 256

template = get_template(template_type, tokenizer)
seed_everything(42)
query = '你好，你是谁？'
response, history = inference(model, template, query)
print(f'query: {query}')
print(f'response: {response}')
query = '下面是一名患者的基本情况。年龄：78岁，性别：女。主 诉：活动后胸痛一周。现病史：患者一周前活动后出现胸口隐隐作痛，如针刺样乏力气短，活动后汗出，偏头痛。中医望闻切诊：表情自然，面色红润，形体正常,语气清,气息平；无异常气味,舌暗红，苔少。请你根据上述患者的主诉、病史和中医望闻切诊情况，判断该患者的主要中医疾病和中医证型，并给出中医辨病辨证的依据。'
response, history = inference(model, template, query, history)
print(f'query: {query}')
print(f'response: {response}')
print(f'history: {history}')