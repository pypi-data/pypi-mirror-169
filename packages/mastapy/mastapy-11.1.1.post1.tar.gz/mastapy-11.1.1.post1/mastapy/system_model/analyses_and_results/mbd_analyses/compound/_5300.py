﻿'''_5300.py

CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.cycloidal import _2311
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5151
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5355
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'CycloidalAssemblyCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblyCompoundMultibodyDynamicsAnalysis',)


class CycloidalAssemblyCompoundMultibodyDynamicsAnalysis(_5355.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis):
    '''CycloidalAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblyCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2311.CycloidalAssembly':
        '''CycloidalAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2311.CycloidalAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2311.CycloidalAssembly':
        '''CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2311.CycloidalAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5151.CycloidalAssemblyMultibodyDynamicsAnalysis]':
        '''List[CycloidalAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5151.CycloidalAssemblyMultibodyDynamicsAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5151.CycloidalAssemblyMultibodyDynamicsAnalysis]':
        '''List[CycloidalAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5151.CycloidalAssemblyMultibodyDynamicsAnalysis))
        return value
