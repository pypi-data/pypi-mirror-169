from pydantic import BaseModel, EmailStr
from basemodels.user import User
from typing import List,Optional
from basemodels.experience.employmentcert import ExperienceModel, ExperienceModelE
from pr.webform.prmodel import PrModel
from pr.webform.i5406 import F5406
from pr.webform.i5562 import F5562
from pr.webform.i5669 import F5669
from pr.webform.i0008 import F0008
from pr.webform.application import Application

def user_schema(user):
    return {
        "_id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "phone": user["phone"],
        # "password": user["password"],
        "role": user.get("role"),
        "permission": user.get("permission"),
    }


def users_schema(users):
    return [user_schema(user) for user in users]


class ShowUser(BaseModel):
    _id: str
    username: str
    email: EmailStr
    phone: str
    password: str
    role: str
    permission: list


class Login(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    # email: str | None = None
    email: str


class Permission(BaseModel):
    user_email: EmailStr
    permissions: List[str]
    remove: bool


class Role(BaseModel):
    user_email: EmailStr
    role: str

class EmploymentCertificate(BaseModel):
    """Generate employment certificate based on input company"""
    source:dict
    company:str
    language:str
    
    @property
    def data(self):
        return ExperienceModel(**self.source)
    
class EmploymentCompany(BaseModel):
    """Get companies list and pick a company for generating certificate"""
    source:dict
    language:str
    
    @property
    def data(self):
        return ExperienceModel(**self.source)
    
class PRFormRequest(BaseModel):
    pa:dict
    sp:Optional[dict]
    dps:List[dict]
    model:str
    models:dict={
        '5406':F5406,
        '5562':F5562,
        '5669':F5669,
        '0008':F0008
    }

    def data(self):
        pa=PrModel(**self.pa)
        sp=PrModel(**self.sp) if self.sp else None
        dps=[PrModel(**dp) for dp in self.dps]
        the_model=self.models.get(self.model)
        if the_model:
            return the_model(pa,sp,dps).fill()
        raise ValueError(f"{self.model} is not a valid model.")

class PickAppRequest(BaseModel):
    pa:dict
    
    def data(self):
        pa=PrModel(**self.pa)
        app=Application(pa)
        return app.pick()
