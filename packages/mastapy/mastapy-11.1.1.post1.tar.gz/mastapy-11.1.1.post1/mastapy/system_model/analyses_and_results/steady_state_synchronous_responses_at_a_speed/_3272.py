﻿'''_3272.py

ConceptGearSetSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2265
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6560
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3273, _3271, _3301
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'ConceptGearSetSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetSteadyStateSynchronousResponseAtASpeed',)


class ConceptGearSetSteadyStateSynchronousResponseAtASpeed(_3301.GearSetSteadyStateSynchronousResponseAtASpeed):
    '''ConceptGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2265.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2265.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6560.ConceptGearSetLoadCase':
        '''ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6560.ConceptGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def concept_gears_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3273.ConceptGearSteadyStateSynchronousResponseAtASpeed]':
        '''List[ConceptGearSteadyStateSynchronousResponseAtASpeed]: 'ConceptGearsSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsSteadyStateSynchronousResponseAtASpeed, constructor.new(_3273.ConceptGearSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def concept_meshes_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3271.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed]':
        '''List[ConceptGearMeshSteadyStateSynchronousResponseAtASpeed]: 'ConceptMeshesSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesSteadyStateSynchronousResponseAtASpeed, constructor.new(_3271.ConceptGearMeshSteadyStateSynchronousResponseAtASpeed))
        return value
