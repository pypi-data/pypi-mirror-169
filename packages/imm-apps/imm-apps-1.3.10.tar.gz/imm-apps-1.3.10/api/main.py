import context
from fastapi import FastAPI

# import uvicorn
from api.routers import user, case, authentication,prwebform

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(case.router)
app.include_router(prwebform.router)

# uvicorn.run(app, host="localhost", port=8000)
