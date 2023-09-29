from ..models import Contrato, Servicio, Factura

def get_servicio():
        queryset = Servicio.objects.all().order_by('nombre_servicio')
        return (queryset)

def create_servicio(form):
        servicio = form.save()
        servicio.save()
        return ()