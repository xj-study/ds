drop database if exists stu_sys;

create database stu_sys;

use stu_sys;

-- 用户登录
create table user_login (
    id int(20) PRIMARY KEY AUTO_INCREMENT,
    user_name varchar(20) NOT NULL,
    password varchar(20) NOT NULL,
    UNIQUE (user_name)
);

-- 学生成绩表
create table stu_score (
    id int(20) PRIMARY KEY,
    name varchar(100) NOT NULL,
    english int(4) default 0 NOT NULL,
    math int(4) default 0 NOT NULL,
    java int(4) default 0 NOT NULL,
    python int(4) default 0 NOT NULL,
    status int default 1
);

insert into
    stu_score
values
    ('1001', '张三', '110', '120', '90', '89', 1);

insert into
    stu_score
values
    ('1002', '李四', '120', '110', '92', '90', 1);

insert into
    stu_score
values
    ('1003', '王五', '90', '90', '89', '89', 1);

insert into
    stu_score
values
    ('1004', '赵六', '80', '80', '70', '79', 1);