﻿'''_5519.py

PowerLoadHarmonicAnalysis
'''


from mastapy.system_model.part_model import _2216
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6660
from mastapy.system_model.analyses_and_results.system_deflections import _2530
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5557
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'PowerLoadHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadHarmonicAnalysis',)


class PowerLoadHarmonicAnalysis(_5557.VirtualComponentHarmonicAnalysis):
    '''PowerLoadHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _POWER_LOAD_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2216.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2216.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6660.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6660.PowerLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2530.PowerLoadSystemDeflection':
        '''PowerLoadSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2530.PowerLoadSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
