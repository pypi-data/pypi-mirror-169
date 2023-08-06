﻿'''_3718.py

PlanetCarrierCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2213
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3587
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3710
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'PlanetCarrierCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierCompoundStabilityAnalysis',)


class PlanetCarrierCompoundStabilityAnalysis(_3710.MountableComponentCompoundStabilityAnalysis):
    '''PlanetCarrierCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _PLANET_CARRIER_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2213.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2213.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3587.PlanetCarrierStabilityAnalysis]':
        '''List[PlanetCarrierStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3587.PlanetCarrierStabilityAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3587.PlanetCarrierStabilityAnalysis]':
        '''List[PlanetCarrierStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3587.PlanetCarrierStabilityAnalysis))
        return value
