from distutils.core import setup


setup(name='django_nice_form_fields',
      long_description='Django forms custom imagefield that dynamically renders the loaded image.',
      version='0.9.2',
      description='Django custom imagefield that dynamically renders the loaded image.',
      author='Artur Karpovich',
      author_email='onelifeitsme@gmail.com',
      url='https://github.com/onelifeitsme/django_nice_form_fields',
      packages=['django_nice_form_fields', 'django_nice_form_fields.templates', 'django_nice_form_fields.templates.django_nice_form_fields'],
      package_data={'django_nice_form_fields.templates': ['django_nice_form_fields/*.html']},
      install_requires=['django', 'pillow'],
     )
