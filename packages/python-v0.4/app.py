from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    form = request.form
    id = form.get('id') or ''
    name = form.get('name') or ''
    status = form.get('status') or ''
    sort = request.args.get('s') or ''
    list = query_list(id=id, name=name, status=status, sort=sort)
    print('list', list)
    return render_template('index.html', **locals())


@app.route('/add', methods=['get', 'post'])
def add():
    if request.method == 'GET':
        return render_template('add.html', data={}, action="/add")
    else:
        form = request.form
        add_user(form)
        return redirect(url_for('index'))


@app.route('/status/<id>/<status>')
def status_update(id, status):
    update_status(id, status)
    return redirect(url_for('index'))


@app.route('/modify/<id>', methods=['get', 'post'])
def modify(id):
    if request.method == 'GET':
        data = get_user(id)
        return render_template('add.html', data=data, action="/modify/"+id)
    else:
        update_stu_data(id, request.form)
        return redirect(url_for('index'))


def update_status(id, status):
    cursor, db = get_db()
    cursor.execute('update stu_score set status = ' +
                   status + ' where id = ' + id)
    db.commit()
    db.close()


def update_stu_data(id, data):
    cursor, db = get_db()
    query = 'update stu_score set'
    query += ' name="%s"' % data.get('name')
    query += ' ,english="%s"' % data.get('english')
    query += ' ,math="%s"' % data.get('math')
    query += ' ,java="%s"' % data.get('java')
    query += ' ,python="%s"' % data.get('python')
    query += ' where id = ' + id
    print('sql', query)
    cursor.execute(query)
    db.commit()
    db.close()


def add_user(data):
    cursor, db = get_db()
    query = 'insert into stu_score (%s, %s, %s, %s, %s, %s) ' % tuple(data.keys()) + \
        ' values ' + str(tuple(data.values()))

    cursor.execute(query)
    db.commit()

    db.close()


def parse2dict(data):
    id, name, english, math, java, python = data
    data = {'id': id, 'name': name, 'english': english, 'math': math,
            'java': java, 'python': python}
    return data


def get_user(id):
    cursor, db = get_db()
    cursor.execute(
        'select id, name, english, math, java, python from stu_score where id =' + id)
    rst = cursor.fetchone()
    rst = parse2dict(rst)
    db.close()
    return rst


def query_list(**args):
    cursor, db = get_db()

    id = args.get('id')
    name = args.get('name')
    status = args.get('status')
    sort = args.get('sort')

    query = 'select id, name, english, math, java, python, status from stu_score'
    list = []
    if id:
        list.append('id = "%s"' % id)
    if name:
        list.append('name = "%s"' % name)
    if status:
        list.append('status = %d' % int(status))

    if len(list):
        query += ' where ' + ' and '.join(list)

    # 有排序
    if sort:
        query += ' order by %s desc' % sort

    print('list query', query)
    cursor.execute(query)
    list = cursor.fetchall()

    db.close()
    return list


def get_db():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='admin123',
        database='stu_sys'
    )
    cursor = db.cursor()
    return cursor, db


if __name__ == '__main__':
    app.run(debug=True, port=9000)
