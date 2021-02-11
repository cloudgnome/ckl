import imp,sys,os
from celery import Celery
import shutil

sys.path.append('/home/ckl/manager/core')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')


app = Celery('ckl',backend='redis://127.0.0.1',broker='redis://127.0.0.1:6379/4')

@app.task(bind=True)
def merchant_task(self,min_price,facebook=False):
    from main.tasks import merchant_task

    merchant_task(min_price)

@app.task(bind=True)
def currency_prices(self):
    from main.tasks import currency_prices

    currency_prices()

@app.task(bind=True)
def sync(self,brands=[]):
    from main.tasks import stock

    stock(brands=brands)

@app.task(bind=True)
def prices(self,brands=[]):
    from main.tasks import prices

    prices(brands=brands)

@app.task(bind=True)
def stock(self):
    from main.tasks import stock

    stock(verbose=True)

@app.task(bind=True)
def rozetka(self):
    from main.tasks import rozetka

    rozetka()