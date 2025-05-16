from ._Api_Schema import (
    At_Change_email,
    NewUser,
    Required_At_Del,
    At_Change_password,
    CreateUser_Token,
    Get_User,
)
from flask.views import MethodView
from . import account_blp
from flask_smorest import abort
from app.models.Account import Accounts
from app import db
from flask_jwt_extended import (
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    create_access_token,
)
from app.utils import fetch_user, try_commit
from sqlalchemy import or_
from sqlalchemy.exc import OperationalError, SQLAlchemyError


# add new user
@account_blp.route("/", methods=["POST"])
@account_blp.arguments(NewUser)
@account_blp.response(201, CreateUser_Token)
def create_and_login(args):
    """Create new user Account"""
    try:
        existing_user = (
            db.session.query(Accounts)
            .filter(
                or_(
                    Accounts.email == args["email"],
                    Accounts.username == args["username"],
                )
            )
            .first()
        )
    except OperationalError:
        abort(500, message=f"oprational problem")
    except Exception as e:
        abort(500, message=f"{e}")
    if existing_user:
        if existing_user.username == args["username"]:
            abort(409, message=f"username '{args["username"]}' not avalable !")
        if existing_user.email == args["email"]:
            abort(409, message=f"email '{args["email"]}' not avalable !")
    try:
        newuser = Accounts(
            name=args["name"],
            email=args["email"],
            username=args["username"],
            password=args["password"],
        )
        db.session.add(newuser)
        # generate token based on data
        access_token = create_access_token(identity=newuser.id)
        refresh_token = create_refresh_token(identity=newuser.id)
    except SQLAlchemyError:
        abort(500, message=f"oprational problem at creating account")
    except Exception as e:
        abort(500, message=f"{e}")

    try_commit()

    return {"access_token": access_token, "refresh_token": refresh_token}


@account_blp.route("/account")
class UserAccount(MethodView):

    # get account
    @account_blp.response(200, Get_User)
    @jwt_required()
    def get(self):
        """Get all Account details"""

        id_from_jwt = get_jwt_identity()

        user = fetch_user(id_from_jwt)

        return {
            "id": user.id,
            "name": user.name,
            "username": user.username,
            "email": user.email,
        }

    # delete request
    @account_blp.arguments(Required_At_Del)
    @account_blp.response(202)
    @jwt_required()
    def delete(self, args):
        """Delete Account"""

        id_from_jwt = get_jwt_identity()

        user = fetch_user(id_from_jwt)

        if user.username == args["username"] and user.check_password(args["password"]):

            db.session.delete(user)

        else:
            abort(401, message="invalid credentials")

        try_commit()
        return {"message": f"{id_from_jwt}:Deleted"}


# change password
@account_blp.route("/password", methods=["PATCH"])
@account_blp.arguments(At_Change_password)
@account_blp.response(200)
@jwt_required()
def changepassword(args):
    """Change password"""

    id_from_jwt = get_jwt_identity()

    user = fetch_user(id_from_jwt)

    if user.check_password(args["password"]):
        user.password = args["newpassword"]
    else:
        abort(401, message="invalid credentials")

    try_commit()

    return {"message": f"{user.id}:Password Changed"}


# change email
@account_blp.route("/email", methods=["PATCH"])
@account_blp.arguments(At_Change_email)
@account_blp.response(200)
@jwt_required()
def change_email(args):
    """Change email"""

    id_from_jwt = get_jwt_identity()

    user = fetch_user(id_from_jwt)
    _current_email = user.email

    try:
        _already_exists = (
            db.session.query(Accounts).filter_by(email=args["newemail"]).first()
        )

    except OperationalError:
        abort(500, message=f"oprational problem")

    except SQLAlchemyError:
        abort(500, message=f"Database ORM problem")

    except Exception as e:
        abort(500, message=f"{e}")

    # check entered email is same as existing
    if _current_email != args["email"]:
        abort(406, message="Entred email is not same as existing")
    # email is not used by another
    if _already_exists:
        abort(409, message=f"Use another email insted of {args["newemail"]}")
    # change email if password is matched
    if user.check_password(args["password"]):
        user.email = args["newemail"]
        try_commit()
    else:
        abort(401, message="your password is not matched")

    return {"message": f"{user.id}:{user.email}:Updated"}
