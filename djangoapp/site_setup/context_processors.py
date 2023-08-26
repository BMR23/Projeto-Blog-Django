# Sempre que precisamos acessar variáveis nos templates, mandamos
# um context pela view.
# Mas se queremos que todos os templates tenham acesso a um certo context,
# podemos configura-la junto com o templates { context_processo},
# no settings.py
from site_setup.models import SiteSetup


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()
    return {
        'site_setup': setup
    }
