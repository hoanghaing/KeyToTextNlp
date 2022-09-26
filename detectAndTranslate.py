import googletrans
from googletrans import Translator
# pip install deep-translator
# import time
# translator = Translator()
# sentences = ['Bienvenu', 'Comment allez-vous', 'je vais bien']
# sentences = []
# result = translator.translate(sentences, dest='en')
# for trans in result:
#     print(f'{trans.origin} -> {trans.text}')
# print(result)
# pip install googletrans==3.1.0a0
# 오늘 날씨 26도
# 화장 안해도 이쁘다
# 어떤 사람들은 종종 공항에서 여권을 잊어버립니다.
# startTime = time.time()
# sentences = [
#   '오늘 날씨 26도', '화장 안해도 이쁘다', '어떤 사람들은 종종 공항에서 여권을 잊어버립니다.',
#   '메일을 다 비울까 아니면 안읽은 것만 지울까?',
#   '메일 중에 안읽은 것만 지울까? 다 지울까?',
#   '안읽은 메일만 지워 다지워?',
#   '다 지울까 안읽은 메일만 지울까?',
#   '전체를 비울까 안읽은 것만 비울까?',
#   '안읽은 메일만 지울꺼야? 아니면 다 지울꺼야?',
#   '어떻게 지울까? 안읽은거만? 전체 다?',
#   '메일을 다 지울지 안읽은거만 지울지 알려주세요',
#   '메일은 다 지울수도 있고, 안읽은거만 지울 수도 있어. 어떻게 할래?',
# ]
# For korean case
# 167 sentence cause error handshake, reduce...
# 43 sentence work: about 25 second.
# 20 sentence work: 11 second.
# 10 sentence work: 4second

# sentences = [
#   'The impact of global warming is far greater than just increasing temperatures. It modifies rainfall patterns, amplifies coastal erosion, melts ice caps and alters the ranges of some infectious diseases.',
#   'Children born in poor families are forced to work not only for their own survival but also for the irfamily',
#   'So far, there are no known ways to prevent tsunamis, making them extremely dangerous',
#   'Burgers, chips, pastries, chow mein, French fires, chocolate bars, soft drinks and hot dogs, etc. fall in this category',
#   'Another ingredient is the amount of sugar that is added to it',
#   'They may fail once or twice or even repeatedly; still they carry on bravely and firmly until success comes to them in the end',
#   'Tsunamis can savagely attack coastlines, causing devastating property damage and loss of life',
#   'Indebtedness of the parents also compels poor parents to their children employed as labourers in agricultural forms, factories, brick kilns and as domestic servants',
#   'Cutting down pollution from car emissions and power plants will decrease the rate of global warming to a great ex tent',
#   'Research done by UNICEF indicated illegal marriage of almost 82 percent of girls',
# ]
# result = translator.translate(sentences, dest='en')
# endTime = time.time()
# print('process: ', endTime - startTime)
# 10 english sentences -> 3s
# httpcore._exceptions.ConnectTimeout: _ssl.c:1074: The handshake operation timed out => google block your ip from spam request
# for trans in result:
#     print(f'{trans.origin} -> {trans.text}')

from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto', target='en').translate("메일은 다 지울수도 있고, 안읽은거만 지울 수도 있어. 어떻게 할래?")  # output -> Weiter so, du bist großartig
print(translated)