
# 数据路径
import json
import os


db_path = 'packages/python-v0.2/stusystem/studata.txt'
# 菜单宽度
menu_width = 100


def main():
    while True:
        menu()

        choice = int(input('请选择：'))
        if choice == 100:
            if exit_confirm('确认退出吗？'):
                break
            else:
                continue
        elif choice == 0:
            break
        elif choice == 1:
            insert()
        elif choice == 2:
            search()
        elif choice == 3:
            delete()
        elif choice == 4:
            modify()
        elif choice == 5:
            sort()
        elif choice == 6:
            total()
        elif choice == 7:
            show()


def menu():
    menu_border('学生信息管理系统', '=')
    menu_border('功能菜单', '-', 2)
    menu_line('1.录入学生信息')
    menu_line('2.查找学生信息')
    menu_line('3.删除学生信息')
    menu_line('4.修改学生信息')
    menu_line('5.对学生成绩排序')
    menu_line('6.统计学生总人数')
    menu_line('7.显示所有学生信息')
    menu_line('100.退出系统')
    menu_line('0.强退系统')
    menu_border('', '-', 4)


def menu_border(txt, fill, offset=0):
    l = len(txt)
    w = int(menu_width - l / 2)
    print(txt.center(w + offset, fill))


def menu_line(txt):
    print('\t\t\t\t\t    {}'.format(txt))


def exit_confirm(msg):
    cf = input(msg + 'y/n：')
    if cf == 'y':
        return True
    else:
        return False


def insert():
    stulist = []
    while 1:
        id = input_verify('请输入学生ID:')
        name = input_verify('请输入学姓名:')
        english = input_verify('请输入英语成绩:', f_int=1)
        math = input_verify('请输入数学成绩:', f_int=1)
        java = input_verify('请输入Java成绩:', f_int=1)
        python = input_verify('请输入Python成绩:', f_int=1)
        stu = {'id': id, 'name': name, 'english': english,
               'math': math, 'java': java, 'python': python}
        stu['total'] = calc_total(stu)
        stulist.append(stu)

        if exit_confirm('是否继续添加？'):
            continue
        else:
            break

    print('学生信息录入完毕！')
    print('录入的学生信息：\n')
    show_stulist(stulist)
    save_stulist(stulist)
    print('\n')


def show_stulist(lst):
    f_title = '{:<6}\t{:<12}\t{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}'
    print(f_title.format('ID', '姓名', '英语成绩', '数学成绩', 'Java成绩', 'Python成绩', '总成绩'))
    menu_border('', '-', 4)
    for item in lst:
        print(f_title.format(
            item['id'], item['name'], item['english'], item['math'], item['java'], item['python'], item['total']))


def calc_total(item):
    return item['english'] + item['math'] + item['java'] + item['python']


def save_stulist(lst):
    f = get_wdb()
    for item in lst:
        f.write(json.dumps(item) + '\n')
    f.close()


def get_wdb():
    f = open(db_path, 'a+')
    return f


def get_rdb(msg_not_exist='数据为空'):
    if check_fexist(msg_not_exist):
        return open(db_path, 'r')


def check_fexist(msg_not_exist='数据为空'):
    if not os.path.exists(db_path):
        print(msg_not_exist)
        return False
    return True


def search():
    lst = get_stu_list_db()
    if not len(lst):
        print('数据为空')
        return

    while True:
        search_lst = search_to(lst)
        if not search_lst:
            break

        if len(search_lst):
            show_stulist(search_lst)
        else:
            print('没有找到对应的学生。')

        if not exit_confirm('\n还继续查找吗？'):
            break


def search_to(lst):
    search_lst = []
    while True:
        i = input_verify('请选择查询方式(1.按ID查询; 2.按姓名查询；0.返回目录):', f_int=1)
        if i == 1:
            search_lst = search_by(lst, 'id')
            break
        elif i == 2:
            search_lst = search_by(lst, 'name')
            break
        elif i == 0:
            # 返回
            return 0
        else:
            print('请输入正确的选项！')
            continue
    return search_lst


def search_by(lst, key):
    val = input_verify('请输入关键字：')

    rst = []
    for item in lst:
        if item[key] == val:
            rst.append(item)
    return rst


def delete():
    pass


def modify():
    lst = get_stu_list_db()
    if not len(lst):
        print('数据为空')
        return

    while True:
        search_lst = search_to(lst)
        if not search_lst:
            break

        if not len(search_lst):
            if not exit_confirm('没找到对应的同学，还继续修改吗？'):
                break
            else:
                continue

        i = input_verify(
            '请选择查询方式(1.修改姓名;2.修改英语成绩;3.修改数学成绩;4.修改Java成绩;5.修改Python成绩;0.返回主菜单):', f_int=1)
        if i == 0:
            break
        if i in [1, 2, 3, 4, 5]:
            pass
        else:
            print('请输入正确的选项！')


def sort():
    pass


def total():
    pass


def show():
    lst = get_stu_list_db()
    if len(lst) == 0:
        print('数据为空')
        return
    show_stulist(lst)
    print('\n')


def get_stu_list_db(msg_not_exist=''):
    stu_list = []
    f = get_rdb(msg_not_exist)
    if f:
        lines = f.readlines()
        stu_list = []
        for item in lines:
            stu_list.append(json.loads(item))
        f.close()
    return stu_list


def input_verify(msg, **options):
    while True:
        rst = input(msg)
        if not rst:
            continue
        if options:
            if options['f_int']:
                try:
                    rst = int(rst)
                except:
                    continue
        return rst


if __name__ == '__main__':
    main()
