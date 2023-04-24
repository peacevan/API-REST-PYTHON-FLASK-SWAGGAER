from flask_restx import fields
from src.server.instance import server


project = server.api.model('project',{
        "id": fields.String(description="Id do projeto"),
        "description":fields.String(requered=True,min_length=1,max_length=200,description='descrição do projeto')

 })