from pydantic import ValidationError
from fastapi import HTTPException
from utils.utils import print_validation_error


def show_exception(e: Exception,language="English"):
    if type(e) == ValidationError:
        raise HTTPException(status_code=422, detail=print_validation_error(e,language=language))
    else:
        raise HTTPException(status_code=422, detail=e)
