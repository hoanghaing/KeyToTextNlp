import googletrans
from googletrans import Translator

translator = Translator()
sentences = ['Bienvenu', 'Comment allez-vous', 'je vais bien']
sentences = ['오늘 날씨 26도', '화장 안해도 이쁘다', '어떤 사람들은 종종 공항에서 여권을 잊어버립니다.']
result = translator.translate(sentences, dest='en')
for trans in result:
    print(f'{trans.origin} -> {trans.text}')
# print(result)
# pip install googletrans==3.1.0a0
# 오늘 날씨 26도
# 화장 안해도 이쁘다
# 어떤 사람들은 종종 공항에서 여권을 잊어버립니다.