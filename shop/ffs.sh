#!/bin/bash
cd /home/ckl/shop && /home/ckl/Envs/shop/bin/python3 manage.py static
touch /home/ckl/shop/uwsgi.ini
