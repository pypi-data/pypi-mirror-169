﻿'''_5431.py

ShaftHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model.shaft_model import _2159
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6597
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5336
from mastapy._internal.python_net import python_net_import

_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ShaftHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHarmonicAnalysisOfSingleExcitation',)


class ShaftHarmonicAnalysisOfSingleExcitation(_5336.AbstractShaftHarmonicAnalysisOfSingleExcitation):
    '''ShaftHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2159.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2159.Shaft)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6597.ShaftLoadCase':
        '''ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6597.ShaftLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[ShaftHarmonicAnalysisOfSingleExcitation]':
        '''List[ShaftHarmonicAnalysisOfSingleExcitation]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftHarmonicAnalysisOfSingleExcitation))
        return value
