﻿'''_5100.py

WormGearMeshCompoundModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2074
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4970
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5035
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'WormGearMeshCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshCompoundModalAnalysisAtASpeed',)


class WormGearMeshCompoundModalAnalysisAtASpeed(_5035.GearMeshCompoundModalAnalysisAtASpeed):
    '''WormGearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearMeshCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2074.WormGearMesh':
        '''WormGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2074.WormGearMesh)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2074.WormGearMesh':
        '''WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2074.WormGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4970.WormGearMeshModalAnalysisAtASpeed]':
        '''List[WormGearMeshModalAnalysisAtASpeed]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_4970.WormGearMeshModalAnalysisAtASpeed))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4970.WormGearMeshModalAnalysisAtASpeed]':
        '''List[WormGearMeshModalAnalysisAtASpeed]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_4970.WormGearMeshModalAnalysisAtASpeed))
        return value
