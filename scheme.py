from pydantic import BaseModel


class PersonInfo(BaseModel):
    name: str
    surname: str
    age: int
    job_post: str
    access_level: int


class SignUpData(BaseModel):
    photo: str
    info: PersonInfo


class LogInData(BaseModel):
    photo: str
