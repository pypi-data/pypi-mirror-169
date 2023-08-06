from distutils.core import setup

setup(name='django-nice-form-fields',
      version='0.7.1',
      description='Django custom imagefield that dynamically renders the loaded image.',
      author='Artur Karpovich',
      author_email='onelifeitsme@gmail.com',
      url='https://github.com/onelifeitsme/django-nice-form-fields',
      packages=['django_dynamic_fields', 'django_dynamic_fields.templates'],
      install_requires=['django', 'pillow'],
     )
