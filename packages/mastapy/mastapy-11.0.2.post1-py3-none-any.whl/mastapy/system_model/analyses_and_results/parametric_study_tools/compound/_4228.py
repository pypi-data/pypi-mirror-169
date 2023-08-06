﻿'''_4228.py

UnbalancedMassCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model import _2156
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4099
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4229
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'UnbalancedMassCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundParametricStudyTool',)


class UnbalancedMassCompoundParametricStudyTool(_4229.VirtualComponentCompoundParametricStudyTool):
    '''UnbalancedMassCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2156.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2156.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4099.UnbalancedMassParametricStudyTool]':
        '''List[UnbalancedMassParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_4099.UnbalancedMassParametricStudyTool))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4099.UnbalancedMassParametricStudyTool]':
        '''List[UnbalancedMassParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_4099.UnbalancedMassParametricStudyTool))
        return value
