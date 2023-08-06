﻿'''_4555.py

GuideDxfModelModalAnalysisAtASpeed
'''


from mastapy.system_model.part_model import _2133
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6541
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4519
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'GuideDxfModelModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelModalAnalysisAtASpeed',)


class GuideDxfModelModalAnalysisAtASpeed(_4519.ComponentModalAnalysisAtASpeed):
    '''GuideDxfModelModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2133.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2133.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6541.GuideDxfModelLoadCase':
        '''GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6541.GuideDxfModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
