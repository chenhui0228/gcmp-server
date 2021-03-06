from db.sqlalchemy import models
from db.sqlalchemy import api as db_api

def t1(db):
    db.create(False)
    for i in range(1, 30):
        policy = {
            'start_time': i,
            'name': 'lucy%d' % i,
            'description': 'this is test %d' % i
        }
        p = db.create_policy(policy)
    u = models.User(name='jack')
    db.add(u)
    for i in range(1, 4):
        worker = {
            'name' : 'worker%d' % i,
            'ip' : 'xxx',
            'port' : 80
        }
        db.create_worker(worker)

    for i in range(1, 30):
        task = {
            'name' : 'a%d' % i,
            'user_id' : 1,
            'policy_id' : i,
            'worker_id' : i % 4,
            'source' : 'a:b',
            'destination': 'a:b'
        }
        db.create_task(task)

    db.flush()


def t2(db):
    worker=db.get_worker(2)
    print worker.to_dict()
    worker.name='Jack'
    w = models.Worker(name='Lala' , ip='xxx', port=80)
    db.add(w)
    db.flush()
    db.delete(worker)

def t3(db):
    w = db.get_worker(1, deleted=True)
    db.soft_delete(w)
    db.flush()

from db.sqlalchemy import copy
def update_policy(db, policy_values):
    values = copy.deepcopy(policy_values)
    id = values['id']
    policy = db.get_policy(id)
    params = policy.generate_param()
    print params
    for k, v in params.items():
        params[k] = values.get(k)
    policy.update(params)
    db.flush()
    return db.get_policy(id)

def t5(db):
    pd = {
        'id': 38,
        'name': 'abc8',
        'start_time': 123,
        'interval': 6,
    }

    update_policy(db, pd)



if __name__ == '__main__':

    db = db_api.get_db(type='sqlite', path='sqlite:///test.db')
    #t2(db)
    #t3(db)
    #t1(db)
    #t5(db)


