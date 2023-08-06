﻿'''_2490.py

ExternalCADModelSystemDeflection
'''


from mastapy.system_model.part_model import _2196
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6601
from mastapy.system_model.analyses_and_results.power_flows import _3821
from mastapy.system_model.analyses_and_results.system_deflections import _2453
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ExternalCADModelSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelSystemDeflection',)


class ExternalCADModelSystemDeflection(_2453.ComponentSystemDeflection):
    '''ExternalCADModelSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _EXTERNAL_CAD_MODEL_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2196.ExternalCADModel':
        '''ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2196.ExternalCADModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6601.ExternalCADModelLoadCase':
        '''ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6601.ExternalCADModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3821.ExternalCADModelPowerFlow':
        '''ExternalCADModelPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3821.ExternalCADModelPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
