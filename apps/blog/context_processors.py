from .models import SiteSetting

def settings(request):
    return {'site_settings': SiteSetting.load()}
