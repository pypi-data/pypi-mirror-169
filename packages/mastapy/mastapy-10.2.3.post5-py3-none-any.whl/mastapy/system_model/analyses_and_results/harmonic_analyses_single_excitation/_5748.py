﻿'''_5748.py

BoltHarmonicAnalysisOfSingleExcitation
'''


from mastapy.system_model.part_model import _2187
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6549
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5753
from mastapy._internal.python_net import python_net_import

_BOLT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'BoltHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltHarmonicAnalysisOfSingleExcitation',)


class BoltHarmonicAnalysisOfSingleExcitation(_5753.ComponentHarmonicAnalysisOfSingleExcitation):
    '''BoltHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _BOLT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2187.Bolt':
        '''Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2187.Bolt)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6549.BoltLoadCase':
        '''BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6549.BoltLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
