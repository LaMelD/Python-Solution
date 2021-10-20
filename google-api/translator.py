# googletrans==4.0.0rc1 버전 사용
from googletrans import Translator

translator = Translator()

lLines = [
    '실험중입니다.',
    '번역 테스트'
]

lRes = []
for nLine in lLines:
	try:
		oRes = translator.translate(nLine, src='en', dest='ko')
		lRes.append(oRes.text)
		print('processing...')
	except:
		print('error : ' + nLine)

print(lRes)