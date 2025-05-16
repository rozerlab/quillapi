from . import id_mixin, timestamp_mixin, credientials_mixin
from app import db, bcrypter


class Accounts(id_mixin, credientials_mixin, timestamp_mixin, db.Model):

    __tablename__ = "Accounts"

    name = db.Column(db.String(length=256), nullable=False)

    quills = db.relationship("Quills", backref="user", lazy=True, cascade="all, delete")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):

        self._password = bcrypter.generate_password_hash(raw_password).decode("utf-8")

    def check_password(self, check_password):

        return bcrypter.check_password_hash(self._password, check_password)

    def __repr__(self):
        return f"Account<{self.id} | {self.username}>"
