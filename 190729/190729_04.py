# module
# 모듈 추가시 파일명은 영문
# '__main__' is not a package 에러.. 해결 shorturl.at/suIJW
# 현재 디렉터리 (190729)를 소스로 설정으로 해결 (폴더 우클 Mark Diretory as -> Source )

from module1 import *

import sys

print(sys.path)

print("module")
print()

print(add_serial(1, 2, 3, 4, 5))

print(__name__)


#exceoption
print("exception")
print()

try:
    3/0
except ZeroDivisionError as e:
    print(e)
