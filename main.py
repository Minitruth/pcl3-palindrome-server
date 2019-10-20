#!/usr/bin/python3

import cgi


def check_palindrome(word):
    reverse = word[::-1]
    if reverse == word:
        return True
    else:
        return False


def application(environ, start_response):
    params = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)

    word = params.getfirst('word', default=None)

    if word is None:
        output = """\
<h1>Palindrome Checker</h1>
<form action="" method="get">
    <label for="word">What word do you want to check?</label>
    <input name="word" id="word">
    <button>Submit</button>
</form>
"""
    else:
        is_palindrome = check_palindrome(word)
        output = """\
        <p><a href="?">&larr; Back</a></p>
        <h1>Result</h1>
        <!-- TODO -->
        """
        if is_palindrome:
            output += '{} is a palindrome!'.format(word)
        else:
            output += '{} is not a palindrome!'.format(word)

    status = "200 OK"
    output = output.encode()
    response_headers = [("Content-type", "text/html; charset=UTF-8"),
                        ("Content-Length", str(len(output)))]
    start_response(status, response_headers)
    return [output]
