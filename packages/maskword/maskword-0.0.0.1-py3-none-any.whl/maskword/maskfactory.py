import re


def _remove_space(input):
    return input.replace(" ", "")


def _mask_str(len):
    result = ''
    for i in range(len):
        result += '*'
    return result


def mask_name(name, level):
    result = ''
    regex = '^([가-힣0-9A-Za-z()]{1})([\\S]*)([가-힣0-9A-Za-z()]{1})$'
    target_name = _remove_space(name)
    p = re.compile(regex)
    m = p.match(target_name)

    if level == 'a':
        result = name[0:1] + _mask_str(len(name) - 1)
    elif level == 'b':
        if len(name) > 2:
            result = name[0:2] + _mask_str(len(name) - 2)
        else:
            result = name[0:1] + _mask_str(len(name) - 1)
    elif level == 'c':
        if len(name) > 2:
            if m:
                result = m.group(1) + _mask_str(len(target_name) - 2) + m.group(3)
            else:
                result = name[0:1] + _mask_str(len(name) - 1)
    return result


def mask_ctznum(name, level):
    result = ''
    if name.find('-') > -1:
        name = name.replace('-', '')

    pattern = '.'
    pattern_mdd = '(.{2})(.{4})(.+)'
    p = re.compile(pattern_mdd)

    if level == 'b':
        m = p.match(name)
        result = _ctzdash('**' + m.group(2) + _mask_str(len(name) -6))
    elif level =='c':
        m = p.match(name)
        result =  _ctzdash(m.group(1) +  m.group(2) +  _mask_str(len(name) -6))
    else:  # level is a
        result = _ctzdash(re.sub(pattern, '*', name))

    return result


def _ctzdash(num):
    result = ''
    if num == None or num == '':
        return result
    else:
        result = num[0:6] + '-' + num[6:]
        return result


if __name__ == '__main__':
    tst = "안녕 하 세 요  "
    # print('_remove_space : [', _remove_space(tst),']')
    # print('mask_str : [', _mask_str(3), ']')

    print('mask_name : [', mask_name('전현상', 'a'), ']')
