
from django.views.generic import ListView
from django.views.generic.base import ContextMixin

from .models import HelpContent

class FieldHelpMixin(ContextMixin):
    ''' 
    Extends ContentMixin to add the key, field_help, to the context. The value for field_help
    will by the set up HelpContent objects with field names matching those in the
    attribute field_names. If no field_names are specified, return all of the HelpContent
    objects.
    '''
    
    field_names = [] # List of field_name's to retrieve from HelpContext. If empty return all
    
    def get_context_data(self, **kwargs):
        context = super(FieldHelpMixin, self).get_context_data(**kwargs)
        if self.field_names:
            qs = HelpContent.objects.filter(field_name__in=self.field_names)
            context['field_help'] = HelpContent.objects.filter(field_name__in=self.field_names)
            
        else:
            qs = HelpContent.objects.all()
           
        context['field_help'] = dict([(c.field_name, c) for c in qs])
          
        return context
    
class GlossaryView(ListView):
    
    template_name = 'glossary.html'
    queryset = HelpContent.objects.filter(description__isnull=False).values('label', 'description').distinct().order_by('label')
    context_object_name = 'help_list'
    