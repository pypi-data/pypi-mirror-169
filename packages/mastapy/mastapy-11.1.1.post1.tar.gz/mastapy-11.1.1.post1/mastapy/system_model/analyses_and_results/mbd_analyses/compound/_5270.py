﻿'''_5270.py

BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2259
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5268, _5269, _5275
from mastapy.system_model.analyses_and_results.mbd_analyses import _5120
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis',)


class BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis(_5275.BevelGearSetCompoundMultibodyDynamicsAnalysis):
    '''BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2259.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2259.BevelDifferentialGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2259.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2259.BevelDifferentialGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def bevel_differential_gears_compound_multibody_dynamics_analysis(self) -> 'List[_5268.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]: 'BevelDifferentialGearsCompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearsCompoundMultibodyDynamicsAnalysis, constructor.new(_5268.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis))
        return value

    @property
    def bevel_differential_meshes_compound_multibody_dynamics_analysis(self) -> 'List[_5269.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]: 'BevelDifferentialMeshesCompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialMeshesCompoundMultibodyDynamicsAnalysis, constructor.new(_5269.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5120.BevelDifferentialGearSetMultibodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5120.BevelDifferentialGearSetMultibodyDynamicsAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5120.BevelDifferentialGearSetMultibodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5120.BevelDifferentialGearSetMultibodyDynamicsAnalysis))
        return value
