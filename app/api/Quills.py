from . import quill_blp
from flask.views import MethodView
from ._Api_Schema import NewQuill, DeleteQuill, UpdateQuill, GetQuill, QuillsList
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.Quill import Quills
from flask_smorest import abort

from app.utils import fetch_quill, fetch_user, try_commit
from sqlalchemy.exc import OperationalError, SQLAlchemyError

# from app.utils import User_from_jwt
from app import db


@quill_blp.route("/")
class QuillCreateAndMeta(MethodView):

    @quill_blp.arguments(NewQuill)
    @jwt_required()
    def post(self, args):
        """Add new Quill"""

        id_from_jwt = get_jwt_identity()

        try:

            new_quill = Quills(
                user_id=id_from_jwt,
                title=args["title"],
                desc=args["desc"],
                content=args["content"],
            )

            db.session.add(new_quill)

        except Exception as e:
            abort(500, message=f"{e}")

        try_commit()

        return {"message": f"{new_quill.id}:Created"}

    @quill_blp.response(200, QuillsList(many=True))
    @jwt_required()
    def get(self):
        """list the quills of user"""

        id_from_jwt = get_jwt_identity()

        try:

            # user = Accounts.query.get(id_from_jwt)
            # notes = user.notes  # List of note objects

            # for note in notes:
            #     print(note.id, note.title, note.description)

            all_quills = (
                db.session.query(Quills.id, Quills.title, Quills.desc)
                .filter(Quills.user_id == id_from_jwt)
                .all()
            )

        except OperationalError:
            abort(500, message=f"oprational problem at get list of quills")

        except SQLAlchemyError:
            abort(500, message=f"database ORM problem at get list of quills")

        except Exception as e:
            abort(500, message=f"{e}")

        if all_quills.__len__() <= 0:
            abort(404, message="empty not any quill")

        return [
            {"id": id, "title": title, "desc": desc} for id, title, desc in all_quills
        ]


@quill_blp.route("/<uuid:quill_id>")
class EditQuill(MethodView):

    @quill_blp.response(200, GetQuill)
    @jwt_required()
    def get(self, quill_id):
        """get entire quill"""

        id_from_jwt = get_jwt_identity()
        user = fetch_user(id_from_jwt)
        quill = fetch_quill(user.id, quill_id)

        return {
            "id": quill.id,
            "title": quill.title,
            "desc": quill.desc,
            "content": quill.content,
        }

    @quill_blp.arguments(UpdateQuill(partial=True))
    @jwt_required()
    def patch(self, args, quill_id):
        """update quill"""

        id_from_jwt = get_jwt_identity()
        user = fetch_user(id_from_jwt)
        quill = fetch_quill(user.id, quill_id)

        try:
            if args.get("title"):
                quill.title = args["title"]
            if args.get("desc"):
                quill.desc = args["desc"]
            if args.get("content"):
                quill.content = args["content"]

        except Exception as e:
            abort(500, message=f"{e}")

        try_commit()

        return {"message": f"{quill_id}:Updated"}

    @quill_blp.arguments(DeleteQuill)
    @jwt_required()
    def delete(self, args, quill_id):
        """delete the quill"""

        id_from_jwt = get_jwt_identity()
        user = fetch_user(id_from_jwt)
        quill = fetch_quill(user.id, quill_id)

        if quill.title == args["title"]:

            db.session.delete(quill)

        else:
            abort(400, message="enter title name carefully ")

        try_commit()

        return {"message": f"{quill_id}:deleted"}
