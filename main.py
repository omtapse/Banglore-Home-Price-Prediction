from flask import Flask,request,jsonify, render_template
import util
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/inner-page.html")
def innerpage():
    return render_template('inner-page.html')

@app.route('/get_location_names')
def get_location_names():
    responce = jsonify({
        'locations':util.get_location_names()
    })
    responce.headers.add('Access-control-Allow-Origin','*')
    return responce

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft= float(request.form['total_sqft'])
    location= request.form['location']
    bhk= float(request.form['bhk'])
    bath= float(request.form['bath'])



    responce =jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    responce.headers.add('Access-Control-Alow-Origin','*')
    return responce

if __name__ == '__main__':
    print("Starting point")
    util.load_saved_artificates()
    app.run()

app.run(debug=True)