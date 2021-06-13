import time
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

def get_time_passed(object):
    time_passed = int(float(time.time()) - float(object.created_at))
    if time_passed < 60:
        return str(time_passed) + '초 전'
    if time_passed//60 < 60:
        return str(time_passed//60) + '분 전'
    if time_passed//(60*60) < 24:
        return str(time_passed//(60*60)) + '시간 전'
    if time_passed//(60*60*24) < 30:
        return str(time_passed//(60*60*24)) + '일 전'
    