﻿'''_4692.py

SpringDamperHalfModalAnalysisAtAStiffness
'''


from mastapy.system_model.part_model.couplings import _2344
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6679
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4626
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'SpringDamperHalfModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfModalAnalysisAtAStiffness',)


class SpringDamperHalfModalAnalysisAtAStiffness(_4626.CouplingHalfModalAnalysisAtAStiffness):
    '''SpringDamperHalfModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2344.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2344.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6679.SpringDamperHalfLoadCase':
        '''SpringDamperHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6679.SpringDamperHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
