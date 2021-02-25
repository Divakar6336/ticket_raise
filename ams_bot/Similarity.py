import os 
import json
import re

json_data={}
for file in os.listdir('data_json'):
    with open('data_json/' + file) as json_file:
        conversation_data = json.load(json_file)
    json_data.update(conversation_data)
    print("Training Data Added for file: "+file)

full_dataset=list(json_data.keys())

def jaccard_similarity(sent1, sent2):
    list1=sent1.split()
    list2=sent2.split()
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

def get_most_similar_sent(input_sent,threshold=0.2,default_response='I am sorry, but I do not understand.'):
    similarity=[]
    input_sent=re.sub('[^A-Za-z0-9]+', ' ', input_sent)
    for index,sent in enumerate(full_dataset):
        sent=re.sub('[^A-Za-z0-9]+', ' ', sent)
        score=jaccard_similarity(input_sent.lower(),sent.lower())
        similarity.append(score)
        # print(input_sent,sent,score )
    if max(similarity) > threshold:
        max_index=similarity.index(max(similarity))
        return json_data[full_dataset[max_index]]
    else: 
        return default_response

