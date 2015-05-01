from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from plone.directives import form, dexterity
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.namedfile.field import NamedBlobFile

from ntpu.behavior import MessageFactory as _


class IAttachedFile(model.Schema):
    """
       Marker/Form interface for AttachedFile
    """
    form.fieldset(
        _(u'Manuscript file'),
        label=_(u"Manuscript file"),
        fields=['attachFile'],
        description=_(u'Please upload Manuscript file, and you can upload images after submitting.'),
    )

    dexterity.write_permission(attachFile='ntpu.content.IsOwner')
    attachFile = NamedBlobFile(
        title=_(u'Manuscript file'),
        required = False,
    )


alsoProvides(IAttachedFile, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class AttachedFile(object):
    """
       Adapter for AttachedFile
    """
    implements(IAttachedFile)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    attachFile = context_property('attachFile')
