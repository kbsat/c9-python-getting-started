# 이 코드는 어떻게 Python으로 컴퓨터 비전 API를 호출하는 지 보여줍니다.
# 당신은 Computer Vision Analyze Image 메소드의 공식문서를 아래에서 찾을 수 있습니다.
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Python에서 간단하게 REST API 호출을 하기위해 requests 라이브러리를 사용하세요.
import requests

# 우리는 웹 서비스에서 전달받은 데이터를 읽기 위해 json 라이브러리가 필요합니다.
import json

# 우리는 Computer vision service의 주소가 필요합니다.
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"
# 호출하기 원하는 함수의 이름을 주소에 추가합니다.
address = vision_service_address + "analyze"

# 공식 문서에 나온 analyze image 함수의 내용에 따라서
# 세가지 선택적인 인자를 넣어줍니다. : language, details & visualFeatures
parameters = {'visualFeatures': 'Description,Color',
              'language': 'en'}

# 우리는 Computer vision service의 키가 필요합니다.
subscription_key = "xxxxxxxxxxxxxxxxxxxxxxx"

# 분석할 이미지를 담고있는 파일 객체를 얻기 위해 이미지 파일을 어줍니다.
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, 'rb').read()

# 공식 문서에 나온 analyze image 함수의 내용에 따라서
# HTTP 헤더에 subscription key와 content type을 지정해주어야합니다.
# 이미지를 직접 전달할 때에는 Content-Type에 application/octet-stream 을 넣어줍니다.
headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}

# 공식 문서에 나온 analyze image 함수의 내용에 따라서
# 함수를 호출하기 위해 HTTP POST를 사용해야합니다.
response = requests.post(address, headers=headers,
                         params=parameters, data=image_data)

# 만약 호출할 때 에러가 나온다면 예외를 일으키도록 합니다.
response.raise_for_status()

# 반환된 값을 JSON으로 출력합니다.
results = response.json()
print(json.dumps(results))

# color key에서 dominantColorBackground의 값을 출력합니다.
print()
print('dominantColorBackground')
print(results['color']['dominantColorBackground'])
