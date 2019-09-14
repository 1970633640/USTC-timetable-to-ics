from bs4 import BeautifulSoup

x = str(open("1.html", 'r', encoding='UTF-8').readlines())
s = BeautifulSoup(x, features="html.parser")
for c in s.find_all(class_="cell"):
    # print(c)
    # print(c.find(class_="title").string, c.find(class_="teacher").contents, c.find(class_="classroom").string)
    title = c.find(class_="title").string
    teachers = []
    for temp in c.find(class_="teacher").contents:
        teachers.append(temp.string)
    teacher = "、".join(teachers)
    classroom=c.find(class_="classroom").string
    timespan=c.find(class_="timespan").string
    weekspan=c.find(class_="week").string
    print(title, teacher, classroom,timespan,weekspan)