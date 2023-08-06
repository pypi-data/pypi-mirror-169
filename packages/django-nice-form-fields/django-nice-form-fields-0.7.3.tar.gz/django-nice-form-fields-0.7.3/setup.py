from distutils.core import setup

setup(name='django-nice-form-fields',
      version='0.7.3',
      description='Django custom imagefield that dynamically renders the loaded image.',
      author='Artur Karpovich',
      author_email='onelifeitsme@gmail.com',
      url='https://github.com/onelifeitsme/django-nice-form-fields',
      packages=['django-nice-form-fields', 'django-nice-form-fields.templates', 'django-nice-form-fields.templates.django_dynamic_imagefield'],
      install_requires=['django', 'pillow'],
     )
