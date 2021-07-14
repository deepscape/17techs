import json
from dataclasses import dataclass
import datetime
from flask import request, Flask, Blueprint

bp = Blueprint('v1', __name__, url_prefix='/v1')

posts = {}
post_number = 1


@dataclass
class BlogPost:
    title: str  # 제목
    contents: str  # 내용
    date: str  # 작성/마지막 업데이트 날짜


@bp.route('/posts', methods=['POST'])
def write_post():
    request_json = request.get_json()
    title = request_json.get('title', '')
    contents = request_json.get('contents', '')

    if len(title) == 0 or len(contents) == 0:
        return 'Bad request', 400

    global post_number  # 전역 변수 명시

    # 실제 시간을 외부 설정에 영향받지 않는 고정된 날짜 규격으로 변환해 사용
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('title={0}, contents={1}, date={2}, post_number={3}'.format(title, contents, now, post_number))

    # 실무에서는 SQLITE, MySQL 등을 이용해 저장
    posts[post_number] = BlogPost(title=title, contents=contents, date=now)
    post_number = post_number + 1

    return 'OK', 200


app = Flask(__name__)
app.register_blueprint(bp)
app.url_map.strict_slashes = False
app.run()
