from datetime import datetime
# from alerts.models import Alert
from django.core.mail import send_mail
import django
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btctracker.settings')
django.setup()


# sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)


def bitcoin_price_alert():
    get_bitcoin_price = requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice.json')
    results = json.loads(get_bitcoin_price.text)
    current_price = results['bpi']['USD']['rate_float']

    if current_price < 40000:
        send_mail(
            "BTC PRICE LOWER THAN 40k !!",  # subject message
            'Price Alert - Current BTC price is {}'.format(current_price),
            "adityagautam1911@gmail.com",  # from
            ["aditya.gautam2021@vitstudent.ac.in"],  # to
            fail_silently=False,
        )

    if current_price >= 40000:
        send_mail(
            "BTC PRICE MORE THAN 40k !!",
            'Price Alert - Current BTC price is {}'.format(current_price),
            "adityagautam1911@gmail.com",  # from
            ["aditya.gautam2021@vitstudent.ac.in"],  # to
            fail_silently=False,
        )


# sched.start()
bitcoin_price_alert()
