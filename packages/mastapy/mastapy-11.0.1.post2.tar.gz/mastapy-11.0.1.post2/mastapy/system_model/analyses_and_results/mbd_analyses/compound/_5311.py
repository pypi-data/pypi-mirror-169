﻿'''_5311.py

WormGearSetCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2228
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5309, _5310, _5246
from mastapy.system_model.analyses_and_results.mbd_analyses import _5176
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'WormGearSetCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundMultibodyDynamicsAnalysis',)


class WormGearSetCompoundMultibodyDynamicsAnalysis(_5246.GearSetCompoundMultibodyDynamicsAnalysis):
    '''WormGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2228.WormGearSet':
        '''WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2228.WormGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2228.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2228.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def worm_gears_compound_multibody_dynamics_analysis(self) -> 'List[_5309.WormGearCompoundMultibodyDynamicsAnalysis]':
        '''List[WormGearCompoundMultibodyDynamicsAnalysis]: 'WormGearsCompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsCompoundMultibodyDynamicsAnalysis, constructor.new(_5309.WormGearCompoundMultibodyDynamicsAnalysis))
        return value

    @property
    def worm_meshes_compound_multibody_dynamics_analysis(self) -> 'List[_5310.WormGearMeshCompoundMultibodyDynamicsAnalysis]':
        '''List[WormGearMeshCompoundMultibodyDynamicsAnalysis]: 'WormMeshesCompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesCompoundMultibodyDynamicsAnalysis, constructor.new(_5310.WormGearMeshCompoundMultibodyDynamicsAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5176.WormGearSetMultibodyDynamicsAnalysis]':
        '''List[WormGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5176.WormGearSetMultibodyDynamicsAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5176.WormGearSetMultibodyDynamicsAnalysis]':
        '''List[WormGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5176.WormGearSetMultibodyDynamicsAnalysis))
        return value
