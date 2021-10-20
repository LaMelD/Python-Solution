import json

dFruit = {
    'first': 'banana',
    'second': 'apple',
    'third': 'orange',
    'fourth': 'tomato'
}

print(json.dumps(dFruit, sort_keys=True, indent=4))
# json.dumps
# sort_keys : 키값으로 정렬할지 T/F
# indent : 음이 아닌 정수나 문자열이면 들여쓰기 되어 인쇄된다. 양수라면 해당 수만큼 스페이스 들여쓰기되어 인쇄


# json.JSONDecoder()
# json.JSONEncoder()