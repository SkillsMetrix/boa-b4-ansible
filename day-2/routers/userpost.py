from fastapi import FastAPI ,status,HTTPException,APIRouter
from .. import postschema
from random import randrange

router=APIRouter(tags=[" User POST Related Application"])

my_posts=[{"title":"welcome Title","content":"Demo Content","id":1}]

# search user
def findPost(id):
    for i,p in enumerate(my_posts):
        if(p['id']== id):
            return i

# load all the data
@router.get('/post/loadusers')
def loadUsers():
    return {'message':my_posts}

# get specific data
@router.get('/loaduser/{id}')
def loadUser(id:int):
    foundData=findPost(id)
    if not foundData:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='OOPS....Given Id not found')
    else:
        return {'data':foundData}

# delete specific data
@router.delete('/deleteuser/{id}')
def deleteUser(id:int):
    foundData=findPost(id)
    print(foundData)
    if not foundData:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='OOPS....Given Id not found')
    else:
        my_posts.pop(foundData)
        return {'data':'user deleted'}


# add the new data
@router.post('/registeruser',status_code=status.HTTP_201_CREATED)
def register(payload: postschema.UserPost):
    #convert recieveing data into key:value pair
    userdata=payload.model_dump()
    # update the id with rand range
    userdata['id']=randrange(0,1000)
    # update the array with new data
    my_posts.append(userdata)
    return {'message':userdata}

# update specific data
@router.put('/updateuser/{id}')
def updateUser(id:int,payload:postschema.UserPost):
    foundData=findPost(id)
   
    if not foundData:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='OOPS....Given Id not found')
    else:
        userdata=payload.model_dump()
        # checking the ID what user has passed with existing data
        userdata['id']=id
        # replacing that existing data with new data recieved from the client
        my_posts[foundData]= userdata
        return {'data':userdata}