from dao.UserDao import UserDao
from flask import Flask
from flask import make_response, request


app = Flask(__name__)
app.json.ensure_ascii = False


def wp_dumps(data=None, errno=0, errmsg="Success", status=200):
    return make_response(
        # json.dumps({
        #     'errno': errno,
        #     'errmsg': errmsg,
        #     'data': data,
        # }, ensure_ascii=False, separators=(',', ':')),
        {
            "errno": errno,
            "errmsg": errmsg,
            "data": data,
        },
        status,
    )


@app.route("/")
def hello_world():
    return "hello_world"


@app.route("/v1/users", methods=["GET"])
def get_users():
    page = request.args.get("page", 1)
    limit = request.args.get("limit", 10)
    userDao = UserDao()
    users = userDao.get_users(page, limit)
    return wp_dumps(users)


@app.errorhandler(404)
def not_found(e):
    return wp_dumps(errno=404, errmsg=str(e), status=404)


@app.errorhandler(Exception)
def server_error(e):
    return wp_dumps(errno=500, errmsg=str(e), status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
