# API 호출

웹 서버에서 호스팅된 프로그램에서 호출하는 함수를 호출할 수 있습니다. [Microsoft Azure Cognitive Services](https://docs.microsoft.com/azure/cognitive-services/?WT.mc_id=python-c9-niner)는 코드에서 호출하여 당신의 앱이나 웹에 지성을 추가할 수 있는 많은 API를 담고 있습니다.

코드 예제에서는 [컴퓨터 비전](https://docs.microsoft.com/azure/cognitive-services/computer-vision/?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner)의 [Analyze Image](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa0) 함수를 호출해 볼 것입니다.

API를 호출하기 위한 요구사항

- [API Key](https://azure.microsoft.com/try/cognitive-services/?WT.mc_id=python-c9-niner)가 여러분에게 API를 호출을 허락해줍니다.
- 서비스의 주소나 종단점
- 호출할 메소드의 함수 이름을 [API 문서](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner)에서 찾습니다.
- [API 문서](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner)에서 함수에 넣어야할 인자들을 찾습니다.
- [API 문서](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner)에서 HTTP 헤더에 대한 내용을 찾습니다.
