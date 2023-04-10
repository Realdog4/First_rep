from http.cookies import SimpleCookie


def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


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