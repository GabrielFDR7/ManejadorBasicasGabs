from ..models import Measurement

def get_measurements():
    queryset = Measurement.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_measurement(form):
    measurement = form.save()
    measurement.save()
    return ()

def create_measurement_object(id, value, variable):
    measurement = Measurement()
    measurement.id = id
    measurement.value = value
    measurement.variable = variable
    measurement.save()
    return ()