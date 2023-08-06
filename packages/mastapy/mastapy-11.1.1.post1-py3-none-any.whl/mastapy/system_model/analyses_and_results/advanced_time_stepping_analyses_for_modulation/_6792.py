﻿'''_6792.py

GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
'''


from mastapy.system_model.part_model import _2199
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6614
from mastapy.system_model.analyses_and_results.system_deflections import _2500
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6756
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'GuideDxfModelAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelAdvancedTimeSteppingAnalysisForModulation',)


class GuideDxfModelAdvancedTimeSteppingAnalysisForModulation(_6756.ComponentAdvancedTimeSteppingAnalysisForModulation):
    '''GuideDxfModelAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2199.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2199.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6614.GuideDxfModelLoadCase':
        '''GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6614.GuideDxfModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2500.GuideDxfModelSystemDeflection':
        '''GuideDxfModelSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2500.GuideDxfModelSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
