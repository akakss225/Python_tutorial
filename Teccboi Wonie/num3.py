# 패키지와 모듈
# 패키지 : 어떤 기능들을 구현하는 패키지의 합
# 모듈 : 코드를 잘 모아서 기능 하나를 구현해놓은 파일

# 결국 폴더가 패키지, 파일이 모듈이 된다.

from animal import dog # animal 패키지에서 dog이란 모듈을 가져와줘.
from animal import cat
from animal import * # animal 패키지가 가지고있는 모든 모듈을 다 불러와

d = Dog()
c = Cat()

d.hi()
c.hi()

