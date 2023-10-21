from ..models import Measurement

def create_measurement(value, variable):
    # Crea una nueva instancia de Measurement y la guarda en la base de datos
    measurement = Measurement(value=value, variable=variable)
    measurement.save()
    return measurement

def get_latest_measurements(limit=10):
    # Obtiene las últimas mediciones
    measurements = Measurement.objects.order_by('-timestamp')[:limit]
    return measurements