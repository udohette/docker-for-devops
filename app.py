# app.py
import os

app_version = os.environ.get('APP_VERSION', 'UNKWOWN')
environment = os.environ.get('ENVIRONMENT', 'UNKWOWN')

print(f"Running App Version {app_version} in {environment} environment")