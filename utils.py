ERROR_MSG = {
    'TAKEN_ID': '사용할 수 없는 아이디입니다. 다른 아이디를 사용하세요.',
    'MISSING_INPUT': '모든 항목을 입력해주세요.',
    'INVALID_PW': '비밀번호를 확인하세요.',
    'INVALID_ID': '아이디를 확인하세요.'
}

def build_error_data(error_code):
    return {'error': {'state': True, 'msg': ERROR_MSG[error_code]}}

def build_success_data(object):
    return {'error': {'state': False }, 'data': object}