import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from mangum import Mangum
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class OneTable(Model):
    '''
    DynamoDB works best with a single table. This table. Use this table to model
    other data requests.
    '''
    class Meta:
        table_name = 'DYNAMODB_TABLE_NAME'

    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)


@app.get("/", response_class=HTMLResponse)
def cats(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/dogs/{id}")
def dog(id):
    return "Dog"


@app.get("/health")
def health():
    return {"status": "Success"}


handler = Mangum(app)
