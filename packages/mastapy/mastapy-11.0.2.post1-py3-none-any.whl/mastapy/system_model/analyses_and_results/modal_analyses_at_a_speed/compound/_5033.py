'''_5033.py

FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.part_model import _2198
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4904
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5074
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'FlexiblePinAssemblyCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyCompoundModalAnalysisAtASpeed',)


class FlexiblePinAssemblyCompoundModalAnalysisAtASpeed(_5074.SpecialisedAssemblyCompoundModalAnalysisAtASpeed):
    '''FlexiblePinAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2198.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2198.FlexiblePinAssembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2198.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2198.FlexiblePinAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4904.FlexiblePinAssemblyModalAnalysisAtASpeed]':
        '''List[FlexiblePinAssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4904.FlexiblePinAssemblyModalAnalysisAtASpeed))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4904.FlexiblePinAssemblyModalAnalysisAtASpeed]':
        '''List[FlexiblePinAssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4904.FlexiblePinAssemblyModalAnalysisAtASpeed))
        return value
