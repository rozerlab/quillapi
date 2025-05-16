from app import db
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class id_mixin:

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    def get_id(self):
        return self.id


class timestamp_mixin:

    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )


class credientials_mixin:
    email = db.Column(db.String(length=256), nullable=False, unique=True)
    username = db.Column(db.String(length=64), nullable=False, unique=True)
    # _password is just for orm but in database it is store as password
    _password = db.Column("password", db.String(), nullable=False)
