﻿'''_5904.py

TorqueConverterCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2283
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5740
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5824
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'TorqueConverterCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterCompoundHarmonicAnalysis',)


class TorqueConverterCompoundHarmonicAnalysis(_5824.CouplingCompoundHarmonicAnalysis):
    '''TorqueConverterCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2283.TorqueConverter':
        '''TorqueConverter: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2283.TorqueConverter)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2283.TorqueConverter':
        '''TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2283.TorqueConverter)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5740.TorqueConverterHarmonicAnalysis]':
        '''List[TorqueConverterHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5740.TorqueConverterHarmonicAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5740.TorqueConverterHarmonicAnalysis]':
        '''List[TorqueConverterHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5740.TorqueConverterHarmonicAnalysis))
        return value
