import os

# Configurações gerais
SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')

# Configurações da AWS S3
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_REGION = os.getenv('AWS_REGION')
AWS_S3_BUCKET = os.getenv('AWS_S3_BUCKET')

# Configurações MQTT
MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
