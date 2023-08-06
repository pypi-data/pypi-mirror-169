﻿'''_1347.py

OptimizationVariable
'''


from typing import List

from mastapy.utility.units_and_measurements import _1401
from mastapy._internal import constructor, conversion
from mastapy.utility.units_and_measurements.measurements import (
    _1408, _1409, _1410, _1411,
    _1412, _1413, _1414, _1415,
    _1416, _1417, _1418, _1419,
    _1420, _1421, _1422, _1423,
    _1424, _1425, _1426, _1427,
    _1428, _1429, _1430, _1431,
    _1432, _1433, _1434, _1435,
    _1436, _1437, _1438, _1439,
    _1440, _1441, _1442, _1443,
    _1444, _1445, _1446, _1447,
    _1448, _1449, _1450, _1451,
    _1452, _1453, _1454, _1455,
    _1456, _1457, _1458, _1459,
    _1460, _1461, _1462, _1463,
    _1464, _1465, _1466, _1467,
    _1468, _1469, _1470, _1471,
    _1472, _1473, _1474, _1475,
    _1476, _1477, _1478, _1479,
    _1480, _1481, _1482, _1483,
    _1484, _1485, _1486, _1487,
    _1488, _1489, _1490, _1491,
    _1492, _1493, _1494, _1495,
    _1496, _1497, _1498, _1499,
    _1500, _1501, _1502, _1503,
    _1504, _1505, _1506, _1507,
    _1508, _1509, _1510, _1511,
    _1512, _1513, _1514, _1515
)
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_VARIABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'OptimizationVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationVariable',)


