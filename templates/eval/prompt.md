### Evaluation prompt

---

#### **Prompt 1: TCM Syndrome Differentiation Prompt Template**

***Direct Inference Prompt Template***

下面是患者的病历信息。  
{主诉} {病史} {入院情况} {中医望闻切诊}  
问题：根据患者的上述情况，患者的中医证型为？  
答案：

Below is the patient's medical record information.  
{chief complaint} {medical history} {admission condition} {TCM four diagnostic methods}  
Question: Based on the patient's condition above, what is the patient's Traditional Chinese Medicine (TCM) syndrome type?  
Answer:

***Chain of Thought Prompt Template***

下面是患者的病历信息。  
{主诉} {病史} {入院情况} {中医望闻切诊}  
问题：根据患者的上述情况，对该患者进行中医辨证分析，首先给出辨证过程和依据，然后给出患者的中医证型。  
答案：

Below is the patient's medical record information.  
{chief complaint} {medical history} {admission condition} {TCM four diagnostic methods}  
Question: Based on the patient's condition, perform a TCM syndrome differentiation analysis. First, provide the process and evidence for the differentiation, then identify the patient's TCM syndrome.  
Answer:

---

#### **Prompt 2: TCM Disease Diagnosis Prompt Template**

***Direct Inference***

下面是患者的病历信息。  
{主诉} {病史} {入院情况} {中医望闻切诊}  
问题：根据患者的上述情况，患者的中医疾病为？答案中只输出疾病名称，不要输出其它额外文本。  
答案：

Below is the patient's medical record information.  
{chief complaint} {medical history} {admission condition} {TCM four diagnostic methods}  
Question: Based on the patient's aforementioned condition, what is the patient's TCM disease? Only provide the disease name in your answer, without any additional text.  
Answer:

***Chain of Thought Prompt Template***

下面是患者的病历信息。  
{主诉} {病史} {入院情况} {中医望闻切诊}  
问题：根据患者的上述情况，对该患者进行中医辨病分析，首先给出辨病过程和依据，然后给出患者的中医疾病。  
答案：

Below is the patient's medical record information.  
{chief complaint} {medical history} {admission condition} {TCM four diagnostic methods}  
Question: Based on the patient's condition, perform a TCM disease differentiation analysis. First, provide the process and evidence for the differentiation, then identify the patient's TCM disease.  
Answer:

---

#### **Prompt 3: National Medical Licensing Examination in China Prompt Template**

以下是关于{问题类型}的一道选择题，不需要做任何分析和解释，直接输出答案选项。  
问题：{题目}  
选项：A. {选项A} B. {选项B} ...  
答案：

The following is a multiple-choice question regarding {question type}. No analysis or explanation is required; simply output the answer option.  
Question: {question}  
Options: A. {optionA} B. {optionB} ...  
Answer:

---

#### **Prompt 4: Chinese Medical Benchmark Prompt Template**

以下是中国{考试类型}中{考试科目}考试的一道{问题类型}，不需要做任何分析和解释，直接输出答案选项。  
{题目} A. {选项A} B. {选项B} ...

The following is a {question type} from the {exam class} exam in China's {exam type}. No analysis or explanation is needed, simply output the answer option.  
{question} A. {optionA} B. {optionB} ...  
Answer:

---

#### **Prompt 5: Case Analysis Prompt Template**

以下是一位病人的病例：{case}。  
根据病人的病例回答下面的问题。  
问题：{question}  
答案：

The following is a patient case: {case}.  
Based on the patient's case, answer the following question.  
Question: {question}  
Answer: