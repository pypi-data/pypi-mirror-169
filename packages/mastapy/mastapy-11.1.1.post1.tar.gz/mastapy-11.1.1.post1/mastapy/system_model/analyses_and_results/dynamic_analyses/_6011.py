﻿'''_6011.py

BevelDifferentialSunGearDynamicAnalysis
'''


from mastapy.system_model.part_model.gears import _2261
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6007
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'BevelDifferentialSunGearDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGearDynamicAnalysis',)


class BevelDifferentialSunGearDynamicAnalysis(_6007.BevelDifferentialGearDynamicAnalysis):
    '''BevelDifferentialSunGearDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGearDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2261.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2261.BevelDifferentialSunGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None
