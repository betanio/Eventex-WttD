
# -*- coding: utf-8 -*-

from django import template
from django.template import Context, loader, Node

# instancia um Singleton - do motor de templates do Django
# biblioteca que registra todas as custom tags e custom filters
register = template.Library()

# parsing do texto do template ; construindo uma árvore em memória 
def do_youtube(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, id_ = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 1 argument" % token.contents.split()[0]
    return YoutubeNode(id_)

# já obteve uma árvore em memória ; agora renderiza todos os nodes
class YoutubeNode(Node):
    def __init__(self, id_):
        self.id = template.Variable(id_)

    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except template.VariableDoesNotExist:
            actual_id = self.id

        t = loader.get_template('embed/youtube.html')
        c = Context({'id': actual_id}, autoescape=context.autoescape)
        return t.render(c)


# nome da template tag , nome do callable  --  <p>{% youtube video.media_id %}</p>
register.tag('youtube', do_youtube)

