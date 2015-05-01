from five import grok
from plone.indexer import indexer

from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements, Interface, Invalid, invariant
from plone.directives import form

from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid
from plone import api

from ntpu.behavior import MessageFactory as _


def checkEmail(value):
    try:
        checkEmailAddress(value)
    except EmailAddressInvalid:
#        portal = api.portal.get()
#        api.portal.show_message(message='Wrong Eamil format!', request=portal.REQUEST, type='warning')
        raise Invalid(_(u"Invalid email address."))
    return True


class IAuthorInformation(model.Schema):
    """
       Marker/Form interface for AuthorInformation
    """
    form.fieldset(
        _(u'Author Information'),
        label=_(u"Author Information"),
        fields=['authorNameC', 'authorNameE', 'institutionC',
                'institutionE', 'titleC', 'titleE', 'email', 'phone'],
        description=_(u"Enter author information(fields in RED DOT are Required )"),
    )

    authorNameC = schema.TextLine(
        title=_(u'Name(Chinese)'),
        description=_(u'e.g. Da-Ming Wang.'),
        required=True,
    )

    authorNameE = schema.TextLine(
        title=_(u'Name(English)'),
        description=_(u'e.g. Da-Ming Wang'),
        required=True,
    )

    institutionC = schema.TextLine(
        title=_(u'Institution(Chinese)'),
        required=True,
    )

    institutionE = schema.TextLine(
        title=_(u'Institution(English)'),
        required=True,
    )

    titleC = schema.TextLine(
        title=_(u'Title(Chinese)'),
        required=True,
    )

    titleE = schema.TextLine(
        title=_(u'Title(English)'),
        required=True,
    )

    email = schema.TextLine(
        title=_(u'Email'),
#        constraint=checkEmail,
        required=False,
    )

    phone = schema.TextLine(
        title=_('Phone number'),
        required=False,
    )

    @invariant
    def validateEmail(data):
        if data.email is None:
            return True
        try:
            checkEmailAddress(data.email)
        except EmailAddressInvalid:
#            import pdb; pdb.set_trace()
            portal = api.portal.get()
            api.portal.show_message(message='Wrong Eamil format!', request=portal.REQUEST, type='error')
            raise Invalid(_(u"Invalid email address."))
        return True



alsoProvides(IAuthorInformation, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class AuthorInformation(object):
    """
       Adapter for AuthorInformation
    """
    implements(IAuthorInformation)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-

    authorNameC = context_property('authorNameC')
    authorNameE = context_property('authorNameE')
    institutionC = context_property('institutionC')
    institutionE = context_property('institutionE')
    titleC = context_property('titleC')
    titleE = context_property('titleE')
    email = context_property('email')
    phone = context_property('phone')


@indexer(Interface)
def authorNameC_indexer(obj):
    return obj.authorNameC
grok.global_adapter(authorNameC_indexer, name='authorNameC')

@indexer(Interface)
def authorNameE_indexer(obj):
    return obj.authorNameE
grok.global_adapter(authorNameE_indexer, name='authorNameE')

@indexer(Interface)
def institutionC_indexer(obj):
    return obj.institutionC
grok.global_adapter(institutionC_indexer, name='institutionC')

@indexer(Interface)
def institutionE_indexer(obj):
    return obj.institutionE
grok.global_adapter(institutionE_indexer, name='institutionE')

@indexer(Interface)
def titleC_indexer(obj):
    return obj.titleC
grok.global_adapter(titleC_indexer, name='titleC')

@indexer(Interface)
def titleE_indexer(obj):
    return obj.titleE
grok.global_adapter(titleE_indexer, name='titleE')

@indexer(Interface)
def email_indexer(obj):
    return obj.email
grok.global_adapter(email_indexer, name='email')

@indexer(Interface)
def phone_indexer(obj):
    return obj.phone
grok.global_adapter(phone_indexer, name='phone')
