import pathlib
from django.forms import ImageField, ClearableFileInput
from django.forms.fields import FileInput


class CustomClearableFileInput(ClearableFileInput):
    fp = pathlib.Path('django_nice_form_fields/dynamic_imagefield.html')
    fn = str(fp)
    template_name = fn


class DynamicImageField(ImageField):
    widget = CustomClearableFileInput
    
    def __init__(self, *args, **kwargs):
        self.choose_image_text = kwargs.get('choose_image_text')
        self.change_image_text = kwargs.get('change_image_text')
        kwargs.pop('choose_image_text', None)
        kwargs.pop('change_image_text', None)
        super().__init__(*args, **kwargs)
    
    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        if isinstance(widget, FileInput) and "accept" not in widget.attrs:
            attrs.setdefault("accept", "image/*")
        if self.choose_image_text:
            attrs.setdefault('choose_image_text', self.choose_image_text)
        if self.change_image_text:
            attrs.setdefault('change_image_text', self.change_image_text)
        return attrs
