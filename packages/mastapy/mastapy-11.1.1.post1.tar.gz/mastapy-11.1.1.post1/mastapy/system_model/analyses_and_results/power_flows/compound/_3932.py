﻿'''_3932.py

ConceptGearSetCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2265
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _3930, _3931, _3961
from mastapy.system_model.analyses_and_results.power_flows import _3799
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ConceptGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundPowerFlow',)


class ConceptGearSetCompoundPowerFlow(_3961.GearSetCompoundPowerFlow):
    '''ConceptGearSetCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2265.ConceptGearSet':
        '''ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2265.ConceptGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2265.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2265.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def concept_gears_compound_power_flow(self) -> 'List[_3930.ConceptGearCompoundPowerFlow]':
        '''List[ConceptGearCompoundPowerFlow]: 'ConceptGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsCompoundPowerFlow, constructor.new(_3930.ConceptGearCompoundPowerFlow))
        return value

    @property
    def concept_meshes_compound_power_flow(self) -> 'List[_3931.ConceptGearMeshCompoundPowerFlow]':
        '''List[ConceptGearMeshCompoundPowerFlow]: 'ConceptMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesCompoundPowerFlow, constructor.new(_3931.ConceptGearMeshCompoundPowerFlow))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3799.ConceptGearSetPowerFlow]':
        '''List[ConceptGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3799.ConceptGearSetPowerFlow))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3799.ConceptGearSetPowerFlow]':
        '''List[ConceptGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3799.ConceptGearSetPowerFlow))
        return value
