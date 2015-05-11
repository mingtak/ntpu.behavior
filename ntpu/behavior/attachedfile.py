from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from plone.directives import form, dexterity
from zope.component import adapts
from zope.interface import alsoProvides, implements, invariant, Invalid
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone import api

from ntpu.behavior import MessageFactory as _


class IAttachedFile(model.Schema):
    """
       Marker/Form interface for AttachedFile
    """
    form.fieldset(
        _(u'Manuscript file'),
        label=_(u"Manuscript file"),
        fields=['attachFile',
                'commentReply',
                'attachImage1',
                'attachImage2' ,
                'attachImage3' ,
                'attachImage4' ,
                'attachImage5' ,
                'attachImage6' ,
                'attachImage7' ,
                'attachImage8' ,
                'attachImage9' ,
                'attachImage10',],
#        description=_(u'Please upload Manuscript file, and you can upload images after submitting.'),
    )

    dexterity.write_permission(attachFile='ntpu.content.IsOwner')
    attachFile = NamedBlobFile(
        title=_(u'Manuscript file'),
        required = False,
    )

    dexterity.write_permission(attachFile='ntpu.content.IsOwner')
    form.mode(commentReply='hidden')
    commentReply = NamedBlobFile(
        title=_('Comment reply'),
        required = False,
    )

    dexterity.write_permission(attachImage1='ntpu.content.IsOwner')
    attachImage1 = NamedBlobImage(
        title=_(u'First attach image'),
        required = False,
    )

    dexterity.write_permission(attachImage2='ntpu.content.IsOwner')
    attachImage2 = NamedBlobImage(
        title=_(u'Second attach image'),
        required = False,
    )

    dexterity.write_permission(attachImage3='ntpu.content.IsOwner')
    attachImage3 = NamedBlobImage(
        title=_(u'Third attach image'),
        required = False,
    )

    dexterity.write_permission(attachImage4='ntpu.content.IsOwner')
    attachImage4 = NamedBlobImage(
        title=_(u'4th attach image'),
        required = False,
    )

    dexterity.write_permission(attachImage5='ntpu.content.IsOwner')
    attachImage5 = NamedBlobImage(
        title=_(u'5th attach image'),
        required = False,
    )


    dexterity.write_permission(attachImage6='ntpu.content.IsOwner')
    attachImage6 = NamedBlobImage(
        title=_(u'6th attach image'),
        required = False,
    )


    dexterity.write_permission(attachImage7='ntpu.content.IsOwner')
    attachImage7 = NamedBlobImage(
        title=_(u'7th attach image'),
        required = False,
    )

    dexterity.write_permission(attachImage8='ntpu.content.IsOwner')
    attachImage8 = NamedBlobImage(
        title=_(u'8th attach image'),
        required = False,
    )

    dexterity.write_permission(attachImage9='ntpu.content.IsOwner')
    attachImage9 = NamedBlobImage(
        title=_(u'9th attach image'),
        required = False,
    )

    dexterity.write_permission(attachImage10='ntpu.content.IsOwner')
    attachImage10 = NamedBlobImage(
        title=_(u'10th attach image'),
        required = False,
    )

    @invariant
    def checkFileType(data):
        if data.attachFile is None:
            return
        subFileName = data.attachFile.filename.split('.')[-1].lower()
        if subFileName in [u'doc', u'docx']:
            return
        else:
            portal = api.portal.get()
            request = portal.REQUEST
            message = _(u'Please upload *.doc or *.docx file.')
            api.portal.show_message(message=message, request=request, type='error')
            raise Invalid(message)


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
    commentReply = context_property('commentReply')
    attachImage1 = context_property('attachImage1')
    attachImage2 = context_property('attachImage2')
    attachImage3 = context_property('attachImage3')
    attachImage4 = context_property('attachImage4')
    attachImage5 = context_property('attachImage5')
    attachImage6 = context_property('attachImage6')
    attachImage7 = context_property('attachImage7')
    attachImage8 = context_property('attachImage8')
    attachImage9 = context_property('attachImage9')
    attachImage10 = context_property('attachImage10')
