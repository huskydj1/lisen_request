from flask import Flask, request

app = Flask(__name__)

@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route("/result", methods = ["POST"])
def result():
    print(request.files)
    data = request.files['audio_data'].read()
    print(data)
    
    return 'https://avatars.dicebear.com/api/bottts/:seed.svg'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    # app.run(debug=True, port=5000)
    app.run(host='0.0.0.0', port=80, ssl_context='adhoc')

    
    
