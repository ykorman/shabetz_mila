from bottle import route, request, run, get, template, static_file, post, response

import server

gameStore = server.loadGameStore("sample_db.dat")

@route('/shabetz_mila')
@route('/shabetz_mila/index.html')
def main_html():
    return static_file("ui.html", root="./")

@route('/<script>.js')
def app_js(script):
    if script in ("app", "jquery.cookie"):
        return static_file(script + ".js", root="./")
    else:
        abort(404, "No such script")
   
@post('/shabetz_mila/login')
def login_submit():
    name     = request.forms.get('username')
    password = request.forms.get('password')
    if (name == "abc"):
        response.set_cookie("username", name)
        return "success"
    else:
        return "failure"

    
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


run(host='0.0.0.0', port=8181)