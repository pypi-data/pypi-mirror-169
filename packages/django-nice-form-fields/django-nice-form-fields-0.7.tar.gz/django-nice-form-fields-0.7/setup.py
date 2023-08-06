from distutils.core import setup

setup(name='django-nice-form-fields',
      version='0.7',
      description='Django forms custom imagefield that dynamically renders the loaded image.',
      author='Artur Karpovich',
      author_email='onelifeitsme@gmail.com',
      url='https://github.com/onelifeitsme/django_dynamic_fields',
      packages=['django_dynamic_fields'],
      install_requires=['django', 'pillow'],
     )
