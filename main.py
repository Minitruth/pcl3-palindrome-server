import cgi


def check_palindrome(word):
    return False  # TODO


def application(environ, start_response):
    params = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)

    word = params.getfirst('word', default=None)

    if word is None:
        output = """\
<h1>Palindrome Checker</h1>
<form action="test.py" method="get">
    <label for="word">What word do you want to check?</label>
    <input name="word" id="word">
    <button>Submit</button>
</form>
"""
    else:
        is_palindrome = check_palindrome(word)
        output = """\
        <p><a href="test.py">&larr; Back</a></p>
        <h1>Result</h1>
        <!-- TODO -->
        """

    status = "200 OK"
    output = output.encode()
    response_headers = [("Content-type", "text/html"),
                        ("Content-Length", str(len(output)))]
    start_response(status, response_headers)
    return [output]
