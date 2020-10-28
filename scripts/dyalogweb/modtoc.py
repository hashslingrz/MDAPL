from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from sphinx.environment.collectors import toctree
import sys

class toctree(nodes.General, nodes.Element):
    pass

#class ToctreeDirective(Directive):

#    def run(self):
#        return [toctree('')]

#class TodoDirective(SphinxDirective):

def modify_toc_url(app, doctree):
    print("Pig Poop Balls")
    for node in doctree.traverse():
        print(node)

def setup(app):
    app.add_node(toctree)
    #app.add_directive('todolist', TodolistDirective)
    #app.connect('doctree-resolved', process_todo_nodes)
    #app.add_directive('toctree', ToctreeDirective)
    app.connect('doctree-read', modify_toc_url)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
