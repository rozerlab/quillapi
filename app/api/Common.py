
from . import common_blp
from . import MASTER_PREFIX


@common_blp.route("/", methods=["GET"])
@common_blp.response(200)
def home_endpoint():
    return {"message": "listning done at / "}


@common_blp.route(f"/{MASTER_PREFIX}", methods=["GET"])
@common_blp.response(200)
def master_endpoint():
    return {"message": "listning done at /api/v1 "}
