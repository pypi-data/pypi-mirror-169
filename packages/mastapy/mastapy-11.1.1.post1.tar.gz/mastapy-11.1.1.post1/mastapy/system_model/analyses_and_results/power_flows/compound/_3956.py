﻿'''_3956.py

FaceGearSetCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2272
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _3954, _3955, _3961
from mastapy.system_model.analyses_and_results.power_flows import _3824
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'FaceGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundPowerFlow',)


class FaceGearSetCompoundPowerFlow(_3961.GearSetCompoundPowerFlow):
    '''FaceGearSetCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2272.FaceGearSet':
        '''FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2272.FaceGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2272.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2272.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def face_gears_compound_power_flow(self) -> 'List[_3954.FaceGearCompoundPowerFlow]':
        '''List[FaceGearCompoundPowerFlow]: 'FaceGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsCompoundPowerFlow, constructor.new(_3954.FaceGearCompoundPowerFlow))
        return value

    @property
    def face_meshes_compound_power_flow(self) -> 'List[_3955.FaceGearMeshCompoundPowerFlow]':
        '''List[FaceGearMeshCompoundPowerFlow]: 'FaceMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesCompoundPowerFlow, constructor.new(_3955.FaceGearMeshCompoundPowerFlow))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3824.FaceGearSetPowerFlow]':
        '''List[FaceGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3824.FaceGearSetPowerFlow))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3824.FaceGearSetPowerFlow]':
        '''List[FaceGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3824.FaceGearSetPowerFlow))
        return value
