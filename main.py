from flask import Flask, jsonify ,request
from flask_restful import Api,Resource

app = Flask(__name__)
#alternate method
#api=Api(app)
#class HelloWorld(Resource):
 #   def get(self):
  #      data={"data":"hello world"}
   #     return data
   
@app.route('/hello', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data={"data": "hello world"}
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
 