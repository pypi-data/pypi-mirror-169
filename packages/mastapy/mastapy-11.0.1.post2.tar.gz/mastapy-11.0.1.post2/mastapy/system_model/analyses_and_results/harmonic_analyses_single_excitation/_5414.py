﻿'''_5414.py

OilSealHarmonicAnalysisOfSingleExcitation
'''


from mastapy.system_model.part_model import _2144
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6573
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5371
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'OilSealHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealHarmonicAnalysisOfSingleExcitation',)


class OilSealHarmonicAnalysisOfSingleExcitation(_5371.ConnectorHarmonicAnalysisOfSingleExcitation):
    '''OilSealHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _OIL_SEAL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2144.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2144.OilSeal)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6573.OilSealLoadCase':
        '''OilSealLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6573.OilSealLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
