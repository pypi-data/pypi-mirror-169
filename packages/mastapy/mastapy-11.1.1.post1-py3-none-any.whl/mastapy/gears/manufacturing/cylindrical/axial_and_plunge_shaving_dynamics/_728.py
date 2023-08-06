﻿'''_728.py

ShavingDynamicsCalculationForDesignedGears
'''


from typing import List, Generic, TypeVar

from mastapy.utility_gui.charts import (
    _1629, _1620, _1625, _1626
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _982
from mastapy._internal.python_net import python_net_import
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _725, _711, _718, _722,
    _727, _726
)

_REPORTING_OVERRIDABLE = python_net_import('SMT.MastaAPI.Utility.Property', 'ReportingOverridable')
_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsCalculationForDesignedGears')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsCalculationForDesignedGears',)


T = TypeVar('T', bound='_726.ShavingDynamics')


class ShavingDynamicsCalculationForDesignedGears(_727.ShavingDynamicsCalculation['T'], Generic[T]):
    '''ShavingDynamicsCalculationForDesignedGears

    This is a mastapy class.

    Generic Types:
        T
    '''

    TYPE = _SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsCalculationForDesignedGears.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def redressing_chart(self) -> '_1629.TwoDChartDefinition':
        '''TwoDChartDefinition: 'RedressingChart' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1629.TwoDChartDefinition.TYPE not in self.wrapped.RedressingChart.__class__.__mro__:
            raise CastException('Failed to cast redressing_chart to TwoDChartDefinition. Expected: {}.'.format(self.wrapped.RedressingChart.__class__.__qualname__))

        return constructor.new_override(self.wrapped.RedressingChart.__class__)(self.wrapped.RedressingChart) if self.wrapped.RedressingChart is not None else None

    @property
    def selected_redressing(self) -> 'list_with_selected_item.ListWithSelectedItem_T':
        '''list_with_selected_item.ListWithSelectedItem_T: 'SelectedRedressing' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_T)(self.wrapped.SelectedRedressing) if self.wrapped.SelectedRedressing is not None else None

    @selected_redressing.setter
    def selected_redressing(self, value: 'list_with_selected_item.ListWithSelectedItem_T.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_T.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_T.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectedRedressing = value

    @property
    def start_of_shaving_profile(self) -> '_982.CylindricalGearProfileMeasurement':
        '''CylindricalGearProfileMeasurement: 'StartOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_982.CylindricalGearProfileMeasurement)(self.wrapped.StartOfShavingProfile.Value) if self.wrapped.StartOfShavingProfile.Value is not None else None

    @property
    def end_of_shaving_profile(self) -> '_982.CylindricalGearProfileMeasurement':
        '''CylindricalGearProfileMeasurement: 'EndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_982.CylindricalGearProfileMeasurement)(self.wrapped.EndOfShavingProfile.Value) if self.wrapped.EndOfShavingProfile.Value is not None else None

    @property
    def redressing(self) -> '_725.ShaverRedressing[T]':
        '''ShaverRedressing[T]: 'Redressing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _725.ShaverRedressing[T].TYPE not in self.wrapped.Redressing.__class__.__mro__:
            raise CastException('Failed to cast redressing to ShaverRedressing[T]. Expected: {}.'.format(self.wrapped.Redressing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Redressing.__class__)(self.wrapped.Redressing) if self.wrapped.Redressing is not None else None

    @property
    def redressing_of_type_axial_shaver_redressing(self) -> '_711.AxialShaverRedressing':
        '''AxialShaverRedressing: 'Redressing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _711.AxialShaverRedressing.TYPE not in self.wrapped.Redressing.__class__.__mro__:
            raise CastException('Failed to cast redressing to AxialShaverRedressing. Expected: {}.'.format(self.wrapped.Redressing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Redressing.__class__)(self.wrapped.Redressing) if self.wrapped.Redressing is not None else None

    @property
    def redressing_of_type_plunge_shaver_redressing(self) -> '_718.PlungeShaverRedressing':
        '''PlungeShaverRedressing: 'Redressing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _718.PlungeShaverRedressing.TYPE not in self.wrapped.Redressing.__class__.__mro__:
            raise CastException('Failed to cast redressing to PlungeShaverRedressing. Expected: {}.'.format(self.wrapped.Redressing.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Redressing.__class__)(self.wrapped.Redressing) if self.wrapped.Redressing is not None else None

    @property
    def redressing_settings(self) -> 'List[_722.RedressingSettings[T]]':
        '''List[RedressingSettings[T]]: 'RedressingSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RedressingSettings, constructor.new(_722.RedressingSettings)[T])
        return value
