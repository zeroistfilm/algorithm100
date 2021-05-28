class Rectangle:
    count = 0  # 클래스변수// 모든 클래스가 공유하는 변수이다.

    def __init__(self, width, height):
        # 이니셜라이저는 클래스로부터 객체를 만들떄, 인스턴스 변수를 초기화 하거나, 객체의 상태를 초기상태로 만들기 위해 사용한다.

        # self. 인스턴스변수
        # 생성된 인스턴스마다 각각 가지는 변수들이다.
        self.width = width
        self.height = height
        Rectangle.count += 1

    def calcArea(self):
        area = self.height * self.width
        return area

    # Private 메소드드
    def __internalRun(self):
        pass

    # 정적메서드, 인스턴스 변수에 접근할 수 없다,
    @staticmethod
    def staticMethod():
        pass

    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight

    # 클래스메서드, 정적메서드와 비슷한데 클래스를 의미하는 파라미터를 전달 받는다.클래스 변수에 접근할 수 있다.
    @classmethod
    def classMethod(cls):
        pass

    @classmethod
    def printCount(cls):
        print(cls.count)

    def __add__(self, other):
        obj = Rectangle(self.width+other.width, self.height+other.height)
        return obj

if __name__ == '__main__':
    # squre = Rectangle.isSquare(10, 10)
    # print(squre)
    #
    # rect1 = Rectangle(3, 5)
    # rect2 = Rectangle(5, 5)
    #
    # rect1.printCount()
    #
    # rect3 = rect1+rect2
    # print(rect3.height, rect3.width, rect3.calcArea(), rect3.calcArea())

    # 인스턴스 생성
    r = Rectangle(2, 3)

    # 메서드 호출
    area = r.calcArea()
    print("area = ", area)

    # 인스턴스 변수 엑세스 후 변경
    r.width = 10
    print("width = ", r.width)

    area = r.calcArea()
    print("area = ", area)


    # 클래스 변수 엑세스
    # 클래스 변수에 접근할 때는
    # 객체의 클래스에서 찾아보고, 없으면 상위 클래스에서 찾고 없으면 에러를 뱉는다.
    print(Rectangle.count)
    print(r.count) #삐, 사용하지 말것
    r.count =10

    print(Rectangle.count)
    print(r.count)  # 삐, 사용하지 말것
