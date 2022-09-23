import googletrans
from googletrans import Translator
import time
translator = Translator()
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
startTime = time.time()
sentences = [
  '오늘 날씨 26도', '화장 안해도 이쁘다', '어떤 사람들은 종종 공항에서 여권을 잊어버립니다.',
  '메일을 다 비울까 아니면 안읽은 것만 지울까?',
  '메일 중에 안읽은 것만 지울까? 다 지울까?',
  '안읽은 메일만 지워 다지워?',
  '다 지울까 안읽은 메일만 지울까?',
  '전체를 비울까 안읽은 것만 비울까?',
  '안읽은 메일만 지울꺼야? 아니면 다 지울꺼야?',
  '어떻게 지울까? 안읽은거만? 전체 다?',
  '메일을 다 지울지 안읽은거만 지울지 알려주세요',
  '메일은 다 지울수도 있고, 안읽은거만 지울 수도 있어. 어떻게 할래?',
  '안읽은 메일만 지우든가, 다 지울 수 있는데 어떻게 할꺼야?',
  '지메일 쓸래, 네이버 메일 쓸래',
  '지메일을 쓸거야 네이버 메일을 쓸꺼야?',
  '지메일, 네이버 둘 중에 뭘 쓸래?',
  '네이버랑 지메일이 있는데 뭘 쓸래?',
  '네이버랑 지메일 중에 골라줄래?',
  '두 개 중에 골라줘 네이버랑 지메일.',
  '네이버 아니면 지메일 중에 어떤 이메일 써야될까?',
  '네이버 메일이랑 지메일 중에 어떤 걸 써?',
  '지메일 쓸래? 아님 네이버?',
]
# 167 sentence cause error handshake, reduce...
# 43 sentence work: about 25 second
# 20 sentence work: 11 second
result = translator.translate(sentences, dest='en')
endTime = time.time()
print('process: ', endTime - startTime)
# httpcore._exceptions.ConnectTimeout: _ssl.c:1074: The handshake operation timed out => google block your ip from spam request
# for trans in result:
#     print(f'{trans.origin} -> {trans.text}')