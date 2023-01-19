import re
from embed_video.backends import VideoBackend


class CustomBackend(VideoBackend):
    re_detect = re.compile(r'https://aparat\.com/[0-9]+')
    re_code = re.compile(r'https://aparat\.com/(?P<code>[0-9]+)')

    allow_https = True
    pattern_url = 'https://aparat\.com/c/{code}/'
    pattern_thumbnail_url = 'https://aparat\.com/c/{code}/'

    template_name = 'embed_video/custombackend_embed_code.html'  # added in v0.9
