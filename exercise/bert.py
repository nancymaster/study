from bert_serving.client import BertClient
import numpy as np
import math
from scipy.spatial.distance import cosine

class Nlper:

    def __init__(self, bert_client):
        self.bert_client = bert_client

    def get_text_similarity(self, base_text, compaired_text, algorithm='cosine'):
        if isinstance(algorithm, str) and algorithm.lower() == 'cosine':
            arrays = self.bert_client.encode([base_text, compaired_text])
            norm_1 = np.linalg.norm(arrays[0])
            norm_2 = np.linalg.norm(arrays[1])
            dot_product = np.dot(arrays[0], arrays[1])
            similarity = round(0.5 + 0.5 * (dot_product / (norm_1 * norm_2)), 2)
            return similarity

if __name__ == '__main__':
    from bert_serving.client import BertClient
    bc = BertClient()
    arr = ["你吃饭吗","你上厕所吗"]
    for i in range(len(arr)):
        print(i,arr[i])
    vecs = bc.encode(arr)
    a=1-cosine(vecs[0],vecs[1])
    print(a)
    # nlper = Nlper(bert_client=bc)
    # similarity = nlper.get_text_similarity('你好', '您不好')
    # print(similarity)