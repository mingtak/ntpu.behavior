from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.directives import dexterity, form
from z3c.form.browser.radio import RadioFieldWidget

from ntpu.behavior import MessageFactory as _


Score = SimpleVocabulary(
    [SimpleTerm(value='Perfect', title=_(u'Perfact')),
     SimpleTerm(value='Good', title=_(u'Good')),
     SimpleTerm(value='General', title=_(u'General')),
     SimpleTerm(value='Soso', title=_(u'Soso')),
     SimpleTerm(value='Bad', title=_(u'Bad')),]
)


class IScoreTable(model.Schema):
    """
       Marker/Form interface for ScoreTable
    """

    form.fieldset(
        _(u'Score'),
        label=_(u"Score table"),
        fields=['scoreQ1',
                'scoreQ2',
                'scoreQ3',
                'scoreQ4',],
#        description=_(u'Please upload Manuscript file, and you can upload images after submitting.'),
    )

    dexterity.write_permission(scoreQ1='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreQ1='ntpu.content.IsSuperEditor')
    form.widget(scoreQ1=RadioFieldWidget)
#    form.mode(scoreQ1='hidden')
    scoreQ1 = schema.Choice(
        title=_(u'Research value'),
        vocabulary=Score,
        required=True,
    )

    dexterity.write_permission(scoreQ2='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreQ2='ntpu.content.IsSuperEditor')
    form.widget(scoreQ2=RadioFieldWidget)
#    form.mode(scoreQ2='hidden')
    scoreQ2 = schema.Choice(
        title=_(u'Research Transcend'),
        vocabulary=Score,
        required=True,
    )

    dexterity.write_permission(scoreQ3='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreQ3='ntpu.content.IsSuperEditor')
#    form.mode(scoreQ3='hidden')
    form.widget(scoreQ3=RadioFieldWidget)
    scoreQ3 = schema.Choice(
        title=_(u'Research Design and Data Processing'),
        vocabulary=Score,
        required=True,
    )

    dexterity.write_permission(scoreQ4='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreQ4='ntpu.content.IsSuperEditor')
    form.widget(scoreQ4=RadioFieldWidget)
#    form.mode(scoreQ4='hidden')
    scoreQ4 = schema.Choice(
        title=_(u'Diction smooth and chart product value'),
        vocabulary=Score,
        required=True,
    )


alsoProvides(IScoreTable, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class ScoreTable(object):
    """
       Adapter for ScoreTable
    """
    implements(IScoreTable)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-

    scoreQ1 = context_property('scoreQ1')
    scoreQ2 = context_property('scoreQ2')
    scoreQ3 = context_property('scoreQ3')
    scoreQ4 = context_property('scoreQ4')
