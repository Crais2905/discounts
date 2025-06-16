import json
import logging
from datetime import timedelta
from celery import Celery
from celery.signals import after_setup_logger
from parse_data.atb_parser import ATBParser
import httpx

logger = logging.getLogger(__name__)

celery = Celery(
    'tasks', 
    broker='redis://localhost:6379/0',
)

atb_parser = ATBParser(store_url="https://www.atbmarket.com/catalog/388-aktsiya-7-dniv")


celery.conf.update(
    task_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
    worker_hijack_root_logger=False,
)

celery.autodiscover_tasks()

@celery.task
def parse_atb():
    atb_parser.set_src()
    products_list = atb_parser.get_products()
    headers = {"Content-Type": "application/json"}

    for product in products_list:
        data = atb_parser.get_data(product)
        with httpx.Client() as client:
            response = client.post(f"http://127.0.0.1:8000/products/", json=data, headers=headers)

    data = atb_parser.get_data(products_list[0])
    with httpx.Client() as client:
        response = client.post(f"http://127.0.0.1:8000/products/", json=data, headers=headers)
    return {"status": "completed", "items_sent": len(products_list)}


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('logs.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)



celery.conf.beat_schedule = {
    "test": {
        "task": 'celery_app.parse_atb',
        "schedule": timedelta(seconds=10),
    },
}