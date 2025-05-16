from marshmallow import Schema, fields


class Get_User(Schema):
    id = fields.UUID(required=True)
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)


class _UserBase(Schema):

    name = fields.Str(required=True)
    email = fields.Email(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    class Meta:
        ref_name = "UserBaseSchema"


class NewUser(_UserBase):

    class Meta:
        ref_name = "NewUserSchema"


class Required_At_Del(Schema):

    username = fields.Str(required=True)
    password = fields.Str(required=True)


class _Password_based(Schema):
    password = fields.Str(required=True)

    class Meta:
        ref_name = "PasswordOperation"


class At_Change_password(_Password_based):

    newpassword = fields.Str(required=True)

    class Meta:
        ref_name = "ChangePassword"


class At_Change_email(_Password_based):

    email = fields.Email(required=True)
    newemail = fields.Email(required=True)

    class Meta:
        ref_name = "ChangeEmail"


# NOTES SPECFIC


class QuillsList(Schema):
    id = fields.UUID(required=True)
    title = fields.Str(required=True)
    desc = fields.Str(required=True)


class _QuillBase(Schema):

    title = fields.Str(required=True)
    desc = fields.Str(required=True)
    content = fields.Str(required=True)

    class Meta:
        ref_name = "NoteBaseSchema"


class NewQuill(_QuillBase):

    class Meta:
        ref_name = "NewNoteSchema"


class GetQuill(_QuillBase):

    id = fields.Str(required=True)

    class Meta:
        ref_name = "GetNoteSchema"


class UpdateQuill(_QuillBase):

    class Meta:
        ref_name = "UpdateNoteSchema"


class DeleteQuill(Schema):

    title = fields.Str(required=True)


# AUTH SCHEMA


class TokenSchema_Base(Schema):
    access_token = fields.Str(required=True)
    refresh_token = fields.Str(required=True)

    class Meta:

        ref_name = "TokenSchemaBase"


class CreateUser_Token(TokenSchema_Base):

    class Meta:
        ref_name = "CreateUserToken"


class LoginUser_Token(TokenSchema_Base):

    class Meta:
        ref_name = "LoginUserToken"


class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
