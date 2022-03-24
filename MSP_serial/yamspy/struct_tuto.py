# Python 언어가 바이트 비트 처리가 상당히 어려운 문제가
# struct 모듈 unpack, calcsize의 기능을 이용 정수, 부동 소수점 숫자, 문자열을 bytes 객체로 변환하거나
# bytes 객체에서 필요한 데이터를 꺼낼수 있다.

from struct import pack, unpack, calcsize

data = pack('b', 100)
print(data)
print(f"100 == '{chr(100)}'")
result = unpack('b', data)
print(result) # 튜플 형태로 변환한다.
