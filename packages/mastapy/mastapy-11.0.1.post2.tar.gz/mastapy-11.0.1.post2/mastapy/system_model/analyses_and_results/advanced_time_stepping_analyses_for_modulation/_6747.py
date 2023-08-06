﻿'''_6747.py

PowerLoadAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model import _2150
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6586
from mastapy.system_model.analyses_and_results.system_deflections import _2459
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6782
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'PowerLoadAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadAdvancedTimeSteppingAnalysisForModulation',)


class PowerLoadAdvancedTimeSteppingAnalysisForModulation(_6782.VirtualComponentAdvancedTimeSteppingAnalysisForModulation):
    '''PowerLoadAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _POWER_LOAD_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2150.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2150.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6586.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6586.PowerLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2459.PowerLoadSystemDeflection':
        '''PowerLoadSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2459.PowerLoadSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