class OptimizationVariable(_0.APIBase):
    '''OptimizationVariable

    This is a mastapy class.
    '''

    TYPE = _OPTIMIZATION_VARIABLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OptimizationVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measurement(self) -> '_1401.MeasurementBase':
        '''MeasurementBase: 'Measurement' is the original name of this property.'''

        if _1401.MeasurementBase.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MeasurementBase. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement.setter
    def measurement(self, value: '_1401.MeasurementBase'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_acceleration(self) -> '_1408.Acceleration':
        '''Acceleration: 'Measurement' is the original name of this property.'''

        if _1408.Acceleration.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Acceleration. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_acceleration.setter
    def measurement_of_type_acceleration(self, value: '_1408.Acceleration'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle(self) -> '_1409.Angle':
        '''Angle: 'Measurement' is the original name of this property.'''

        if _1409.Angle.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Angle. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angle.setter
    def measurement_of_type_angle(self, value: '_1409.Angle'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_per_unit_temperature(self) -> '_1410.AnglePerUnitTemperature':
        '''AnglePerUnitTemperature: 'Measurement' is the original name of this property.'''

        if _1410.AnglePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AnglePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angle_per_unit_temperature.setter
    def measurement_of_type_angle_per_unit_temperature(self, value: '_1410.AnglePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_small(self) -> '_1411.AngleSmall':
        '''AngleSmall: 'Measurement' is the original name of this property.'''

        if _1411.AngleSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angle_small.setter
    def measurement_of_type_angle_small(self, value: '_1411.AngleSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_very_small(self) -> '_1412.AngleVerySmall':
        '''AngleVerySmall: 'Measurement' is the original name of this property.'''

        if _1412.AngleVerySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleVerySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angle_very_small.setter
    def measurement_of_type_angle_very_small(self, value: '_1412.AngleVerySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_acceleration(self) -> '_1413.AngularAcceleration':
        '''AngularAcceleration: 'Measurement' is the original name of this property.'''

        if _1413.AngularAcceleration.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularAcceleration. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_acceleration.setter
    def measurement_of_type_angular_acceleration(self, value: '_1413.AngularAcceleration'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_compliance(self) -> '_1414.AngularCompliance':
        '''AngularCompliance: 'Measurement' is the original name of this property.'''

        if _1414.AngularCompliance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularCompliance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_compliance.setter
    def measurement_of_type_angular_compliance(self, value: '_1414.AngularCompliance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_jerk(self) -> '_1415.AngularJerk':
        '''AngularJerk: 'Measurement' is the original name of this property.'''

        if _1415.AngularJerk.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularJerk. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_jerk.setter
    def measurement_of_type_angular_jerk(self, value: '_1415.AngularJerk'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_stiffness(self) -> '_1416.AngularStiffness':
        '''AngularStiffness: 'Measurement' is the original name of this property.'''

        if _1416.AngularStiffness.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularStiffness. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_stiffness.setter
    def measurement_of_type_angular_stiffness(self, value: '_1416.AngularStiffness'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_velocity(self) -> '_1417.AngularVelocity':
        '''AngularVelocity: 'Measurement' is the original name of this property.'''

        if _1417.AngularVelocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularVelocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_angular_velocity.setter
    def measurement_of_type_angular_velocity(self, value: '_1417.AngularVelocity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_area(self) -> '_1418.Area':
        '''Area: 'Measurement' is the original name of this property.'''

        if _1418.Area.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Area. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_area.setter
    def measurement_of_type_area(self, value: '_1418.Area'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_area_small(self) -> '_1419.AreaSmall':
        '''AreaSmall: 'Measurement' is the original name of this property.'''

        if _1419.AreaSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to AreaSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_area_small.setter
    def measurement_of_type_area_small(self, value: '_1419.AreaSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_cycles(self) -> '_1420.Cycles':
        '''Cycles: 'Measurement' is the original name of this property.'''

        if _1420.Cycles.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Cycles. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_cycles.setter
    def measurement_of_type_cycles(self, value: '_1420.Cycles'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_damage(self) -> '_1421.Damage':
        '''Damage: 'Measurement' is the original name of this property.'''

        if _1421.Damage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Damage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_damage.setter
    def measurement_of_type_damage(self, value: '_1421.Damage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_damage_rate(self) -> '_1422.DamageRate':
        '''DamageRate: 'Measurement' is the original name of this property.'''

        if _1422.DamageRate.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to DamageRate. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_damage_rate.setter
    def measurement_of_type_damage_rate(self, value: '_1422.DamageRate'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_data_size(self) -> '_1423.DataSize':
        '''DataSize: 'Measurement' is the original name of this property.'''

        if _1423.DataSize.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to DataSize. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_data_size.setter
    def measurement_of_type_data_size(self, value: '_1423.DataSize'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_decibel(self) -> '_1424.Decibel':
        '''Decibel: 'Measurement' is the original name of this property.'''

        if _1424.Decibel.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Decibel. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_decibel.setter
    def measurement_of_type_decibel(self, value: '_1424.Decibel'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_density(self) -> '_1425.Density':
        '''Density: 'Measurement' is the original name of this property.'''

        if _1425.Density.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Density. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_density.setter
    def measurement_of_type_density(self, value: '_1425.Density'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy(self) -> '_1426.Energy':
        '''Energy: 'Measurement' is the original name of this property.'''

        if _1426.Energy.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Energy. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_energy.setter
    def measurement_of_type_energy(self, value: '_1426.Energy'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_per_unit_area(self) -> '_1427.EnergyPerUnitArea':
        '''EnergyPerUnitArea: 'Measurement' is the original name of this property.'''

        if _1427.EnergyPerUnitArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_energy_per_unit_area.setter
    def measurement_of_type_energy_per_unit_area(self, value: '_1427.EnergyPerUnitArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_per_unit_area_small(self) -> '_1428.EnergyPerUnitAreaSmall':
        '''EnergyPerUnitAreaSmall: 'Measurement' is the original name of this property.'''

        if _1428.EnergyPerUnitAreaSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_energy_per_unit_area_small.setter
    def measurement_of_type_energy_per_unit_area_small(self, value: '_1428.EnergyPerUnitAreaSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_small(self) -> '_1429.EnergySmall':
        '''EnergySmall: 'Measurement' is the original name of this property.'''

        if _1429.EnergySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_energy_small.setter
    def measurement_of_type_energy_small(self, value: '_1429.EnergySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_enum(self) -> '_1430.Enum':
        '''Enum: 'Measurement' is the original name of this property.'''

        if _1430.Enum.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Enum. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_enum.setter
    def measurement_of_type_enum(self, value: '_1430.Enum'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_flow_rate(self) -> '_1431.FlowRate':
        '''FlowRate: 'Measurement' is the original name of this property.'''

        if _1431.FlowRate.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FlowRate. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_flow_rate.setter
    def measurement_of_type_flow_rate(self, value: '_1431.FlowRate'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force(self) -> '_1432.Force':
        '''Force: 'Measurement' is the original name of this property.'''

        if _1432.Force.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Force. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_force.setter
    def measurement_of_type_force(self, value: '_1432.Force'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_length(self) -> '_1433.ForcePerUnitLength':
        '''ForcePerUnitLength: 'Measurement' is the original name of this property.'''

        if _1433.ForcePerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_force_per_unit_length.setter
    def measurement_of_type_force_per_unit_length(self, value: '_1433.ForcePerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_pressure(self) -> '_1434.ForcePerUnitPressure':
        '''ForcePerUnitPressure: 'Measurement' is the original name of this property.'''

        if _1434.ForcePerUnitPressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitPressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_force_per_unit_pressure.setter
    def measurement_of_type_force_per_unit_pressure(self, value: '_1434.ForcePerUnitPressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_temperature(self) -> '_1435.ForcePerUnitTemperature':
        '''ForcePerUnitTemperature: 'Measurement' is the original name of this property.'''

        if _1435.ForcePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_force_per_unit_temperature.setter
    def measurement_of_type_force_per_unit_temperature(self, value: '_1435.ForcePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fraction_measurement_base(self) -> '_1436.FractionMeasurementBase':
        '''FractionMeasurementBase: 'Measurement' is the original name of this property.'''

        if _1436.FractionMeasurementBase.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FractionMeasurementBase. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_fraction_measurement_base.setter
    def measurement_of_type_fraction_measurement_base(self, value: '_1436.FractionMeasurementBase'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_frequency(self) -> '_1437.Frequency':
        '''Frequency: 'Measurement' is the original name of this property.'''

        if _1437.Frequency.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Frequency. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_frequency.setter
    def measurement_of_type_frequency(self, value: '_1437.Frequency'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fuel_consumption_engine(self) -> '_1438.FuelConsumptionEngine':
        '''FuelConsumptionEngine: 'Measurement' is the original name of this property.'''

        if _1438.FuelConsumptionEngine.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelConsumptionEngine. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_fuel_consumption_engine.setter
    def measurement_of_type_fuel_consumption_engine(self, value: '_1438.FuelConsumptionEngine'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fuel_efficiency_vehicle(self) -> '_1439.FuelEfficiencyVehicle':
        '''FuelEfficiencyVehicle: 'Measurement' is the original name of this property.'''

        if _1439.FuelEfficiencyVehicle.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelEfficiencyVehicle. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_fuel_efficiency_vehicle.setter
    def measurement_of_type_fuel_efficiency_vehicle(self, value: '_1439.FuelEfficiencyVehicle'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_gradient(self) -> '_1440.Gradient':
        '''Gradient: 'Measurement' is the original name of this property.'''

        if _1440.Gradient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Gradient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_gradient.setter
    def measurement_of_type_gradient(self, value: '_1440.Gradient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_conductivity(self) -> '_1441.HeatConductivity':
        '''HeatConductivity: 'Measurement' is the original name of this property.'''

        if _1441.HeatConductivity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatConductivity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_heat_conductivity.setter
    def measurement_of_type_heat_conductivity(self, value: '_1441.HeatConductivity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer(self) -> '_1442.HeatTransfer':
        '''HeatTransfer: 'Measurement' is the original name of this property.'''

        if _1442.HeatTransfer.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransfer. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_heat_transfer.setter
    def measurement_of_type_heat_transfer(self, value: '_1442.HeatTransfer'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1443.HeatTransferCoefficientForPlasticGearTooth':
        '''HeatTransferCoefficientForPlasticGearTooth: 'Measurement' is the original name of this property.'''

        if _1443.HeatTransferCoefficientForPlasticGearTooth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth.setter
    def measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self, value: '_1443.HeatTransferCoefficientForPlasticGearTooth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer_resistance(self) -> '_1444.HeatTransferResistance':
        '''HeatTransferResistance: 'Measurement' is the original name of this property.'''

        if _1444.HeatTransferResistance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferResistance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_heat_transfer_resistance.setter
    def measurement_of_type_heat_transfer_resistance(self, value: '_1444.HeatTransferResistance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_impulse(self) -> '_1445.Impulse':
        '''Impulse: 'Measurement' is the original name of this property.'''

        if _1445.Impulse.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Impulse. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_impulse.setter
    def measurement_of_type_impulse(self, value: '_1445.Impulse'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_index(self) -> '_1446.Index':
        '''Index: 'Measurement' is the original name of this property.'''

        if _1446.Index.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Index. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_index.setter
    def measurement_of_type_index(self, value: '_1446.Index'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_integer(self) -> '_1447.Integer':
        '''Integer: 'Measurement' is the original name of this property.'''

        if _1447.Integer.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Integer. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_integer.setter
    def measurement_of_type_integer(self, value: '_1447.Integer'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_inverse_short_length(self) -> '_1448.InverseShortLength':
        '''InverseShortLength: 'Measurement' is the original name of this property.'''

        if _1448.InverseShortLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_inverse_short_length.setter
    def measurement_of_type_inverse_short_length(self, value: '_1448.InverseShortLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_inverse_short_time(self) -> '_1449.InverseShortTime':
        '''InverseShortTime: 'Measurement' is the original name of this property.'''

        if _1449.InverseShortTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_inverse_short_time.setter
    def measurement_of_type_inverse_short_time(self, value: '_1449.InverseShortTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_jerk(self) -> '_1450.Jerk':
        '''Jerk: 'Measurement' is the original name of this property.'''

        if _1450.Jerk.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Jerk. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_jerk.setter
    def measurement_of_type_jerk(self, value: '_1450.Jerk'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_kinematic_viscosity(self) -> '_1451.KinematicViscosity':
        '''KinematicViscosity: 'Measurement' is the original name of this property.'''

        if _1451.KinematicViscosity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to KinematicViscosity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_kinematic_viscosity.setter
    def measurement_of_type_kinematic_viscosity(self, value: '_1451.KinematicViscosity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_long(self) -> '_1452.LengthLong':
        '''LengthLong: 'Measurement' is the original name of this property.'''

        if _1452.LengthLong.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthLong. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_long.setter
    def measurement_of_type_length_long(self, value: '_1452.LengthLong'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_medium(self) -> '_1453.LengthMedium':
        '''LengthMedium: 'Measurement' is the original name of this property.'''

        if _1453.LengthMedium.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthMedium. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_medium.setter
    def measurement_of_type_length_medium(self, value: '_1453.LengthMedium'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_per_unit_temperature(self) -> '_1454.LengthPerUnitTemperature':
        '''LengthPerUnitTemperature: 'Measurement' is the original name of this property.'''

        if _1454.LengthPerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthPerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_per_unit_temperature.setter
    def measurement_of_type_length_per_unit_temperature(self, value: '_1454.LengthPerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_short(self) -> '_1455.LengthShort':
        '''LengthShort: 'Measurement' is the original name of this property.'''

        if _1455.LengthShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_short.setter
    def measurement_of_type_length_short(self, value: '_1455.LengthShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_to_the_fourth(self) -> '_1456.LengthToTheFourth':
        '''LengthToTheFourth: 'Measurement' is the original name of this property.'''

        if _1456.LengthToTheFourth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthToTheFourth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_to_the_fourth.setter
    def measurement_of_type_length_to_the_fourth(self, value: '_1456.LengthToTheFourth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_long(self) -> '_1457.LengthVeryLong':
        '''LengthVeryLong: 'Measurement' is the original name of this property.'''

        if _1457.LengthVeryLong.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryLong. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_very_long.setter
    def measurement_of_type_length_very_long(self, value: '_1457.LengthVeryLong'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_short(self) -> '_1458.LengthVeryShort':
        '''LengthVeryShort: 'Measurement' is the original name of this property.'''

        if _1458.LengthVeryShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_very_short.setter
    def measurement_of_type_length_very_short(self, value: '_1458.LengthVeryShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_short_per_length_short(self) -> '_1459.LengthVeryShortPerLengthShort':
        '''LengthVeryShortPerLengthShort: 'Measurement' is the original name of this property.'''

        if _1459.LengthVeryShortPerLengthShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_length_very_short_per_length_short.setter
    def measurement_of_type_length_very_short_per_length_short(self, value: '_1459.LengthVeryShortPerLengthShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_angular_damping(self) -> '_1460.LinearAngularDamping':
        '''LinearAngularDamping: 'Measurement' is the original name of this property.'''

        if _1460.LinearAngularDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_angular_damping.setter
    def measurement_of_type_linear_angular_damping(self, value: '_1460.LinearAngularDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1461.LinearAngularStiffnessCrossTerm':
        '''LinearAngularStiffnessCrossTerm: 'Measurement' is the original name of this property.'''

        if _1461.LinearAngularStiffnessCrossTerm.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_angular_stiffness_cross_term.setter
    def measurement_of_type_linear_angular_stiffness_cross_term(self, value: '_1461.LinearAngularStiffnessCrossTerm'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_damping(self) -> '_1462.LinearDamping':
        '''LinearDamping: 'Measurement' is the original name of this property.'''

        if _1462.LinearDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_damping.setter
    def measurement_of_type_linear_damping(self, value: '_1462.LinearDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_flexibility(self) -> '_1463.LinearFlexibility':
        '''LinearFlexibility: 'Measurement' is the original name of this property.'''

        if _1463.LinearFlexibility.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearFlexibility. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_flexibility.setter
    def measurement_of_type_linear_flexibility(self, value: '_1463.LinearFlexibility'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_stiffness(self) -> '_1464.LinearStiffness':
        '''LinearStiffness: 'Measurement' is the original name of this property.'''

        if _1464.LinearStiffness.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearStiffness. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_linear_stiffness.setter
    def measurement_of_type_linear_stiffness(self, value: '_1464.LinearStiffness'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass(self) -> '_1465.Mass':
        '''Mass: 'Measurement' is the original name of this property.'''

        if _1465.Mass.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Mass. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_mass.setter
    def measurement_of_type_mass(self, value: '_1465.Mass'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass_per_unit_length(self) -> '_1466.MassPerUnitLength':
        '''MassPerUnitLength: 'Measurement' is the original name of this property.'''

        if _1466.MassPerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_mass_per_unit_length.setter
    def measurement_of_type_mass_per_unit_length(self, value: '_1466.MassPerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass_per_unit_time(self) -> '_1467.MassPerUnitTime':
        '''MassPerUnitTime: 'Measurement' is the original name of this property.'''

        if _1467.MassPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_mass_per_unit_time.setter
    def measurement_of_type_mass_per_unit_time(self, value: '_1467.MassPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_of_inertia(self) -> '_1468.MomentOfInertia':
        '''MomentOfInertia: 'Measurement' is the original name of this property.'''

        if _1468.MomentOfInertia.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertia. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_moment_of_inertia.setter
    def measurement_of_type_moment_of_inertia(self, value: '_1468.MomentOfInertia'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1469.MomentOfInertiaPerUnitLength':
        '''MomentOfInertiaPerUnitLength: 'Measurement' is the original name of this property.'''

        if _1469.MomentOfInertiaPerUnitLength.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_moment_of_inertia_per_unit_length.setter
    def measurement_of_type_moment_of_inertia_per_unit_length(self, value: '_1469.MomentOfInertiaPerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_per_unit_pressure(self) -> '_1470.MomentPerUnitPressure':
        '''MomentPerUnitPressure: 'Measurement' is the original name of this property.'''

        if _1470.MomentPerUnitPressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentPerUnitPressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_moment_per_unit_pressure.setter
    def measurement_of_type_moment_per_unit_pressure(self, value: '_1470.MomentPerUnitPressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_number(self) -> '_1471.Number':
        '''Number: 'Measurement' is the original name of this property.'''

        if _1471.Number.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Number. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_number.setter
    def measurement_of_type_number(self, value: '_1471.Number'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_percentage(self) -> '_1472.Percentage':
        '''Percentage: 'Measurement' is the original name of this property.'''

        if _1472.Percentage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Percentage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_percentage.setter
    def measurement_of_type_percentage(self, value: '_1472.Percentage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power(self) -> '_1473.Power':
        '''Power: 'Measurement' is the original name of this property.'''

        if _1473.Power.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Power. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power.setter
    def measurement_of_type_power(self, value: '_1473.Power'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_per_small_area(self) -> '_1474.PowerPerSmallArea':
        '''PowerPerSmallArea: 'Measurement' is the original name of this property.'''

        if _1474.PowerPerSmallArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerPerSmallArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_per_small_area.setter
    def measurement_of_type_power_per_small_area(self, value: '_1474.PowerPerSmallArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_per_unit_time(self) -> '_1475.PowerPerUnitTime':
        '''PowerPerUnitTime: 'Measurement' is the original name of this property.'''

        if _1475.PowerPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_per_unit_time.setter
    def measurement_of_type_power_per_unit_time(self, value: '_1475.PowerPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small(self) -> '_1476.PowerSmall':
        '''PowerSmall: 'Measurement' is the original name of this property.'''

        if _1476.PowerSmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small.setter
    def measurement_of_type_power_small(self, value: '_1476.PowerSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_area(self) -> '_1477.PowerSmallPerArea':
        '''PowerSmallPerArea: 'Measurement' is the original name of this property.'''

        if _1477.PowerSmallPerArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small_per_area.setter
    def measurement_of_type_power_small_per_area(self, value: '_1477.PowerSmallPerArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1478.PowerSmallPerUnitAreaPerUnitTime':
        '''PowerSmallPerUnitAreaPerUnitTime: 'Measurement' is the original name of this property.'''

        if _1478.PowerSmallPerUnitAreaPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small_per_unit_area_per_unit_time.setter
    def measurement_of_type_power_small_per_unit_area_per_unit_time(self, value: '_1478.PowerSmallPerUnitAreaPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_unit_time(self) -> '_1479.PowerSmallPerUnitTime':
        '''PowerSmallPerUnitTime: 'Measurement' is the original name of this property.'''

        if _1479.PowerSmallPerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_power_small_per_unit_time.setter
    def measurement_of_type_power_small_per_unit_time(self, value: '_1479.PowerSmallPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure(self) -> '_1480.Pressure':
        '''Pressure: 'Measurement' is the original name of this property.'''

        if _1480.Pressure.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Pressure. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_pressure.setter
    def measurement_of_type_pressure(self, value: '_1480.Pressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_per_unit_time(self) -> '_1481.PressurePerUnitTime':
        '''PressurePerUnitTime: 'Measurement' is the original name of this property.'''

        if _1481.PressurePerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressurePerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_pressure_per_unit_time.setter
    def measurement_of_type_pressure_per_unit_time(self, value: '_1481.PressurePerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_velocity_product(self) -> '_1482.PressureVelocityProduct':
        '''PressureVelocityProduct: 'Measurement' is the original name of this property.'''

        if _1482.PressureVelocityProduct.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureVelocityProduct. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_pressure_velocity_product.setter
    def measurement_of_type_pressure_velocity_product(self, value: '_1482.PressureVelocityProduct'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_viscosity_coefficient(self) -> '_1483.PressureViscosityCoefficient':
        '''PressureViscosityCoefficient: 'Measurement' is the original name of this property.'''

        if _1483.PressureViscosityCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureViscosityCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_pressure_viscosity_coefficient.setter
    def measurement_of_type_pressure_viscosity_coefficient(self, value: '_1483.PressureViscosityCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_price(self) -> '_1484.Price':
        '''Price: 'Measurement' is the original name of this property.'''

        if _1484.Price.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Price. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_price.setter
    def measurement_of_type_price(self, value: '_1484.Price'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_quadratic_angular_damping(self) -> '_1485.QuadraticAngularDamping':
        '''QuadraticAngularDamping: 'Measurement' is the original name of this property.'''

        if _1485.QuadraticAngularDamping.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticAngularDamping. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_quadratic_angular_damping.setter
    def measurement_of_type_quadratic_angular_damping(self, value: '_1485.QuadraticAngularDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_quadratic_drag(self) -> '_1486.QuadraticDrag':
        '''QuadraticDrag: 'Measurement' is the original name of this property.'''

        if _1486.QuadraticDrag.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticDrag. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_quadratic_drag.setter
    def measurement_of_type_quadratic_drag(self, value: '_1486.QuadraticDrag'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_rescaled_measurement(self) -> '_1487.RescaledMeasurement':
        '''RescaledMeasurement: 'Measurement' is the original name of this property.'''

        if _1487.RescaledMeasurement.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to RescaledMeasurement. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_rescaled_measurement.setter
    def measurement_of_type_rescaled_measurement(self, value: '_1487.RescaledMeasurement'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_rotatum(self) -> '_1488.Rotatum':
        '''Rotatum: 'Measurement' is the original name of this property.'''

        if _1488.Rotatum.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Rotatum. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_rotatum.setter
    def measurement_of_type_rotatum(self, value: '_1488.Rotatum'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_safety_factor(self) -> '_1489.SafetyFactor':
        '''SafetyFactor: 'Measurement' is the original name of this property.'''

        if _1489.SafetyFactor.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SafetyFactor. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_safety_factor.setter
    def measurement_of_type_safety_factor(self, value: '_1489.SafetyFactor'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_specific_acoustic_impedance(self) -> '_1490.SpecificAcousticImpedance':
        '''SpecificAcousticImpedance: 'Measurement' is the original name of this property.'''

        if _1490.SpecificAcousticImpedance.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificAcousticImpedance. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_specific_acoustic_impedance.setter
    def measurement_of_type_specific_acoustic_impedance(self, value: '_1490.SpecificAcousticImpedance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_specific_heat(self) -> '_1491.SpecificHeat':
        '''SpecificHeat: 'Measurement' is the original name of this property.'''

        if _1491.SpecificHeat.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificHeat. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_specific_heat.setter
    def measurement_of_type_specific_heat(self, value: '_1491.SpecificHeat'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1492.SquareRootOfUnitForcePerUnitArea':
        '''SquareRootOfUnitForcePerUnitArea: 'Measurement' is the original name of this property.'''

        if _1492.SquareRootOfUnitForcePerUnitArea.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_square_root_of_unit_force_per_unit_area.setter
    def measurement_of_type_square_root_of_unit_force_per_unit_area(self, value: '_1492.SquareRootOfUnitForcePerUnitArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_stiffness_per_unit_face_width(self) -> '_1493.StiffnessPerUnitFaceWidth':
        '''StiffnessPerUnitFaceWidth: 'Measurement' is the original name of this property.'''

        if _1493.StiffnessPerUnitFaceWidth.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_stiffness_per_unit_face_width.setter
    def measurement_of_type_stiffness_per_unit_face_width(self, value: '_1493.StiffnessPerUnitFaceWidth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_stress(self) -> '_1494.Stress':
        '''Stress: 'Measurement' is the original name of this property.'''

        if _1494.Stress.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Stress. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_stress.setter
    def measurement_of_type_stress(self, value: '_1494.Stress'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature(self) -> '_1495.Temperature':
        '''Temperature: 'Measurement' is the original name of this property.'''

        if _1495.Temperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Temperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_temperature.setter
    def measurement_of_type_temperature(self, value: '_1495.Temperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature_difference(self) -> '_1496.TemperatureDifference':
        '''TemperatureDifference: 'Measurement' is the original name of this property.'''

        if _1496.TemperatureDifference.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperatureDifference. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_temperature_difference.setter
    def measurement_of_type_temperature_difference(self, value: '_1496.TemperatureDifference'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature_per_unit_time(self) -> '_1497.TemperaturePerUnitTime':
        '''TemperaturePerUnitTime: 'Measurement' is the original name of this property.'''

        if _1497.TemperaturePerUnitTime.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperaturePerUnitTime. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_temperature_per_unit_time.setter
    def measurement_of_type_temperature_per_unit_time(self, value: '_1497.TemperaturePerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_text(self) -> '_1498.Text':
        '''Text: 'Measurement' is the original name of this property.'''

        if _1498.Text.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Text. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_text.setter
    def measurement_of_type_text(self, value: '_1498.Text'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermal_contact_coefficient(self) -> '_1499.ThermalContactCoefficient':
        '''ThermalContactCoefficient: 'Measurement' is the original name of this property.'''

        if _1499.ThermalContactCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalContactCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_thermal_contact_coefficient.setter
    def measurement_of_type_thermal_contact_coefficient(self, value: '_1499.ThermalContactCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermal_expansion_coefficient(self) -> '_1500.ThermalExpansionCoefficient':
        '''ThermalExpansionCoefficient: 'Measurement' is the original name of this property.'''

        if _1500.ThermalExpansionCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalExpansionCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_thermal_expansion_coefficient.setter
    def measurement_of_type_thermal_expansion_coefficient(self, value: '_1500.ThermalExpansionCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermo_elastic_factor(self) -> '_1501.ThermoElasticFactor':
        '''ThermoElasticFactor: 'Measurement' is the original name of this property.'''

        if _1501.ThermoElasticFactor.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermoElasticFactor. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_thermo_elastic_factor.setter
    def measurement_of_type_thermo_elastic_factor(self, value: '_1501.ThermoElasticFactor'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time(self) -> '_1502.Time':
        '''Time: 'Measurement' is the original name of this property.'''

        if _1502.Time.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Time. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_time.setter
    def measurement_of_type_time(self, value: '_1502.Time'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time_short(self) -> '_1503.TimeShort':
        '''TimeShort: 'Measurement' is the original name of this property.'''

        if _1503.TimeShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_time_short.setter
    def measurement_of_type_time_short(self, value: '_1503.TimeShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time_very_short(self) -> '_1504.TimeVeryShort':
        '''TimeVeryShort: 'Measurement' is the original name of this property.'''

        if _1504.TimeVeryShort.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeVeryShort. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_time_very_short.setter
    def measurement_of_type_time_very_short(self, value: '_1504.TimeVeryShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque(self) -> '_1505.Torque':
        '''Torque: 'Measurement' is the original name of this property.'''

        if _1505.Torque.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Torque. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque.setter
    def measurement_of_type_torque(self, value: '_1505.Torque'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_converter_inverse_k(self) -> '_1506.TorqueConverterInverseK':
        '''TorqueConverterInverseK: 'Measurement' is the original name of this property.'''

        if _1506.TorqueConverterInverseK.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterInverseK. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque_converter_inverse_k.setter
    def measurement_of_type_torque_converter_inverse_k(self, value: '_1506.TorqueConverterInverseK'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_converter_k(self) -> '_1507.TorqueConverterK':
        '''TorqueConverterK: 'Measurement' is the original name of this property.'''

        if _1507.TorqueConverterK.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterK. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque_converter_k.setter
    def measurement_of_type_torque_converter_k(self, value: '_1507.TorqueConverterK'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_per_unit_temperature(self) -> '_1508.TorquePerUnitTemperature':
        '''TorquePerUnitTemperature: 'Measurement' is the original name of this property.'''

        if _1508.TorquePerUnitTemperature.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerUnitTemperature. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_torque_per_unit_temperature.setter
    def measurement_of_type_torque_per_unit_temperature(self, value: '_1508.TorquePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_velocity(self) -> '_1509.Velocity':
        '''Velocity: 'Measurement' is the original name of this property.'''

        if _1509.Velocity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Velocity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_velocity.setter
    def measurement_of_type_velocity(self, value: '_1509.Velocity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_velocity_small(self) -> '_1510.VelocitySmall':
        '''VelocitySmall: 'Measurement' is the original name of this property.'''

        if _1510.VelocitySmall.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to VelocitySmall. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_velocity_small.setter
    def measurement_of_type_velocity_small(self, value: '_1510.VelocitySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_viscosity(self) -> '_1511.Viscosity':
        '''Viscosity: 'Measurement' is the original name of this property.'''

        if _1511.Viscosity.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Viscosity. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_viscosity.setter
    def measurement_of_type_viscosity(self, value: '_1511.Viscosity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_voltage(self) -> '_1512.Voltage':
        '''Voltage: 'Measurement' is the original name of this property.'''

        if _1512.Voltage.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Voltage. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_voltage.setter
    def measurement_of_type_voltage(self, value: '_1512.Voltage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_volume(self) -> '_1513.Volume':
        '''Volume: 'Measurement' is the original name of this property.'''

        if _1513.Volume.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Volume. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_volume.setter
    def measurement_of_type_volume(self, value: '_1513.Volume'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_wear_coefficient(self) -> '_1514.WearCoefficient':
        '''WearCoefficient: 'Measurement' is the original name of this property.'''

        if _1514.WearCoefficient.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to WearCoefficient. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_wear_coefficient.setter
    def measurement_of_type_wear_coefficient(self, value: '_1514.WearCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_yank(self) -> '_1515.Yank':
        '''Yank: 'Measurement' is the original name of this property.'''

        if _1515.Yank.TYPE not in self.wrapped.Measurement.__class__.__mro__:
            raise CastException('Failed to cast measurement to Yank. Expected: {}.'.format(self.wrapped.Measurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Measurement.__class__)(self.wrapped.Measurement) if self.wrapped.Measurement is not None else None

    @measurement_of_type_yank.setter
    def measurement_of_type_yank(self, value: '_1515.Yank'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def results(self) -> 'List[float]':
        '''List[float]: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Results, float)
        return value
