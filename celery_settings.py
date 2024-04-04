from celery import Celery


app = Celery(
    'tenderplan',
    broker='redis://localhost',
    backend='redis://localhost:6379/0',
    include=['tasks'])

if __name__ == '__main__':
    app.start()
