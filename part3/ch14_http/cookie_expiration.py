from flask import Flask
from flask import request
from flask import make_response
import uuid
app = Flask(__name__)


@app.route('/')
def hello_world():
    cookies = request.cookies

    if 'sessionId' in cookies:
        response = make_response('기존 연결입니다: sessionId={0}'.format(cookies['sessionId']))
    else:
        new_session_id = str(uuid.uuid4())
        response = make_response('새 연결입니다: sessionId={0}'.format(new_session_id))
        response.set_cookie('sessionId', new_session_id)

        # cookie 만료 시간(max_age) 5초
        response.set_cookie('sessionId', new_session_id, max_age=5)

    return response


app.run()

# https://thecodinglog.github.io/web/2020/08/11/what-is-session.html
# 서버가 클라이언트 ID를 어떤 방법으로 추적할 것인지 정의한 것을 세션 트래킹 모드라고 합니다.
# 트래킹 모드에는 쿠키 사용 모드, URL Rewriting 모드, SSL 모드 가 있는데 대부분 서버에서 쿠키 사용 모드를 기본값으로 하고 있고 이 모드 사용을 권장하고 있습니다.
