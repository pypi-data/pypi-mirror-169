﻿'''_4925.py

BoltedJointCompoundModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2122
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4771
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _5003
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'BoltedJointCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointCompoundModalAnalysis',)


class BoltedJointCompoundModalAnalysis(_5003.SpecialisedAssemblyCompoundModalAnalysis):
    '''BoltedJointCompoundModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2122.BoltedJoint':
        '''BoltedJoint: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2122.BoltedJoint)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2122.BoltedJoint':
        '''BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2122.BoltedJoint)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4771.BoltedJointModalAnalysis]':
        '''List[BoltedJointModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4771.BoltedJointModalAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4771.BoltedJointModalAnalysis]':
        '''List[BoltedJointModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4771.BoltedJointModalAnalysis))
        return value
