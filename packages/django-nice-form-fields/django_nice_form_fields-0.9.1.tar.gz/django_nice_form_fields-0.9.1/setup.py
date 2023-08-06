from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='django_nice_form_fields',
      long_description=long_description,
      long_description_content_type='text/markdown',
      version='0.9.1',
      description='Django custom imagefield that dynamically renders the loaded image.',
      author='Artur Karpovich',
      author_email='onelifeitsme@gmail.com',
      url='https://github.com/onelifeitsme/django_nice_form_fields',
      packages=['django_nice_form_fields', 'django_nice_form_fields.templates', 'django_nice_form_fields.templates.django_nice_form_fields'],
      package_data={'django_nice_form_fields.templates': ['django_nice_form_fields/*.html']},
      install_requires=['django', 'pillow'],
     )
