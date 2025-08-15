from pydantic import BaseModel

class ClientBase(BaseModel):
    project_name: str
    address: str
    phone: str
    email: str
    website: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass
