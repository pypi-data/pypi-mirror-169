﻿'''_632.py

HobbingProcessProfileCalculation
'''


from mastapy.utility_gui.charts import (
    _1629, _1620, _1625, _1626
)
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _983
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _623, _627
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_PROFILE_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessProfileCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessProfileCalculation',)


class HobbingProcessProfileCalculation(_627.HobbingProcessCalculation):
    '''HobbingProcessProfileCalculation

    This is a mastapy class.
    '''

    TYPE = _HOBBING_PROCESS_PROFILE_CALCULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HobbingProcessProfileCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_profile_modification_chart(self) -> '_1629.TwoDChartDefinition':
        '''TwoDChartDefinition: 'LeftFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1629.TwoDChartDefinition.TYPE not in self.wrapped.LeftFlankProfileModificationChart.__class__.__mro__:
            raise CastException('Failed to cast left_flank_profile_modification_chart to TwoDChartDefinition. Expected: {}.'.format(self.wrapped.LeftFlankProfileModificationChart.__class__.__qualname__))

        return constructor.new_override(self.wrapped.LeftFlankProfileModificationChart.__class__)(self.wrapped.LeftFlankProfileModificationChart) if self.wrapped.LeftFlankProfileModificationChart is not None else None

    @property
    def right_flank_profile_modification_chart(self) -> '_1629.TwoDChartDefinition':
        '''TwoDChartDefinition: 'RightFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1629.TwoDChartDefinition.TYPE not in self.wrapped.RightFlankProfileModificationChart.__class__.__mro__:
            raise CastException('Failed to cast right_flank_profile_modification_chart to TwoDChartDefinition. Expected: {}.'.format(self.wrapped.RightFlankProfileModificationChart.__class__.__qualname__))

        return constructor.new_override(self.wrapped.RightFlankProfileModificationChart.__class__)(self.wrapped.RightFlankProfileModificationChart) if self.wrapped.RightFlankProfileModificationChart is not None else None

    @property
    def result_z_plane(self) -> 'float':
        '''float: 'ResultZPlane' is the original name of this property.'''

        return self.wrapped.ResultZPlane

    @result_z_plane.setter
    def result_z_plane(self, value: 'float'):
        self.wrapped.ResultZPlane = float(value) if value else 0.0

    @property
    def number_of_profile_bands(self) -> 'int':
        '''int: 'NumberOfProfileBands' is the original name of this property.'''

        return self.wrapped.NumberOfProfileBands

    @number_of_profile_bands.setter
    def number_of_profile_bands(self, value: 'int'):
        self.wrapped.NumberOfProfileBands = int(value) if value else 0

    @property
    def chart_display_method(self) -> '_983.CylindricalGearProfileMeasurementType':
        '''CylindricalGearProfileMeasurementType: 'ChartDisplayMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ChartDisplayMethod)
        return constructor.new(_983.CylindricalGearProfileMeasurementType)(value) if value is not None else None

    @chart_display_method.setter
    def chart_display_method(self, value: '_983.CylindricalGearProfileMeasurementType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ChartDisplayMethod = value

    @property
    def right_flank(self) -> '_623.CalculateProfileDeviationAccuracy':
        '''CalculateProfileDeviationAccuracy: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_623.CalculateProfileDeviationAccuracy)(self.wrapped.RightFlank) if self.wrapped.RightFlank is not None else None

    @property
    def left_flank(self) -> '_623.CalculateProfileDeviationAccuracy':
        '''CalculateProfileDeviationAccuracy: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_623.CalculateProfileDeviationAccuracy)(self.wrapped.LeftFlank) if self.wrapped.LeftFlank is not None else None
