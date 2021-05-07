from pydantic import BaseModel, validator

from app.excpetions.ParamsException import ParamsError


class TestCaseForm(BaseModel):
    id: int = None
    catalogue: str
    priority: str
    url: str
    name: str
    tag: str = None
    body: str = None
    request_header: str = None
    request_method: str = None
    status: int
    project_id: int
    request_type: int

    @validator("catalogue", "priority", "status", "project_id", "request_type", "url", "name")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        return v