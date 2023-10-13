from flask import Flask, jsonify, request
from etl import etl_data_obj

app= Flask(__name__)

@app.route('/etl', methods=['GET'])
def get_data():
  if request.method == 'GET':
      d=etl_data_obj.get_details()
      print('value returned', d)
      return jsonify(d)

if __name__=="__main__":
   app.run(debug=True)