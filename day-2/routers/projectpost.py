from fastapi import FastAPI ,status,HTTPException,APIRouter
 
 

router=APIRouter(tags=[" Projects Related Application"])

my_projects=[{"title":"Finance Application","content":"US and UK Projects","id":101}]


# load all the Projects
@router.get('/project/loadprojects')
def loadProjects():
    return {'message':my_projects}

