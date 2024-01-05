import re

def wspex(x):
    return re.sub(u'\u200a', '', ''.join(x.split()))


def wspex_space(x):
    return re.sub(u'\u200a', '', ' '.join(str(x).split()))