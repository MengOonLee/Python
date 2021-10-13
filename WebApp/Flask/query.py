from flask import Flask, request

app = Flask(__name__)

@app.route('/query')
def query():
    language = request.args.get('language')
    framework = request.args['framework']
    website = request.args.get('website')
    return """
        <h1>The language value is: {}</h1>
        <h1>The framework value is: {}</h1>
        <h1>The website values is {}</h1>
        """.format(language, framework, website)

@app.route('/form', methods=['Get', 'Post'])
def form():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return """
            <h1>The language value is: {}</h1>
            <h1>The framework value is: {}</h1>
            """.format(language, framework)
    else:
        language = request.args.get('language')
        framework = request.args['framework']
        return """
            <h1>The language value is: {}</h1>
            <h1>The framework value is: {}
            """.format(language, framework)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
