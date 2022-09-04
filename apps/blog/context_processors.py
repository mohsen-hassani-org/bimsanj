from .models import SiteSetting
from .models import ThemeContent

def site_settings(request):
    return {'settings': SiteSetting.load()}

def theme_content(request):
    contents = ThemeContent.objects.theme_contents()

    theme_content = type("ThemeContent", (), {})()
    for content in contents:
        setattr(theme_content, content.key, content.value)

    return {'theme_content': theme_content} 


    
