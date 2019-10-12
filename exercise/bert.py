from bert_serving.client import BertClient
import numpy as np
import math
# bc = BertClient()
# test = bc.encode(['我想要离婚怎么办', '怎么样离婚呢'])
# #test = bc.encode(['123123'])
# print(test)


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

def age(*arg):
    num=lambda a,b: a*b
    print(num(2,2))
if __name__ == '__main__':
    # bc = BertClient()
    # nlper = Nlper(bert_client=bc)
    # similarity = nlper.get_text_similarity('你好', '他要死了')
    # print(similarity)
    #
    # prefix_q = '##### **Q:** '
    # with open('README.md',encoding='gb18030',errors='ignore') as fp:
    #     questions = [v.replace(prefix_q, '').strip() for v in fp if v.strip() and v.startswith(prefix_q)]
    #     print('%d questions loaded, avg. len of %d' % (len(questions), np.mean([len(d.split()) for d in questions])))
    #     print(questions)

    a=[1,2,3,4,5]
    print(a[-1:])