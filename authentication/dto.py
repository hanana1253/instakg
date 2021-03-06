from dataclasses import dataclass

@dataclass
class SignupDto():
    userid: str
    userpw: str
    userpw_check: str
    name: str

@dataclass
class LoginDto():
    userid: str
    userpw: str

@dataclass
class EditDto():
    my_pk: int
    introduction: str
