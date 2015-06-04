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
        fields=['scoreR1Q1',
                'scoreR1Q2',
                'scoreR1Q3',
                'scoreR1Q4',
                'scoreR2Q1',
                'scoreR2Q2',
                'scoreR2Q3',
                'scoreR2Q4',
                'scoreR3Q1',
                'scoreR3Q2',
                'scoreR3Q3',
                'scoreR3Q4',],
    )

    dexterity.write_permission(scoreR1Q1='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR1Q1='ntpu.content.IsSuperEditor')
    #form.widget(scoreR1Q1=RadioFieldWidget)
#    form.mode(scoreR1Q1='hidden')
    scoreR1Q1 = schema.Choice(
        title=_(u'Research value'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR1Q2='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR1Q2='ntpu.content.IsSuperEditor')
    #form.widget(scoreR1Q2=RadioFieldWidget)
#    form.mode(scoreR1Q2='hidden')
    scoreR1Q2 = schema.Choice(
        title=_(u'Research Transcend'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR1Q3='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR1Q3='ntpu.content.IsSuperEditor')
#    form.mode(scoreR1Q3='hidden')
    #form.widget(scoreR1Q3=RadioFieldWidget)
    scoreR1Q3 = schema.Choice(
        title=_(u'Research Design and Data Processing'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR1Q4='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR1Q4='ntpu.content.IsSuperEditor')
    #form.widget(scoreR1Q4=RadioFieldWidget)
#    form.mode(scoreR1Q4='hidden')
    scoreR1Q4 = schema.Choice(
        title=_(u'Diction smooth and chart product value'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR2Q1='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR2Q1='ntpu.content.IsSuperEditor')
    #form.widget(scoreR2Q1=RadioFieldWidget)
#    form.mode(scoreR2Q1='hidden')
    scoreR2Q1 = schema.Choice(
        title=_(u'Research value'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR2Q2='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR2Q2='ntpu.content.IsSuperEditor')
    #form.widget(scoreR2Q2=RadioFieldWidget)
#    form.mode(scoreR2Q2='hidden')
    scoreR2Q2 = schema.Choice(
        title=_(u'Research Transcend'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR2Q3='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR2Q3='ntpu.content.IsSuperEditor')
#    form.mode(scoreR2Q3='hidden')
    #form.widget(scoreR2Q3=RadioFieldWidget)
    scoreR2Q3 = schema.Choice(
        title=_(u'Research Design and Data Processing'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR2Q4='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR2Q4='ntpu.content.IsSuperEditor')
    #form.widget(scoreR2Q4=RadioFieldWidget)
#    form.mode(scoreR2Q4='hidden')
    scoreR2Q4 = schema.Choice(
        title=_(u'Diction smooth and chart product value'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR3Q1='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR3Q1='ntpu.content.IsSuperEditor')
    #form.widget(scoreR3Q1=RadioFieldWidget)
#    form.mode(scoreR3Q1='hidden')
    scoreR3Q1 = schema.Choice(
        title=_(u'Research value'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR3Q2='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR3Q2='ntpu.content.IsSuperEditor')
    #form.widget(scoreR3Q2=RadioFieldWidget)
#    form.mode(scoreR3Q2='hidden')
    scoreR3Q2 = schema.Choice(
        title=_(u'Research Transcend'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR3Q3='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR3Q3='ntpu.content.IsSuperEditor')
#    form.mode(scoreR3Q3='hidden')
    #form.widget(scoreR3Q3=RadioFieldWidget)
    scoreR3Q3 = schema.Choice(
        title=_(u'Research Design and Data Processing'),
        vocabulary=Score,
        required=False,
    )

    dexterity.write_permission(scoreR3Q4='ntpu.content.IsExternalReviewer')
    dexterity.read_permission(scoreR3Q4='ntpu.content.IsSuperEditor')
    #form.widget(scoreR3Q4=RadioFieldWidget)
#    form.mode(scoreR3Q4='hidden')
    scoreR3Q4 = schema.Choice(
        title=_(u'Diction smooth and chart product value'),
        vocabulary=Score,
        required=False,
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

    scoreR1Q1 = context_property('scoreR1Q1')
    scoreR1Q2 = context_property('scoreR1Q2')
    scoreR1Q3 = context_property('scoreR1Q3')
    scoreR1Q4 = context_property('scoreR1Q4')

    scoreR2Q1 = context_property('scoreR2Q1')
    scoreR2Q2 = context_property('scoreR2Q2')
    scoreR2Q3 = context_property('scoreR2Q3')
    scoreR2Q4 = context_property('scoreR2Q4')

    scoreR3Q1 = context_property('scoreR3Q1')
    scoreR3Q2 = context_property('scoreR3Q2')
    scoreR3Q3 = context_property('scoreR3Q3')
    scoreR3Q4 = context_property('scoreR3Q4')
