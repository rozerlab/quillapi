from app import db
from . import id_mixin, timestamp_mixin
from sqlalchemy.dialects.postgresql import UUID


class Quills(id_mixin, timestamp_mixin, db.Model):

    __tablename__ = "Quills"

    user_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("Accounts.id"), nullable=False
    )

    title = db.Column(db.String(150), nullable=False)

    desc = db.Column(db.String(256), nullable=False)

    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Note<{self.id} | {self.title}>"
