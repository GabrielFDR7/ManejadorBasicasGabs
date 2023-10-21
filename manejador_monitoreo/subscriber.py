import json
import pika
from sys import path
from os import environ
import django
from ManejadorBasicas.manejador_monitoreo.variables.forms import VariableForm
from ManejadorBasicas.manejador_monitoreo.variables.logic.variable_logic import create_variable

rabbit_host = '10.128.0.15'
rabbit_user = 'rasi-db'
rabbit_password = 'rasi2023'
exchange = 'monitoring_measurements'
topics = ['Patient.#']


path.append('monitoring/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')
django.setup()

from measurements.logic.logic_measurement import create_measurement_object
from measurements.services.services_measurements import check_alarm
from variables.services.services_variables import get_variable

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

for topic in topics:
    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=topic)

print('> Waiting measurements. To exit press CTRL+C')


def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    topic = method.routing_key  # No se requiere split en este caso
    variable = get_variable(topic)  # Accede directamente a la variable

    # Verifica si la variable es None (no se encontró por nombre), en cuyo caso deberías crearla
    if variable is None:
        variable = create_variable(name=topic)  # Puedes ajustar esto según tus campos de Variable
        # También puedes pasar otros campos necesarios al crear la variable

    # Asegúrate de que VariableForm tenga los campos y valores adecuados
    variable_form = VariableForm({'name': variable.name, 'description': variable.description, 'unit': variable.unit})
    create_variable(variable_form)

    create_measurement_object(
        variable, payload['value'], payload['unit'], topic)
    if variable.name == 'Heart-rate':
        check_alarm(payload['value'])
    print("Measurement :%r" % (str(payload)))



channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()