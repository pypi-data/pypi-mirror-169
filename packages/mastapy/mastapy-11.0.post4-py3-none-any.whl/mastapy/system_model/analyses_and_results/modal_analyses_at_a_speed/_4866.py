﻿'''_4866.py

BoltedJointModalAnalysisAtASpeed
'''


from mastapy.system_model.part_model import _2188
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6548
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4945
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'BoltedJointModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointModalAnalysisAtASpeed',)


class BoltedJointModalAnalysisAtASpeed(_4945.SpecialisedAssemblyModalAnalysisAtASpeed):
    '''BoltedJointModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2188.BoltedJoint':
        '''BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2188.BoltedJoint)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6548.BoltedJointLoadCase':
        '''BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6548.BoltedJointLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None
