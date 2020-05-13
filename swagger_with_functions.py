from flask import Flask
from flask_restplus import Resource, Api, fields

app = Flask(__name__)                 
api = Api(app, title = "BOOKMARKS", description="design of an api")                        

SITES = [
     {'id': 1, 'title': 'Google', 'url': 'http://google.com'},
     {'id': 2, 'title': 'Yahoo', 'url': 'http://yahoo.com'}
]

parametros = api.model('Bookmarks', {'title': fields.String("GRÊMIO."), 'url': fields.String("www.gremio.com")})

@api.route('/bookmarks')                   
class Bookmarks(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')            
    def get(self):                     
        return SITES
    @api.expect(parametros)
    @api.response(201, 'Object created', parametros)
    @api.response(400, 'Validation Error')
    def post(self):
        new_bookmark = api.payload
        new_bookmark['id'] = len(SITES) + 1
        SITES.append(new_bookmark)
        return SITES[-1]
@api.route('/bookmarks/<id>')
class id_bookmarks(Resource):
    @api.response(200, 'update success ')
    @api.response(400, 'Not Found')
    @api.expect(parametros)
    def put(self, id):
        updatebookmarks = api.payload
        id = int(id)
        sitez = [s for s in SITES if s['id'] == id]
        sitez[0]['title'] = updatebookmarks['title']
        sitez[0]['url'] = updatebookmarks['url']
        return sitez[0]

    @api.response(200, 'Deleted successfully')
    @api.response(400, 'Not Found')
    def delete(self, id):
        id = int(id)
        sitez = [s for s in SITES if s['id'] == id]
        SITES.remove(sitez[0])
        return SITES
@api.route('/bookmarks/<title>')
class title_bookmarks(Resource):
    @api.response(200, 'Success')
    @api.response(400, 'Not Found')  
    def get(self, title):
        sitez = [s for s in SITES['title'] if s == title]
        return sitez[0]

if __name__ == '__main__':
    app.run(debug=True) 
    