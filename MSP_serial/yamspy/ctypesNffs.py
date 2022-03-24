# what is ffs
# 주어진 2진 정수에 설정된 least bit set 리턴하는 함수 ffs()

# 우분투에서는 ..
# import ctypes
# libc = ctypes.cdll.LoadLibrary('libc.so.6')
# print(libc.ffs(135))

# 그외에서는 
def ffs(x): # modified from https://stackoverflow.com/a/36059264
    return (x&-x).bit_length() -1
print(ffs(2))

# bitwise 연산
bin(0b1101 & 0b1001)    # 비트 AND
# result :'0b1001'
# 13 & 9 --> 9                 # 비트 AND
# 우리 코드에서 (x&-x)를 한건 양수와 정수 사이의 비트 연산을 해서 
# .bit_length 는 정수를 이진수로 표현해주기 위해 필요한 연산