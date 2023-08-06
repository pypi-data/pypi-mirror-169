from distutils.core import setup

setup(name='django-nice-form-fields',
      version='0.8.01',
      description='Django custom imagefield that dynamically renders the loaded image.',
      author='Artur Karpovich',
      author_email='onelifeitsme@gmail.com',
      url='https://github.com/onelifeitsme/django-nice-form-fields',
      packages=['django-nice-form-fields', 'django-nice-form-fields.templates', 'django-nice-form-fields.templates.django_dynamic_imagefield'],
      include_package_data=True,
      package_data={
        'django-nice-form-fields.templates.django_dynamic_imagefield' : ['django-nice-form-fields.templates.django_dynamic_imagefield/*.html']
    },
      install_requires=['django', 'pillow'],
     )
