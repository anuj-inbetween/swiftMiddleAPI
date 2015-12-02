from rest_framework import renderers


class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/*'
    format = '*'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data
