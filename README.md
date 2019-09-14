# USTC-timetable-to-ics
USTC timetable to calendar ics file 中国科学技术大学教务课程表转换日历ics文件
有了ics文件，可以导入到win10日历、Google日历、outlook日历等等……

# 使用方法
登录教务系统后（研究生、本科生），在浏览器开启F12调试窗口后打开```https://jw.ustc.edu.cn/for-std/course-table```，在调试窗口找到一个含有选课信息、个人信息、上课时间的返回结果（返回的是json），将返回内容文本复制到```json_version.py```文件目录下的```1.json```中，
然后**修改py文件**中学期第一周星期一前面一天（星期日）的日期，最后运行```json_version.py```，输出的ics就是日历文件。

# 怎么导出到……
win10日历、outlook可以直接导入
**Google日历网页版**直接上传ics导入**不行**，**要通过网址**添加，例如可以把ics文件托管在github pages上然后在Google日历中添加
