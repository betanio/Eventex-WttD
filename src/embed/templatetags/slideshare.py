
# -*- coding: utf-8 -*-

from django import template
from django.template import Context, loader, Node

# instancia um Singleton - do motor de templates do Django
# biblioteca que registra todas as custom tags e custom filters
register = template.Library()

# parsing do texto do template ; construindo uma árvore em memória 
def do_slideshare(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, id_, doc = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 2 arguments" % token.contents.split()[0]
    return SlideShareNode(id_, doc)

# já obteve uma árvore em memória ; agora renderiza todos os nodes
class SlideShareNode(Node):
    def __init__(self, id_, doc):
        self.id = template.Variable(id_)
        self.doc = template.Variable(doc)

    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except template.VariableDoesNotExist:
            actual_id = self.id

        try:
            actual_doc = self.doc.resolve(context)
        except template.VariableDoesNotExist:
            actual_doc = self.doc
            
        t = loader.get_template('embed/slideshare.html')
        c = Context({'id': actual_id, 'doc': actual_doc}, autoescape=context.autoescape)
        return t.render(c)


# nome da template tag , nome do callable
register.tag('slideshare', do_slideshare)

