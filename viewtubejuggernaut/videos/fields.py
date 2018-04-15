import magic

from drf_extra_fields.fields import Base64FileField

class CustomBase64FileField(Base64FileField):

    ALLOWED_TYPES = [
        'mp4',
        'mov',
    ]

    TYPE_MAP = {
        'video/mp4': 'mp4',
        'video/quicktime': 'mov',
    }

    def get_file_extension(self, filename, decoded_file):
        mime = magic.from_buffer(decoded_file[:1024], mime=True)
        return self.TYPE_MAP.get(mime)
