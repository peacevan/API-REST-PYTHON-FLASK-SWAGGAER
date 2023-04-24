from flask import  Flask
from flask_restx import Api,Resource
from src.server.instance import server
from src.models.projects import project

app, api = server.app,server.api
projects_db = [
        {"id":1,'description': 'Projeto I'},
        {"id":2,'description': 'Projeto II'}
]

@api.route('/projects')
class projects(Resource):
    @api.marshal_list_with(project)
    def get(self,):
        return projects_db
    @api.expect(project,validade=True)
    @api.marshal_with(project)
    def post(self,):
        response= api.payload
        projects_db.append(response)
        return projects_db,200


