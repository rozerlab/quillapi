from flask_smorest import Blueprint

MASTER_PREFIX = "/api/v1"

common_blp = Blueprint("Common", __name__, url_prefix=f"/")

account_blp = Blueprint("Accounts", __name__, url_prefix=f"{MASTER_PREFIX}/user")

quill_blp = Blueprint("Quills", __name__, url_prefix=f"{MASTER_PREFIX}/quill")

auth_blp = Blueprint("Auth", __name__, url_prefix=f"{MASTER_PREFIX}/auth")
