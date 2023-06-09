from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs


def parse (query: str) -> dict:
    parsed_url = urlparse(query)
    params = parse_qs(parsed_url.query)
    result = {k: v[0] for k, v in params.items()}

    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://www.google.com/search?q=python+documentation&oq=python+documentation') == {'q': 'python documentation', 'oq': 'python documentation'}
    assert parse('https://www.youtube.com/watch?v=dQw4w9WgXcQ') == {'v': 'dQw4w9WgXcQ'}
    assert parse('https://en.wikipedia.org/wiki/Main_Page') == {}
    assert parse('https://example.com/?name=John&age=30&gender=male') == {'name': 'John', 'age': '30', 'gender': 'male'}
    assert parse('http://localhost:8080/?id=123&name=Bob') == {'id': '123', 'name': 'Bob'}
    assert parse('https://www.facebook.com/profile.php?id=1234567890&ref=bookmarks') == {'id': '1234567890', 'ref': 'bookmarks'}
    assert parse('https://www.example.com/?param1=value1&param2=value2') == {'param1': 'value1', 'param2': 'value2'}
    assert parse('http://localhost:5000/search?q=python+development') == {'q': 'python development'}
    assert parse('https://www.linkedin.com/in/johndoe/') == {}
    assert parse('https://twitter.com/search?q=%23python') == {'q': '#python'}
    assert parse('https://www.amazon.com/s?k=laptop&ref=nb_sb_noss') == {'k': 'laptop', 'ref': 'nb_sb_noss'}
    assert parse('http://www.example.com/page.php?id=23&name=John&city=New+York') == {'id': '23', 'name': 'John', 'city': 'New York'}



def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    result = {k: v.value for k, v in cookie.items()}
    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('key=value;name=Dima;') == {'key': 'value', 'name': 'Dima'}
    assert parse_cookie('name=Dima;age=28;city=New+York;') == {'name': 'Dima', 'age': '28', 'city': 'New+York'}
    assert parse_cookie('username=johndoe;sessionid=1234567890;') == {'username': 'johndoe', 'sessionid': '1234567890'}
    assert parse_cookie('name=Dima;age=28;email=dima@example.com;') == {'name': 'Dima', 'age': '28', 'email': 'dima@example.com'}
    assert parse_cookie('user_id=1234;first_name=John;last_name=Doe;') == {'user_id': '1234', 'first_name': 'John', 'last_name': 'Doe'}
    assert parse_cookie('username=admin;password=12345;is_admin=true;') == {'username': 'admin', 'password': '12345','is_admin': 'true'}
    assert parse_cookie('username=johndoe;sessionid=1234567890;lang=en-US;') == {'username': 'johndoe','sessionid': '1234567890','lang': 'en-US'}
    assert parse_cookie('foo=bar;baz=qux;') == {'foo': 'bar', 'baz': 'qux'}
    assert parse_cookie('name=Dima=Smith;') == {'name': 'Dima=Smith'}