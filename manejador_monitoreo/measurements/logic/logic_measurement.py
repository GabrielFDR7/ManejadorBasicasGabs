from ..models import Measurement

def get_measurements():
    queryset = Measurement.objects.all().order_by('-timestamp')[:10]
    return queryset

def create_measurement(form):
    measurement = form.save()
    return measurement

def create_measurement_object(id, value, variable):
    measurement = Measurement(id=id, value=value, variable=variable)
    measurement.save()
    return measurement