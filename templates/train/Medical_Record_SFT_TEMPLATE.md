# Example of TCMSD & TCMDD

## Query

下面是一名患者的病历情况：  
年龄：{age}，性别：{sex}  
主诉：{chief complaint}  
入院症见：{admission condition}  
现病史：{present medical history}  
既往史：{past medical history}  
个人史：{personal history}  
婚育史：{marital and reproductive history}  
家族史：{family history}  

请依据患者的主诉、病史、年龄、性别及中医望闻问切的结果，确定其主要中医疾病与中医证型，并给出辨病辨证的理由。

## Response

根据患者的性别、年龄、主诉、病史和中医望闻问切的情况，患者可能患有 **{disease}**，中医证型属于 **{syndrome}**。  
**{disease and syndrome differentiation analysis}**

---

# Example of Differential Diagnosis

## Query

病人被诊断为 **{disease}**，该诊断需要与哪些病症进行鉴别？怎样进行鉴别？

## Response

**{differential diagnosis of {disease}}**

---

# Example of Diagnosis and Treatment Plan

## Query

请查阅这名患者的入院情况和诊断信息：  
年龄：{age}，性别：{sex}  
主诉：{chief complaint}  
入院症见：{admission condition}  
中医望闻切诊：{TCM four diagnostic methods}  
现病史：{present medical history}  
既往史：{past medical history}  
个人史：{personal history}  
婚育史：{marital and reproductive history}  
家族史：{family history}  
专科检查：{specialist examination}  
辅助检查：{auxiliary examination}  
体格检查：{physical examination}  
西医诊断：{Western Medicine Diagnosis}  
中医诊断：{TCM Diagnosis}  
中医证型：{TCM Syndrome}  

请根据该患者的入院描述和诊断信息，为患者制定一个治疗计划。

## Response

**{diagnosis and treatment plan}**