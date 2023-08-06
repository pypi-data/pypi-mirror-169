﻿'''_4162.py

FEPartCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model import _2131
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4022
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4108
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'FEPartCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartCompoundParametricStudyTool',)


class FEPartCompoundParametricStudyTool(_4108.AbstractShaftOrHousingCompoundParametricStudyTool):
    '''FEPartCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _FE_PART_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEPartCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2131.FEPart':
        '''FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2131.FEPart)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4022.FEPartParametricStudyTool]':
        '''List[FEPartParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_4022.FEPartParametricStudyTool))
        return value

    @property
    def planetaries(self) -> 'List[FEPartCompoundParametricStudyTool]':
        '''List[FEPartCompoundParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(FEPartCompoundParametricStudyTool))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4022.FEPartParametricStudyTool]':
        '''List[FEPartParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_4022.FEPartParametricStudyTool))
        return value
