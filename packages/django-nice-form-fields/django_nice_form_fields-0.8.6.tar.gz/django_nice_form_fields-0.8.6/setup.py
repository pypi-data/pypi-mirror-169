from distutils.core import setup

setup(name='django_nice_form_fields',
      version='0.8.6',
      description='Django custom imagefield that dynamically renders the loaded image.',
      author='Artur Karpovich',
      author_email='onelifeitsme@gmail.com',
      url='https://github.com/onelifeitsme/django_nice_form_fields',
      packages=['django_nice_form_fields', 'django_nice_form_fields.templates', 'django_nice_form_fields.templates.django_dynamic_imagefield'],
      package_data={'django_nice_form_fields.templates': ['django_dynamic_imagefield/*.html']},
      install_requires=['django', 'pillow'],
     )
