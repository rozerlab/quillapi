from . import auth_blp
from flask.views import MethodView
from ._Api_Schema import LoginSchema, LoginUser_Token
from app.models.Account import Accounts
from app import db
from flask_smorest import abort
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
from sqlalchemy.exc import OperationalError


@auth_blp.route("/login")
class Auth_login(MethodView):

    @auth_blp.arguments(LoginSchema)
    @auth_blp.response(200, LoginUser_Token)
    def post(self, args):
        """for login return access and refresh token"""
        try:
            user = (
                db.session.query(Accounts).filter_by(username=args["username"]).first()
            )

        except OperationalError:
            abort(500, message=f"oprational problem at login")

        except Exception as e:
            abort(500, message=f"{e}:at login")

        if not user:
            abort(404, message=f"Account of {args["username"]} not found")

        if user.check_password(args["password"]):

            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
        else:
            abort(400, message=f"password not match")

        return {"access_token": f"{access_token}", "refresh_token": refresh_token}


@auth_blp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    """return new access token"""
    user_id_jwt = get_jwt_identity()
    try:
        user = db.session.query(Accounts).filter_by(id=user_id_jwt).first()

    except OperationalError:
        abort(500, message=f"oprational problem at refresh")

    except Exception as e:
        abort(500, message=f"{e}:at refresh")

    if user:
        access_token = create_access_token(identity=user.id)
    else:
        abort(400, message="Account not found")

    return {"access_token": f"{access_token}"}
