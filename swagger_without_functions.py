from flask import Flask
from flask_restplus import Resource, Api, fields

app = Flask(__name__)                 
api = Api(app)

parametros = api.model('Bookmarks', {'title': fields.String("GRÊMIO."), 'url': fields.String("www.gremio.com")})

@api.route('/bookmarks')                   
class Bookmarks(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')           
    def get(self):                     
        return SITES, 200

    @api.expect(parametros)
    @api.response(201, 'Object created', parametros)
    @api.response(400, 'Validation Error')
    def post(self):
        return 
@api.route('/bookmarks/<id>')
class id_bookmarks(Resource):
    @api.response(200, 'update success ')
    @api.response(400, 'Not Found')
    @api.expect(parametros)
    def put(self, id):
        return 
    @api.response(200, 'Deleted successfully')
    @api.response(400, 'Not Found')
    def delete(self, id):
        return
@api.route('/bookmarks/<title>')
class title_bookmarks(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Not Found')  
    def get(self, title):
        return

if __name__ == '__main__':
    app.run(debug=True) 
    