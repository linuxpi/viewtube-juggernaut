import magic

from drf_extra_fields.fields import Base64FileField

class CustomBase64FileField(Base64FileField):

    ALLOWED_TYPES = [
        'video/mp4',
        'video/quicktime',
    ]

    def get_file_extension(self, filename, decoded_file):
        return magic.from_buffer(decoded_file[:1024], mime=True)
