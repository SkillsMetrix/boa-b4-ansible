from fastapi import FastAPI ,status,HTTPException
from . routers import userpost,projectpost
 
app= FastAPI()
# registering your application to crudapp
app.include_router(userpost.router)
app.include_router(projectpost.router)




