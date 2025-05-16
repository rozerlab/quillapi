from app import db
from app.models.Account import Accounts
from app.models.Quill import Quills
from flask_smorest import abort
from sqlalchemy.exc import (
    SQLAlchemyError,
    NoResultFound,
    MultipleResultsFound,
    IntegrityError,
    DataError,
    OperationalError,
    InterfaceError,
    InternalError,
)


def fetch_user(jwt_id):

    try:

        _user = db.session.query(Accounts).filter_by(id=jwt_id).first()

    except NoResultFound:

        abort(404, message="user is not found")

    except MultipleResultsFound:

        abort(500, message="multiple result is found try to fix")

    except SQLAlchemyError as e:

        abort(500, message=f"Data Base Error :{e}")

    if _user:
        return _user
    abort(404, message="User not found")


def fetch_quill(passed_user_id, passed_quill_id):

    try:

        _quill = (
            db.session.query(Quills)
            .filter_by(user_id=passed_user_id, id=passed_quill_id)
            .first()
        )

    except NoResultFound:

        abort(404, message="Quill is not found")

    except MultipleResultsFound:

        abort(500, message="multiple result is found try to fix")

    except SQLAlchemyError as e:

        abort(500, message=f"Data Base Error :{e}")

    if _quill:
        return _quill
    abort(404, message=f"quill '{passed_quill_id}' not found")


def try_commit():

    try:

        db.session.commit()

    except IntegrityError:
        db.session.rollback()
        abort(500, message="schema structure rule violates : integrity problem")

    except DataError:
        db.session.rollback()
        abort(
            500,
            message="meta of data is not good violates length etc.: data problem",
        )
    except OperationalError:
        db.session.rollback()
        abort(500, message="unaxpected timeout or connection : operational problem")

    except InternalError:
        db.session.rollback()
        abort(500, message="internal process invalid state : internal problem")

    except InterfaceError:
        db.session.rollback()
        abort(500, message="driver problems psycopg2  : interface problem")

    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, message=f"sqlalchemy base error  : Sqlalchemy:{e}")

    except Exception as e:
        db.session.rollback()
        abort(500, message=f"system error  : Exception:{e}")
