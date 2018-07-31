import six


def base64encode(s):
    if six.PY3 and isinstance(s, six.string_types):
        s = s.encode('utf-8')
    else:
        # Python 2 support because the base64 module doesnt like unicode
        s = str(s)

    encoded = base64.urlsafe_b64encode(s).rstrip(b'\n=')
    if six.PY3:
        try:
            encoded = encoded.decode('utf-8')
        except UnicodeDecodeError:
            pass
    return encoded


def base64decode(s):
    if six.PY3 and isinstance(s, six.string_types):
        s = s.encode('utf-8')
    else:
        # Python 2 support because the base64 module doesnt like unicode
        s = str(s)

    decoded = base64.urlsafe_b64decode(s.ljust(len(s) + len(s) % 4, b'='))
    if six.PY3:
        try:
            decoded = decoded.decode('utf-8')
        except UnicodeDecodeError:
            pass
    return decoded