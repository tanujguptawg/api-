from marshmallow import Schema,fields


class PlainSignupSchema(Schema):
    name = fields.Str(required=True, unique = True)
    password = fields.Str(required=True)
    conf_password = fields.Str(required=True)

class LoginSchema(Schema):
    username = fields.Str(required=True, unique = True)
    password = fields.Str(required=True)

class SignupSchema(PlainSignupSchema):
    # role_type=fields.Int(dump_only=True, dump_default=2)
    role=fields.List(fields.Nested(lambda:PlainSignupSchema(),dump_only=True))

# class GaganSchema(Schema):

