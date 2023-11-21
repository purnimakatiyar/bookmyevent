import string
import shortuuid


def generate_uuid():
    text = string.ascii_lowercase + string.digits
    su = shortuuid.ShortUUID(alphabet=text)
    return su.random(length=8)