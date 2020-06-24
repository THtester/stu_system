import os


# 定义一个读文件的函数
def read_stus():
    if os.path.exists(file_name):  # 判断文件是否存在，如果存在就开始读取，如果不存在，则不做任何操作
        f = open(file_name, "r")
        while True:
            student_str = f.readline()  # 一行行读取内容
            if student_str == "":  # 判断文件是否为空，为空则结束循环
                break
            elif student_str.strip() != "" and student_str.strip() != "\n":  # 判断内容是否为空或者换行符，不等于则开始读取
                student_info_list = student_str.split()
                student = {"name": student_info_list[0], "age": student_info_list[1],
                           "qq": student_info_list[2]}  # 按格式赋值
                stus.append(student)  # 将读取到的内容存到stus中


# 定义一个写文件的函数
def write_stus_to_file():
    if os.path.exists(file_name):  # 判断文件是否存在
        if os.path.exists(backup_file):  # 判断备份文件是否存在，如果存在则删除
            os.remove(backup_file)
        os.rename(file_name, "backup_" + file_name)  # 如果不存在，则改名为备份文件
    f = open(file_name, "w")  # 打开文件，开始写操作
    for student in stus:
        student_str = "%s\t%s\t%s" % (student["name"], student["age"], student["qq"])
        f.write(student_str)
        f.write("\n")  # 写完一行内容后加一个换行符，换行
    f.close()  # 写完后，关闭文件


# 定义一个打印主菜单的函数
def print_menu():
    print("=" * 30)
    print("学生管理系统".center(25))
    print("输入1：添加学生")
    print("输入2：查找学生")
    print("输入3：修改学生")
    print("输入4：删除学生")
    print("输入5：查看所有学生")
    print("输入6：退出")


# 定义一个添加学生的函数
def add_student():
    name = input("请输入学生的名字：")
    age = int(input("请输入学生的年龄："))
    qq = input("请输入学生的qq号：")

    stu = {}  # 声明一个字典变量，一个学生包含3个信息，将这三个信息存到一个字典中
    stu["name"] = name  # 往字典中添加一个原始key：name
    stu["age"] = age  # 往字典中添加一个原始key：age
    stu["qq"] = qq  # 往字典中添加一个原始key：qq
    stus.append(stu)
    print("添加成功")


# 定义一个查找学生的函数
def search_student(name):
    for item in stus:
        if item["name"] == name.strip():  # 判断字典中是否包含该学生的名字
            print("%s 学生存在" % name)
            print_student(item)  # 调用print_student()函数，打印学生的信息
            return item
        else:
            print("学生：%s 没有找到" % name)


# 定义一个打印学生信息的函数
def print_student(item):
    print("%s\t%s\t%s"%(item["name"], item["age"], item["qq"]))


# 定义一个打印所有学生的函数
def print_all_students():
    print("序号\t姓名\t年龄\tQQ号")
    for i, item in enumerate(stus, 1):
        print("%s\t" % i, end="")  # 打印序号
        print_student(item)  # 打印学生信息


# 定义一个删除学生的函数
def del_student(name):
    student = search_student(name)
    stus.remove(student)
    print("%s 学生已被删除"%name)


# 定义一个修改学生的函数
def change_student(name):
    pass


# 主函数
def main():
    print_menu()
    read_stus()
    while True:
        operate = input("请输入你想要的操作：")
        if operate == "1":
            add_student()
            write_stus_to_file()
        if operate == "2":
            name = input("请输入需要查找的学生名字：")
            search_student(name)
        if operate == "3":
            name = input("请输入需要修改的学生名字：")
            change_student(name)
        if operate == "4":
            name = input("请输入需要删除的学生名字：")
            del_student(name)
        if operate == "5":
            print_all_students()
        if operate == "6":
            break


file_name = "stus.txt"
backup_file = "backup_stus.txt"
stus = []   # 一个学生包含很多信息，一个学生一个字典，学生列表用列表来存储
main()
