from bottle import route, request, run, get, template, static_file, post

@route('/shabetz_mila')
def main_html():
    return static_file("ui.html", root="./")

@route('/app.js')
def app_js():
    return static_file("app.js", root="./")
   
@post('/shabetz_mila/login')
def login_submit():
    name     = request.forms.get('username')
    password = request.forms.get('password')
    if (name == "abc"):
        return "success"
    else:
        return "failure"
    #return "username=%s password=%s" % (name, password)

    
# samples

@route('/hello/<name>')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)
    
@route('/form')
def construct_form():
    return '''

<!DOCTYPE html>
<html>
<head>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            $('form').submit(function(e) {
                $.ajax({
                    type: 'POST',
                    url: '/ajax',
                    data: $(this).serialize(),
                    success: function(response) {
                        $('#ajaxP').html(response);
                    }
                });
                e.preventDefault();
            });
        });
    </script>
</head>
<body>
    <form method="POST" action="/ajax">
        <input id="ajaxTextbox" name="text" type"text" />
        <input id="ajaxButton" type="submit" value="Submit" />
    </form>
    <p id="ajaxP">Nothing to see here.</p>
</body>
</html>

    '''

@route('/ajax', method='POST')
def ajaxtest():
    theText = request.forms.text
    if theText:
        return theText
    return "You didn't type anything."


run(host='localhost', port=8181)