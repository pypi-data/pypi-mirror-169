from api.show import show_exception
from basemodels.user import User
from fastapi import APIRouter, Depends
from system.config import db
from  api import schemas
from api.routers.authentication import permission_check
from api import oauth2
from api import schemas
user_collection = db.user
router = APIRouter(
    prefix="/pr", tags=["PR Webform"], responses={404: {"description": "Nof found"}}
)

@router.post("/pickapp")
async def pickapp(request:schemas.PickAppRequest, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("run", current_user)
    try:
        return request.data()
    except Exception as e:
        show_exception(e)
        
@router.post("/webform")
async def webform(request:schemas.PRFormRequest, current_user: User = Depends(oauth2.get_current_user)):
    permission_check("run", current_user)
    try:
        return request.data()
    except Exception as e:
        show_exception(e)

