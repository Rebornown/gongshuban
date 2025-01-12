from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    """
    产品类
    """

    def __init__(self, age=None, gender=None, height=None, weight=None):
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"年龄:{self.age}, 性别:{self.gender}, 身高:{self.height}, 体重:{self.weight}"


class BuilderPerson(metaclass=ABCMeta):
    """
    抽象建造者类
    """

    @abstractmethod
    def build_age(self):
        pass

    @abstractmethod
    def build_gender(self):
        pass

    @abstractmethod
    def build_height(self):
        pass

    @abstractmethod
    def build_weight(self):
        pass


class BuildYoungWomanPerson(BuilderPerson):
    """
    实际的产品类
    """

    def __init__(self):
        self.person = Person()

    def build_age(self):
        self.person.age = "18"

    def build_gender(self):
        self.person.gender = "女"

    def build_height(self):
        self.person.height = "1.7m"

    def build_weight(self):
        self.person.weight = "50kg"


class BuildOldManPerson(BuilderPerson):
    """
    实际的产品类
    """

    def __init__(self):
        self.person = Person()

    def build_age(self):
        self.person.age = "60"

    def build_gender(self):
        self.person.gender = "男"

    def build_height(self):
        self.person.height = "1.8m"

    def build_weight(self):
        self.person.weight = "70g"


class PersonDirector:
    """
    指挥者类，描述产品构建的细节
    """

    def build_person(self, builder: BuilderPerson):
        builder.build_age()
        builder.build_gender()
        builder.build_height()
        builder.build_weight()
        return builder.person


# 高层代码：
# 创建年轻的女人
builder1 = BuildYoungWomanPerson()
hd = PersonDirector()
p = hd.build_person(builder1)
print(p)

# 创建老男人
builder2 = BuildOldManPerson()
hd2 = PersonDirector()
p2 = hd2.build_person(builder2)
print(p2)


# # 输出
# ================================
# 年龄:18, 性别:女, 身高:1.7m, 体重:50kg
# 年龄:60, 性别:男, 身高:1.8m, 体重:70g
