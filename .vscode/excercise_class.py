"""
class firstclass:
    class_atribute = value
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

        def method1(self, parameter1):
            return self.attribute1 + parameter1
"""

# 예제가 너무 복잡하고 불편해서 그냥 현실 세계와 유사한 예제를 통해 학습하기로 함.

class Car:
    # 클래스 속성 (모든 개체가 공유함)
    max_speed = 120  # 최고 속도, 단위: km/h

    # 생성자 (객체 생성 시 실행됨)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # 기본 속도 = 0

    # 자동차 가속 메서드
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed  # 오타 수정

    # 현재 속도 반환 메서드
    def get_speed(self):
        return self.speed


# 객체 생성
car1 = Car("Hyundai", "Sonata", "Black")
car2 = Car("Toyota", "Camry", "White")

# 속도 증가
car1.accelerate(30)
car2.accelerate(20)

# 출력
print(f"{car1.make} {car1.model}의 현재 속도 : {car1.get_speed()} km/h")
print(f"{car2.make} {car2.model}의 현재 속도 : {car2.get_speed()} km/h")

import matplotlib.pyplot as plt

# class cirble (object):

class Circle(object):
    # constructor
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    # method
    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)
    
    # method
    def drawCircle(self):
        