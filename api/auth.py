import fastapi


from fastapi import Depends
from sqlalchemy.orm import Session

from api.utils.users import get_user_by_email
from db.db_setup import get_db
from schemas.user import UserLoginSchema



router = fastapi.APIRouter()

@router.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema,db: Session = Depends(get_db)):
    user = get_user_by_email(db, user.email)

