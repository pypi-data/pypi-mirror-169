﻿'''_1950.py

Design
'''


from typing import List, Optional, TypeVar
from os import path

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.class_property import classproperty
from mastapy.system_model_gui import _1616
from mastapy._internal.python_net import python_net_import
from mastapy.materials.efficiency import _261
from mastapy._internal.implicit import enum_with_selected_value, overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import (
    _2219, _2222, _2216, _2218,
    _2212, _2179, _2180, _2181,
    _2182, _2185, _2187, _2188,
    _2189, _2192, _2193, _2196,
    _2197, _2198, _2199, _2206,
    _2207, _2208, _2210, _2213,
    _2215, _2220, _2221, _2223
)
from mastapy.system_model import (
    _1971, _1972, _1970, _1951
)
from mastapy.gears import _289, _295
from mastapy.gears.materials import _559
from mastapy.utility import _1383, _1382, _1381
from mastapy.shafts import _34
from mastapy.detailed_rigid_connectors.splines import _1194
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.part_model.gears import (
    _2255, _2276, _2256, _2257,
    _2258, _2259, _2260, _2261,
    _2262, _2263, _2264, _2265,
    _2266, _2267, _2268, _2269,
    _2270, _2271, _2272, _2273,
    _2275, _2277, _2278, _2279,
    _2280, _2281, _2282, _2283,
    _2284, _2285, _2286, _2287,
    _2288, _2289, _2290, _2291,
    _2292, _2293, _2294, _2295,
    _2296, _2297
)
from mastapy.system_model.fe import _2106
from mastapy.bearings.bearing_results.rolling import _1732
from mastapy.system_model.part_model.configurations import _2357, _2355, _2358
from mastapy.system_model.analyses_and_results.load_case_groups import _5391, _5399, _5392
from mastapy.system_model.analyses_and_results.static_loads import _6522
from mastapy.utility.model_validation import _1567
from mastapy.system_model.database_access import _2009
from mastapy.bearings.bearing_designs.rolling import _1915
from mastapy.nodal_analysis import _75
from mastapy.system_model.part_model.creation_options import (
    _2314, _2317, _2318, _2316,
    _2315
)
from mastapy.gears.gear_designs.creation_options import _1095, _1098, _1097
from mastapy import _7278, _0
from mastapy.system_model.analyses_and_results.synchroniser_analysis import _2720
from mastapy.system_model.part_model.shaft_model import _2226
from mastapy.system_model.part_model.cycloidal import _2311, _2312, _2313
from mastapy.system_model.part_model.couplings import (
    _2319, _2321, _2322, _2324,
    _2325, _2326, _2327, _2329,
    _2330, _2331, _2332, _2333,
    _2339, _2340, _2341, _2343,
    _2344, _2345, _2347, _2348,
    _2349, _2350, _2351, _2353
)

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ARRAY = python_net_import('System', 'Array')
_STRING = python_net_import('System', 'String')
_BOOLEAN = python_net_import('System', 'Boolean')
_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_DESIGN = python_net_import('SMT.MastaAPI.SystemModel', 'Design')


__docformat__ = 'restructuredtext en'
__all__ = ('Design',)


class Design(_0.APIBase):
    '''Design

    This is a mastapy class.
    '''

    TYPE = _DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Design.TYPE' = None):
        super().__init__(instance_to_wrap if instance_to_wrap else Design.TYPE())
        self._freeze()

    @classproperty
    def available_examples(cls) -> 'List[str]':
        '''List[str]: 'AvailableExamples' is the original name of this property.'''

        value = conversion.pn_to_mp_objects_in_list(Design.TYPE.AvailableExamples, str)
        return value

    @property
    def masta_gui(self) -> '_1616.MASTAGUI':
        '''MASTAGUI: 'MastaGUI' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1616.MASTAGUI)(self.wrapped.MastaGUI) if self.wrapped.MastaGUI is not None else None

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(self) -> 'str':
        '''str: 'ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase' is the original name of this property.'''

        return self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SelectedItemName

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database.setter
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(self, value: 'str'):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(self) -> 'str':
        '''str: 'ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase' is the original name of this property.'''

        return self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SelectedItemName

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database.setter
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(self, value: 'str'):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def volumetric_oil_air_mixture_ratio(self) -> 'float':
        '''float: 'VolumetricOilAirMixtureRatio' is the original name of this property.'''

        return self.wrapped.VolumetricOilAirMixtureRatio

    @volumetric_oil_air_mixture_ratio.setter
    def volumetric_oil_air_mixture_ratio(self, value: 'float'):
        self.wrapped.VolumetricOilAirMixtureRatio = float(value) if value else 0.0

    @property
    def use_element_contact_angles_for_angular_velocities_in_ball_bearings(self) -> 'bool':
        '''bool: 'UseElementContactAnglesForAngularVelocitiesInBallBearings' is the original name of this property.'''

        return self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearings

    @use_element_contact_angles_for_angular_velocities_in_ball_bearings.setter
    def use_element_contact_angles_for_angular_velocities_in_ball_bearings(self, value: 'bool'):
        self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearings = bool(value) if value else False

    @property
    def coefficient_of_friction(self) -> 'float':
        '''float: 'CoefficientOfFriction' is the original name of this property.'''

        return self.wrapped.CoefficientOfFriction

    @coefficient_of_friction.setter
    def coefficient_of_friction(self, value: 'float'):
        self.wrapped.CoefficientOfFriction = float(value) if value else 0.0

    @property
    def efficiency_rating_method_for_bearings(self) -> '_261.BearingEfficiencyRatingMethod':
        '''BearingEfficiencyRatingMethod: 'EfficiencyRatingMethodForBearings' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.EfficiencyRatingMethodForBearings)
        return constructor.new(_261.BearingEfficiencyRatingMethod)(value) if value is not None else None

    @efficiency_rating_method_for_bearings.setter
    def efficiency_rating_method_for_bearings(self, value: '_261.BearingEfficiencyRatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.EfficiencyRatingMethodForBearings = value

    @property
    def efficiency_rating_method_if_skf_loss_model_does_not_provide_losses(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod':
        '''enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod: 'EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses, value) if self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses is not None else None

    @efficiency_rating_method_if_skf_loss_model_does_not_provide_losses.setter
    def efficiency_rating_method_if_skf_loss_model_does_not_provide_losses(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses = value

    @property
    def shaft_diameter_modification_due_to_rolling_bearing_rings(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing':
        '''enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing: 'ShaftDiameterModificationDueToRollingBearingRings' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.ShaftDiameterModificationDueToRollingBearingRings, value) if self.wrapped.ShaftDiameterModificationDueToRollingBearingRings is not None else None

    @shaft_diameter_modification_due_to_rolling_bearing_rings.setter
    def shaft_diameter_modification_due_to_rolling_bearing_rings(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ShaftDiameterModificationDueToRollingBearingRings = value

    @property
    def unbalanced_mass_inclusion(self) -> '_2222.UnbalancedMassInclusionOption':
        '''UnbalancedMassInclusionOption: 'UnbalancedMassInclusion' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.UnbalancedMassInclusion)
        return constructor.new(_2222.UnbalancedMassInclusionOption)(value) if value is not None else None

    @unbalanced_mass_inclusion.setter
    def unbalanced_mass_inclusion(self, value: '_2222.UnbalancedMassInclusionOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.UnbalancedMassInclusion = value

    @property
    def manufacturer(self) -> 'str':
        '''str: 'Manufacturer' is the original name of this property.'''

        return self.wrapped.Manufacturer

    @manufacturer.setter
    def manufacturer(self, value: 'str'):
        self.wrapped.Manufacturer = str(value) if value else ''

    @property
    def housing_material_for_grounded_connections(self) -> 'str':
        '''str: 'HousingMaterialForGroundedConnections' is the original name of this property.'''

        return self.wrapped.HousingMaterialForGroundedConnections.SelectedItemName

    @housing_material_for_grounded_connections.setter
    def housing_material_for_grounded_connections(self, value: 'str'):
        self.wrapped.HousingMaterialForGroundedConnections.SetSelectedItem(str(value) if value else '')

    @property
    def thermal_expansion_for_grounded_nodes(self) -> '_1971.ThermalExpansionOptionForGroundedNodes':
        '''ThermalExpansionOptionForGroundedNodes: 'ThermalExpansionForGroundedNodes' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ThermalExpansionForGroundedNodes)
        return constructor.new(_1971.ThermalExpansionOptionForGroundedNodes)(value) if value is not None else None

    @thermal_expansion_for_grounded_nodes.setter
    def thermal_expansion_for_grounded_nodes(self, value: '_1971.ThermalExpansionOptionForGroundedNodes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ThermalExpansionForGroundedNodes = value

    @property
    def comment(self) -> 'str':
        '''str: 'Comment' is the original name of this property.'''

        return self.wrapped.Comment

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value else ''

    @property
    def node_size(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'NodeSize' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.NodeSize) if self.wrapped.NodeSize is not None else None

    @node_size.setter
    def node_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeSize = value

    @property
    def use_expanded_2d_projection_mode(self) -> 'bool':
        '''bool: 'UseExpanded2DProjectionMode' is the original name of this property.'''

        return self.wrapped.UseExpanded2DProjectionMode

    @use_expanded_2d_projection_mode.setter
    def use_expanded_2d_projection_mode(self, value: 'bool'):
        self.wrapped.UseExpanded2DProjectionMode = bool(value) if value else False

    @property
    def gravity_magnitude(self) -> 'float':
        '''float: 'GravityMagnitude' is the original name of this property.'''

        return self.wrapped.GravityMagnitude

    @gravity_magnitude.setter
    def gravity_magnitude(self, value: 'float'):
        self.wrapped.GravityMagnitude = float(value) if value else 0.0

    @property
    def input_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        '''list_with_selected_item.ListWithSelectedItem_PowerLoad: 'InputPowerLoad' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_PowerLoad)(self.wrapped.InputPowerLoad) if self.wrapped.InputPowerLoad is not None else None

    @input_power_load.setter
    def input_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.InputPowerLoad = value

    @property
    def output_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        '''list_with_selected_item.ListWithSelectedItem_PowerLoad: 'OutputPowerLoad' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_PowerLoad)(self.wrapped.OutputPowerLoad) if self.wrapped.OutputPowerLoad is not None else None

    @output_power_load.setter
    def output_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.OutputPowerLoad = value

    @property
    def design_name(self) -> 'str':
        '''str: 'DesignName' is the original name of this property.'''

        return self.wrapped.DesignName

    @design_name.setter
    def design_name(self, value: 'str'):
        self.wrapped.DesignName = str(value) if value else ''

    @property
    def file_name(self) -> 'str':
        '''str: 'FileName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FileName

    @property
    def gear_set_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'GearSetConfiguration' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.GearSetConfiguration) if self.wrapped.GearSetConfiguration is not None else None

    @gear_set_configuration.setter
    def gear_set_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.GearSetConfiguration = value

    @property
    def number_of_gear_set_configurations(self) -> 'int':
        '''int: 'NumberOfGearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfGearSetConfigurations

    @property
    def shaft_detail_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'ShaftDetailConfiguration' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.ShaftDetailConfiguration) if self.wrapped.ShaftDetailConfiguration is not None else None

    @shaft_detail_configuration.setter
    def shaft_detail_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.ShaftDetailConfiguration = value

    @property
    def fe_substructure_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'FESubstructureConfiguration' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.FESubstructureConfiguration) if self.wrapped.FESubstructureConfiguration is not None else None

    @fe_substructure_configuration.setter
    def fe_substructure_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.FESubstructureConfiguration = value

    @property
    def bearing_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'BearingConfiguration' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.BearingConfiguration) if self.wrapped.BearingConfiguration is not None else None

    @bearing_configuration.setter
    def bearing_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.BearingConfiguration = value

    @property
    def transverse_contact_ratio_requirement(self) -> '_289.ContactRatioRequirements':
        '''ContactRatioRequirements: 'TransverseContactRatioRequirement' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.TransverseContactRatioRequirement)
        return constructor.new(_289.ContactRatioRequirements)(value) if value is not None else None

    @transverse_contact_ratio_requirement.setter
    def transverse_contact_ratio_requirement(self, value: '_289.ContactRatioRequirements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.TransverseContactRatioRequirement = value

    @property
    def axial_contact_ratio_requirement(self) -> '_289.ContactRatioRequirements':
        '''ContactRatioRequirements: 'AxialContactRatioRequirement' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.AxialContactRatioRequirement)
        return constructor.new(_289.ContactRatioRequirements)(value) if value is not None else None

    @axial_contact_ratio_requirement.setter
    def axial_contact_ratio_requirement(self, value: '_289.ContactRatioRequirements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AxialContactRatioRequirement = value

    @property
    def maximum_acceptable_axial_contact_ratio(self) -> 'float':
        '''float: 'MaximumAcceptableAxialContactRatio' is the original name of this property.'''

        return self.wrapped.MaximumAcceptableAxialContactRatio

    @maximum_acceptable_axial_contact_ratio.setter
    def maximum_acceptable_axial_contact_ratio(self, value: 'float'):
        self.wrapped.MaximumAcceptableAxialContactRatio = float(value) if value else 0.0

    @property
    def minimum_acceptable_axial_contact_ratio(self) -> 'float':
        '''float: 'MinimumAcceptableAxialContactRatio' is the original name of this property.'''

        return self.wrapped.MinimumAcceptableAxialContactRatio

    @minimum_acceptable_axial_contact_ratio.setter
    def minimum_acceptable_axial_contact_ratio(self, value: 'float'):
        self.wrapped.MinimumAcceptableAxialContactRatio = float(value) if value else 0.0

    @property
    def maximum_acceptable_axial_contact_ratio_above_integer(self) -> 'float':
        '''float: 'MaximumAcceptableAxialContactRatioAboveInteger' is the original name of this property.'''

        return self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger

    @maximum_acceptable_axial_contact_ratio_above_integer.setter
    def maximum_acceptable_axial_contact_ratio_above_integer(self, value: 'float'):
        self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger = float(value) if value else 0.0

    @property
    def minimum_acceptable_axial_contact_ratio_below_integer(self) -> 'float':
        '''float: 'MinimumAcceptableAxialContactRatioBelowInteger' is the original name of this property.'''

        return self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger

    @minimum_acceptable_axial_contact_ratio_below_integer.setter
    def minimum_acceptable_axial_contact_ratio_below_integer(self, value: 'float'):
        self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger = float(value) if value else 0.0

    @property
    def maximum_acceptable_transverse_contact_ratio(self) -> 'float':
        '''float: 'MaximumAcceptableTransverseContactRatio' is the original name of this property.'''

        return self.wrapped.MaximumAcceptableTransverseContactRatio

    @maximum_acceptable_transverse_contact_ratio.setter
    def maximum_acceptable_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.MaximumAcceptableTransverseContactRatio = float(value) if value else 0.0

    @property
    def minimum_acceptable_transverse_contact_ratio(self) -> 'float':
        '''float: 'MinimumAcceptableTransverseContactRatio' is the original name of this property.'''

        return self.wrapped.MinimumAcceptableTransverseContactRatio

    @minimum_acceptable_transverse_contact_ratio.setter
    def minimum_acceptable_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.MinimumAcceptableTransverseContactRatio = float(value) if value else 0.0

    @property
    def maximum_acceptable_transverse_contact_ratio_above_integer(self) -> 'float':
        '''float: 'MaximumAcceptableTransverseContactRatioAboveInteger' is the original name of this property.'''

        return self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger

    @maximum_acceptable_transverse_contact_ratio_above_integer.setter
    def maximum_acceptable_transverse_contact_ratio_above_integer(self, value: 'float'):
        self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger = float(value) if value else 0.0

    @property
    def minimum_acceptable_transverse_contact_ratio_below_integer(self) -> 'float':
        '''float: 'MinimumAcceptableTransverseContactRatioBelowInteger' is the original name of this property.'''

        return self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger

    @minimum_acceptable_transverse_contact_ratio_below_integer.setter
    def minimum_acceptable_transverse_contact_ratio_below_integer(self, value: 'float'):
        self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger = float(value) if value else 0.0

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_external_external_meshes(self) -> '_559.ISOTR1417912001CoefficientOfFrictionConstants':
        '''ISOTR1417912001CoefficientOfFrictionConstants: 'ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_559.ISOTR1417912001CoefficientOfFrictionConstants)(self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes) if self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes is not None else None

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes(self) -> '_559.ISOTR1417912001CoefficientOfFrictionConstants':
        '''ISOTR1417912001CoefficientOfFrictionConstants: 'ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_559.ISOTR1417912001CoefficientOfFrictionConstants)(self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes) if self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes is not None else None

    @property
    def file_save_details_most_recent(self) -> '_1383.FileHistoryItem':
        '''FileHistoryItem: 'FileSaveDetailsMostRecent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1383.FileHistoryItem)(self.wrapped.FileSaveDetailsMostRecent) if self.wrapped.FileSaveDetailsMostRecent is not None else None

    @property
    def default_system_temperatures(self) -> '_1972.TransmissionTemperatureSet':
        '''TransmissionTemperatureSet: 'DefaultSystemTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1972.TransmissionTemperatureSet)(self.wrapped.DefaultSystemTemperatures) if self.wrapped.DefaultSystemTemperatures is not None else None

    @property
    def shafts(self) -> '_34.ShaftSafetyFactorSettings':
        '''ShaftSafetyFactorSettings: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_34.ShaftSafetyFactorSettings)(self.wrapped.Shafts) if self.wrapped.Shafts is not None else None

    @property
    def detailed_spline_settings(self) -> '_1194.DetailedSplineJointSettings':
        '''DetailedSplineJointSettings: 'DetailedSplineSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1194.DetailedSplineJointSettings)(self.wrapped.DetailedSplineSettings) if self.wrapped.DetailedSplineSettings is not None else None

    @property
    def gravity_vector_components(self) -> 'Vector3D':
        '''Vector3D: 'GravityVectorComponents' is the original name of this property.'''

        value = conversion.pn_to_mp_vector3d(self.wrapped.GravityVectorComponents)
        return value

    @gravity_vector_components.setter
    def gravity_vector_components(self, value: 'Vector3D'):
        value = value if value else None
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.GravityVectorComponents = value

    @property
    def gravity_orientation(self) -> 'Vector3D':
        '''Vector3D: 'GravityOrientation' is the original name of this property.'''

        value = conversion.pn_to_mp_vector3d(self.wrapped.GravityOrientation)
        return value

    @gravity_orientation.setter
    def gravity_orientation(self, value: 'Vector3D'):
        value = value if value else None
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.GravityOrientation = value

    @property
    def file_save_details_all(self) -> '_1382.FileHistory':
        '''FileHistory: 'FileSaveDetailsAll' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1382.FileHistory)(self.wrapped.FileSaveDetailsAll) if self.wrapped.FileSaveDetailsAll is not None else None

    @property
    def gear_set_design_group(self) -> '_295.GearSetDesignGroup':
        '''GearSetDesignGroup: 'GearSetDesignGroup' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_295.GearSetDesignGroup)(self.wrapped.GearSetDesignGroup) if self.wrapped.GearSetDesignGroup is not None else None

    @property
    def selected_gear_set_selection_group(self) -> '_2255.ActiveGearSetDesignSelectionGroup':
        '''ActiveGearSetDesignSelectionGroup: 'SelectedGearSetSelectionGroup' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2255.ActiveGearSetDesignSelectionGroup)(self.wrapped.SelectedGearSetSelectionGroup) if self.wrapped.SelectedGearSetSelectionGroup is not None else None

    @property
    def system(self) -> '_1970.SystemReporting':
        '''SystemReporting: 'System' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1970.SystemReporting)(self.wrapped.System) if self.wrapped.System is not None else None

    @property
    def fe_batch_operations(self) -> '_2106.BatchOperations':
        '''BatchOperations: 'FEBatchOperations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2106.BatchOperations)(self.wrapped.FEBatchOperations) if self.wrapped.FEBatchOperations is not None else None

    @property
    def iso14179_settings_per_bearing_type(self) -> 'List[_1732.ISO14179SettingsPerBearingType]':
        '''List[ISO14179SettingsPerBearingType]: 'ISO14179SettingsPerBearingType' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ISO14179SettingsPerBearingType, constructor.new(_1732.ISO14179SettingsPerBearingType))
        return value

    @property
    def gear_set_configurations(self) -> 'List[_2255.ActiveGearSetDesignSelectionGroup]':
        '''List[ActiveGearSetDesignSelectionGroup]: 'GearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearSetConfigurations, constructor.new(_2255.ActiveGearSetDesignSelectionGroup))
        return value

    @property
    def shaft_detail_configurations(self) -> 'List[_2357.ActiveShaftDesignSelectionGroup]':
        '''List[ActiveShaftDesignSelectionGroup]: 'ShaftDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftDetailConfigurations, constructor.new(_2357.ActiveShaftDesignSelectionGroup))
        return value

    @property
    def fe_substructure_configurations(self) -> 'List[_2355.ActiveFESubstructureSelectionGroup]':
        '''List[ActiveFESubstructureSelectionGroup]: 'FESubstructureConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FESubstructureConfigurations, constructor.new(_2355.ActiveFESubstructureSelectionGroup))
        return value

    @property
    def bearing_detail_configurations(self) -> 'List[_2358.BearingDetailConfiguration]':
        '''List[BearingDetailConfiguration]: 'BearingDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BearingDetailConfigurations, constructor.new(_2358.BearingDetailConfiguration))
        return value

    @property
    def design_states(self) -> 'List[_5391.DesignState]':
        '''List[DesignState]: 'DesignStates' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DesignStates, constructor.new(_5391.DesignState))
        return value

    @property
    def time_series_load_case_groups(self) -> 'List[_5399.TimeSeriesLoadCaseGroup]':
        '''List[TimeSeriesLoadCaseGroup]: 'TimeSeriesLoadCaseGroups' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TimeSeriesLoadCaseGroups, constructor.new(_5399.TimeSeriesLoadCaseGroup))
        return value

    @property
    def static_loads(self) -> 'List[_6522.StaticLoadCase]':
        '''List[StaticLoadCase]: 'StaticLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StaticLoads, constructor.new(_6522.StaticLoadCase))
        return value

    @property
    def duty_cycles(self) -> 'List[_5392.DutyCycle]':
        '''List[DutyCycle]: 'DutyCycles' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DutyCycles, constructor.new(_5392.DutyCycle))
        return value

    @property
    def root_assembly(self) -> '_2218.RootAssembly':
        '''RootAssembly: 'RootAssembly' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2218.RootAssembly)(self.wrapped.RootAssembly) if self.wrapped.RootAssembly is not None else None

    @property
    def gear_set_config(self) -> '_2276.GearSetConfiguration':
        '''GearSetConfiguration: 'GearSetConfig' is the original name of this property.'''

        return constructor.new(_2276.GearSetConfiguration)(self.wrapped.GearSetConfig) if self.wrapped.GearSetConfig is not None else None

    @gear_set_config.setter
    def gear_set_config(self, value: '_2276.GearSetConfiguration'):
        value = value.wrapped if value else None
        self.wrapped.GearSetConfig = value

    @property
    def status(self) -> '_1567.Status':
        '''Status: 'Status' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1567.Status)(self.wrapped.Status) if self.wrapped.Status is not None else None

    @property
    def databases(self) -> '_2009.Databases':
        '''Databases: 'Databases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2009.Databases)(self.wrapped.Databases) if self.wrapped.Databases is not None else None

    @property
    def masta_settings(self) -> '_1951.MastaSettings':
        '''MastaSettings: 'MastaSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1951.MastaSettings)(self.wrapped.MastaSettings) if self.wrapped.MastaSettings is not None else None

    def clear_design(self):
        ''' 'ClearDesign' is the original name of this method.'''

        self.wrapped.ClearDesign()

    def remove_bearing_from_database(self, rolling_bearing: '_1915.RollingBearing'):
        ''' 'RemoveBearingFromDatabase' is the original name of this method.

        Args:
            rolling_bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        '''

        self.wrapped.RemoveBearingFromDatabase(rolling_bearing.wrapped if rolling_bearing else None)

    def new_nodal_matrix(self, dense_matrix: 'List[List[float]]') -> '_75.NodalMatrix':
        ''' 'NewNodalMatrix' is the original name of this method.

        Args:
            dense_matrix (List[List[float]])

        Returns:
            mastapy.nodal_analysis.NodalMatrix
        '''

        dense_matrix = conversion.mp_to_pn_list_float_2d(dense_matrix)
        method_result = self.wrapped.NewNodalMatrix(dense_matrix)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def new_belt_creation_options(self, centre_distance: Optional['float'] = 0.1, pulley_a_diameter: Optional['float'] = 0.08, pulley_b_diameter: Optional['float'] = 0.08, name: Optional['str'] = 'Belt Drive') -> '_2314.BeltCreationOptions':
        ''' 'NewBeltCreationOptions' is the original name of this method.

        Args:
            centre_distance (float, optional)
            pulley_a_diameter (float, optional)
            pulley_b_diameter (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.BeltCreationOptions
        '''

        centre_distance = float(centre_distance)
        pulley_a_diameter = float(pulley_a_diameter)
        pulley_b_diameter = float(pulley_b_diameter)
        name = str(name)
        method_result = self.wrapped.NewBeltCreationOptions(centre_distance if centre_distance else 0.0, pulley_a_diameter if pulley_a_diameter else 0.0, pulley_b_diameter if pulley_b_diameter else 0.0, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def new_planet_carrier_creation_options(self, number_of_planets: Optional['int'] = 3, diameter: Optional['float'] = 0.05) -> '_2317.PlanetCarrierCreationOptions':
        ''' 'NewPlanetCarrierCreationOptions' is the original name of this method.

        Args:
            number_of_planets (int, optional)
            diameter (float, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.PlanetCarrierCreationOptions
        '''

        number_of_planets = int(number_of_planets)
        diameter = float(diameter)
        method_result = self.wrapped.NewPlanetCarrierCreationOptions(number_of_planets if number_of_planets else 0, diameter if diameter else 0.0)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def new_shaft_creation_options(self, length: Optional['float'] = 0.1, outer_diameter: Optional['float'] = 0.025, bore: Optional['float'] = 0.0, name: Optional['str'] = 'Shaft') -> '_2318.ShaftCreationOptions':
        ''' 'NewShaftCreationOptions' is the original name of this method.

        Args:
            length (float, optional)
            outer_diameter (float, optional)
            bore (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.ShaftCreationOptions
        '''

        length = float(length)
        outer_diameter = float(outer_diameter)
        bore = float(bore)
        name = str(name)
        method_result = self.wrapped.NewShaftCreationOptions(length if length else 0.0, outer_diameter if outer_diameter else 0.0, bore if bore else 0.0, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def new_cylindrical_gear_pair_creation_options(self) -> '_1095.CylindricalGearPairCreationOptions':
        ''' 'NewCylindricalGearPairCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions
        '''

        method_result = self.wrapped.NewCylindricalGearPairCreationOptions()
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def new_cylindrical_gear_linear_train_creation_options(self, number_of_gears: Optional['int'] = 3, name: Optional['str'] = 'Gear Train') -> '_2316.CylindricalGearLinearTrainCreationOptions':
        ''' 'NewCylindricalGearLinearTrainCreationOptions' is the original name of this method.

        Args:
            number_of_gears (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.CylindricalGearLinearTrainCreationOptions
        '''

        number_of_gears = int(number_of_gears)
        name = str(name)
        method_result = self.wrapped.NewCylindricalGearLinearTrainCreationOptions(number_of_gears if number_of_gears else 0, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def new_spiral_bevel_gear_set_creation_options(self) -> '_1098.SpiralBevelGearSetCreationOptions':
        ''' 'NewSpiralBevelGearSetCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.SpiralBevelGearSetCreationOptions
        '''

        method_result = self.wrapped.NewSpiralBevelGearSetCreationOptions()
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def new_hypoid_gear_set_creation_options(self) -> '_1097.HypoidGearSetCreationOptions':
        ''' 'NewHypoidGearSetCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.HypoidGearSetCreationOptions
        '''

        method_result = self.wrapped.NewHypoidGearSetCreationOptions()
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def new_cycloidal_assembly_creation_options(self, number_of_discs: Optional['int'] = 1, number_of_pins: Optional['int'] = 10, name: Optional['str'] = 'Cycloidal Assembly') -> '_2315.CycloidalAssemblyCreationOptions':
        ''' 'NewCycloidalAssemblyCreationOptions' is the original name of this method.

        Args:
            number_of_discs (int, optional)
            number_of_pins (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.CycloidalAssemblyCreationOptions
        '''

        number_of_discs = int(number_of_discs)
        number_of_pins = int(number_of_pins)
        name = str(name)
        method_result = self.wrapped.NewCycloidalAssemblyCreationOptions(number_of_discs if number_of_discs else 0, number_of_pins if number_of_pins else 0, name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def design_state_load_case_group_named(self, name: 'str') -> '_5391.DesignState':
        ''' 'DesignStateLoadCaseGroupNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        '''

        name = str(name)
        method_result = self.wrapped.DesignStateLoadCaseGroupNamed(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def time_series_load_case_group_named(self, name: 'str') -> '_5399.TimeSeriesLoadCaseGroup':
        ''' 'TimeSeriesLoadCaseGroupNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup
        '''

        name = str(name)
        method_result = self.wrapped.TimeSeriesLoadCaseGroupNamed(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def design_state_named(self, name: 'str') -> '_5391.DesignState':
        ''' 'DesignStateNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        '''

        name = str(name)
        method_result = self.wrapped.DesignStateNamed(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def duty_cycle_named(self, name: 'str') -> '_5392.DutyCycle':
        ''' 'DutyCycleNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle
        '''

        name = str(name)
        method_result = self.wrapped.DutyCycleNamed(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def __copy__(self) -> 'Design':
        ''' 'Copy' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        '''

        method_result = self.wrapped.Copy()
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def __deepcopy__(self, memo) -> 'Design':
        ''' 'Copy' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        '''

        method_result = self.wrapped.Copy()
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def save(self, file_name: 'str', save_results: 'bool') -> '_1567.Status':
        ''' 'Save' is the original name of this method.

        Args:
            file_name (str)
            save_results (bool)

        Returns:
            mastapy.utility.model_validation.Status
        '''

        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save.Overloads[_STRING, _BOOLEAN](file_name if file_name else '', save_results if save_results else False)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def save_with_progess(self, file_name: 'str', save_results: 'bool', progress: '_7278.TaskProgress') -> '_1567.Status':
        ''' 'Save' is the original name of this method.

        Args:
            file_name (str)
            save_results (bool)
            progress (mastapy.TaskProgress)

        Returns:
            mastapy.utility.model_validation.Status
        '''

        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save.Overloads[_STRING, _BOOLEAN, _TASK_PROGRESS](file_name if file_name else '', save_results if save_results else False, progress.wrapped if progress else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def remove_synchroniser_shift(self, shift: '_2720.SynchroniserShift'):
        ''' 'RemoveSynchroniserShift' is the original name of this method.

        Args:
            shift (mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift)
        '''

        self.wrapped.RemoveSynchroniserShift(shift.wrapped if shift else None)

    def add_synchroniser_shift(self, name: 'str') -> '_2720.SynchroniserShift':
        ''' 'AddSynchroniserShift' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift
        '''

        name = str(name)
        method_result = self.wrapped.AddSynchroniserShift.Overloads[_STRING](name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_synchroniser_shift_empty(self) -> '_2720.SynchroniserShift':
        ''' 'AddSynchroniserShift' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift
        '''

        method_result = self.wrapped.AddSynchroniserShift()
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_design_state(self, name: Optional['str'] = 'New Design State') -> '_5391.DesignState':
        ''' 'AddDesignState' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        '''

        name = str(name)
        method_result = self.wrapped.AddDesignState(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def add_duty_cycle(self, name: Optional['str'] = 'New Duty Cycle') -> '_5392.DutyCycle':
        ''' 'AddDutyCycle' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle
        '''

        name = str(name)
        method_result = self.wrapped.AddDutyCycle(name if name else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def dispose(self):
        ''' 'Dispose' is the original name of this method.'''

        self.wrapped.Dispose()

    def all_parts(self) -> 'List[_2212.Part]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Part]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2212.Part.TYPE](), constructor.new(_2212.Part))

    def all_parts_of_type_assembly(self) -> 'List[_2179.Assembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Assembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2179.Assembly.TYPE](), constructor.new(_2179.Assembly))

    def all_parts_of_type_abstract_assembly(self) -> 'List[_2180.AbstractAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2180.AbstractAssembly.TYPE](), constructor.new(_2180.AbstractAssembly))

    def all_parts_of_type_abstract_shaft(self) -> 'List[_2181.AbstractShaft]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaft]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2181.AbstractShaft.TYPE](), constructor.new(_2181.AbstractShaft))

    def all_parts_of_type_abstract_shaft_or_housing(self) -> 'List[_2182.AbstractShaftOrHousing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaftOrHousing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2182.AbstractShaftOrHousing.TYPE](), constructor.new(_2182.AbstractShaftOrHousing))

    def all_parts_of_type_bearing(self) -> 'List[_2185.Bearing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bearing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2185.Bearing.TYPE](), constructor.new(_2185.Bearing))

    def all_parts_of_type_bolt(self) -> 'List[_2187.Bolt]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bolt]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2187.Bolt.TYPE](), constructor.new(_2187.Bolt))

    def all_parts_of_type_bolted_joint(self) -> 'List[_2188.BoltedJoint]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.BoltedJoint]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2188.BoltedJoint.TYPE](), constructor.new(_2188.BoltedJoint))

    def all_parts_of_type_component(self) -> 'List[_2189.Component]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Component]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2189.Component.TYPE](), constructor.new(_2189.Component))

    def all_parts_of_type_connector(self) -> 'List[_2192.Connector]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Connector]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2192.Connector.TYPE](), constructor.new(_2192.Connector))

    def all_parts_of_type_datum(self) -> 'List[_2193.Datum]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Datum]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2193.Datum.TYPE](), constructor.new(_2193.Datum))

    def all_parts_of_type_external_cad_model(self) -> 'List[_2196.ExternalCADModel]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.ExternalCADModel]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2196.ExternalCADModel.TYPE](), constructor.new(_2196.ExternalCADModel))

    def all_parts_of_type_fe_part(self) -> 'List[_2197.FEPart]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FEPart]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2197.FEPart.TYPE](), constructor.new(_2197.FEPart))

    def all_parts_of_type_flexible_pin_assembly(self) -> 'List[_2198.FlexiblePinAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FlexiblePinAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2198.FlexiblePinAssembly.TYPE](), constructor.new(_2198.FlexiblePinAssembly))

    def all_parts_of_type_guide_dxf_model(self) -> 'List[_2199.GuideDxfModel]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.GuideDxfModel]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2199.GuideDxfModel.TYPE](), constructor.new(_2199.GuideDxfModel))

    def all_parts_of_type_mass_disc(self) -> 'List[_2206.MassDisc]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MassDisc]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2206.MassDisc.TYPE](), constructor.new(_2206.MassDisc))

    def all_parts_of_type_measurement_component(self) -> 'List[_2207.MeasurementComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MeasurementComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2207.MeasurementComponent.TYPE](), constructor.new(_2207.MeasurementComponent))

    def all_parts_of_type_mountable_component(self) -> 'List[_2208.MountableComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MountableComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2208.MountableComponent.TYPE](), constructor.new(_2208.MountableComponent))

    def all_parts_of_type_oil_seal(self) -> 'List[_2210.OilSeal]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.OilSeal]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2210.OilSeal.TYPE](), constructor.new(_2210.OilSeal))

    def all_parts_of_type_planet_carrier(self) -> 'List[_2213.PlanetCarrier]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PlanetCarrier]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2213.PlanetCarrier.TYPE](), constructor.new(_2213.PlanetCarrier))

    def all_parts_of_type_point_load(self) -> 'List[_2215.PointLoad]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PointLoad]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2215.PointLoad.TYPE](), constructor.new(_2215.PointLoad))

    def all_parts_of_type_power_load(self) -> 'List[_2216.PowerLoad]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PowerLoad]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2216.PowerLoad.TYPE](), constructor.new(_2216.PowerLoad))

    def all_parts_of_type_root_assembly(self) -> 'List[_2218.RootAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.RootAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2218.RootAssembly.TYPE](), constructor.new(_2218.RootAssembly))

    def all_parts_of_type_specialised_assembly(self) -> 'List[_2220.SpecialisedAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.SpecialisedAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2220.SpecialisedAssembly.TYPE](), constructor.new(_2220.SpecialisedAssembly))

    def all_parts_of_type_unbalanced_mass(self) -> 'List[_2221.UnbalancedMass]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.UnbalancedMass]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2221.UnbalancedMass.TYPE](), constructor.new(_2221.UnbalancedMass))

    def all_parts_of_type_virtual_component(self) -> 'List[_2223.VirtualComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.VirtualComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2223.VirtualComponent.TYPE](), constructor.new(_2223.VirtualComponent))

    def all_parts_of_type_shaft(self) -> 'List[_2226.Shaft]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.shaft_model.Shaft]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2226.Shaft.TYPE](), constructor.new(_2226.Shaft))

    def all_parts_of_type_agma_gleason_conical_gear(self) -> 'List[_2256.AGMAGleasonConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2256.AGMAGleasonConicalGear.TYPE](), constructor.new(_2256.AGMAGleasonConicalGear))

    def all_parts_of_type_agma_gleason_conical_gear_set(self) -> 'List[_2257.AGMAGleasonConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2257.AGMAGleasonConicalGearSet.TYPE](), constructor.new(_2257.AGMAGleasonConicalGearSet))

    def all_parts_of_type_bevel_differential_gear(self) -> 'List[_2258.BevelDifferentialGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2258.BevelDifferentialGear.TYPE](), constructor.new(_2258.BevelDifferentialGear))

    def all_parts_of_type_bevel_differential_gear_set(self) -> 'List[_2259.BevelDifferentialGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2259.BevelDifferentialGearSet.TYPE](), constructor.new(_2259.BevelDifferentialGearSet))

    def all_parts_of_type_bevel_differential_planet_gear(self) -> 'List[_2260.BevelDifferentialPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2260.BevelDifferentialPlanetGear.TYPE](), constructor.new(_2260.BevelDifferentialPlanetGear))

    def all_parts_of_type_bevel_differential_sun_gear(self) -> 'List[_2261.BevelDifferentialSunGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialSunGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2261.BevelDifferentialSunGear.TYPE](), constructor.new(_2261.BevelDifferentialSunGear))

    def all_parts_of_type_bevel_gear(self) -> 'List[_2262.BevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2262.BevelGear.TYPE](), constructor.new(_2262.BevelGear))

    def all_parts_of_type_bevel_gear_set(self) -> 'List[_2263.BevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2263.BevelGearSet.TYPE](), constructor.new(_2263.BevelGearSet))

    def all_parts_of_type_concept_gear(self) -> 'List[_2264.ConceptGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2264.ConceptGear.TYPE](), constructor.new(_2264.ConceptGear))

    def all_parts_of_type_concept_gear_set(self) -> 'List[_2265.ConceptGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2265.ConceptGearSet.TYPE](), constructor.new(_2265.ConceptGearSet))

    def all_parts_of_type_conical_gear(self) -> 'List[_2266.ConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2266.ConicalGear.TYPE](), constructor.new(_2266.ConicalGear))

    def all_parts_of_type_conical_gear_set(self) -> 'List[_2267.ConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2267.ConicalGearSet.TYPE](), constructor.new(_2267.ConicalGearSet))

    def all_parts_of_type_cylindrical_gear(self) -> 'List[_2268.CylindricalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2268.CylindricalGear.TYPE](), constructor.new(_2268.CylindricalGear))

    def all_parts_of_type_cylindrical_gear_set(self) -> 'List[_2269.CylindricalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2269.CylindricalGearSet.TYPE](), constructor.new(_2269.CylindricalGearSet))

    def all_parts_of_type_cylindrical_planet_gear(self) -> 'List[_2270.CylindricalPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2270.CylindricalPlanetGear.TYPE](), constructor.new(_2270.CylindricalPlanetGear))

    def all_parts_of_type_face_gear(self) -> 'List[_2271.FaceGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2271.FaceGear.TYPE](), constructor.new(_2271.FaceGear))

    def all_parts_of_type_face_gear_set(self) -> 'List[_2272.FaceGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2272.FaceGearSet.TYPE](), constructor.new(_2272.FaceGearSet))

    def all_parts_of_type_gear(self) -> 'List[_2273.Gear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.Gear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2273.Gear.TYPE](), constructor.new(_2273.Gear))

    def all_parts_of_type_gear_set(self) -> 'List[_2275.GearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.GearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2275.GearSet.TYPE](), constructor.new(_2275.GearSet))

    def all_parts_of_type_hypoid_gear(self) -> 'List[_2277.HypoidGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2277.HypoidGear.TYPE](), constructor.new(_2277.HypoidGear))

    def all_parts_of_type_hypoid_gear_set(self) -> 'List[_2278.HypoidGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2278.HypoidGearSet.TYPE](), constructor.new(_2278.HypoidGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> 'List[_2279.KlingelnbergCycloPalloidConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2279.KlingelnbergCycloPalloidConicalGear.TYPE](), constructor.new(_2279.KlingelnbergCycloPalloidConicalGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> 'List[_2280.KlingelnbergCycloPalloidConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2280.KlingelnbergCycloPalloidConicalGearSet.TYPE](), constructor.new(_2280.KlingelnbergCycloPalloidConicalGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> 'List[_2281.KlingelnbergCycloPalloidHypoidGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2281.KlingelnbergCycloPalloidHypoidGear.TYPE](), constructor.new(_2281.KlingelnbergCycloPalloidHypoidGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> 'List[_2282.KlingelnbergCycloPalloidHypoidGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2282.KlingelnbergCycloPalloidHypoidGearSet.TYPE](), constructor.new(_2282.KlingelnbergCycloPalloidHypoidGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> 'List[_2283.KlingelnbergCycloPalloidSpiralBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2283.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](), constructor.new(_2283.KlingelnbergCycloPalloidSpiralBevelGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> 'List[_2284.KlingelnbergCycloPalloidSpiralBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2284.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](), constructor.new(_2284.KlingelnbergCycloPalloidSpiralBevelGearSet))

    def all_parts_of_type_planetary_gear_set(self) -> 'List[_2285.PlanetaryGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.PlanetaryGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2285.PlanetaryGearSet.TYPE](), constructor.new(_2285.PlanetaryGearSet))

    def all_parts_of_type_spiral_bevel_gear(self) -> 'List[_2286.SpiralBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2286.SpiralBevelGear.TYPE](), constructor.new(_2286.SpiralBevelGear))

    def all_parts_of_type_spiral_bevel_gear_set(self) -> 'List[_2287.SpiralBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2287.SpiralBevelGearSet.TYPE](), constructor.new(_2287.SpiralBevelGearSet))

    def all_parts_of_type_straight_bevel_diff_gear(self) -> 'List[_2288.StraightBevelDiffGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2288.StraightBevelDiffGear.TYPE](), constructor.new(_2288.StraightBevelDiffGear))

    def all_parts_of_type_straight_bevel_diff_gear_set(self) -> 'List[_2289.StraightBevelDiffGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2289.StraightBevelDiffGearSet.TYPE](), constructor.new(_2289.StraightBevelDiffGearSet))

    def all_parts_of_type_straight_bevel_gear(self) -> 'List[_2290.StraightBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2290.StraightBevelGear.TYPE](), constructor.new(_2290.StraightBevelGear))

    def all_parts_of_type_straight_bevel_gear_set(self) -> 'List[_2291.StraightBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2291.StraightBevelGearSet.TYPE](), constructor.new(_2291.StraightBevelGearSet))

    def all_parts_of_type_straight_bevel_planet_gear(self) -> 'List[_2292.StraightBevelPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2292.StraightBevelPlanetGear.TYPE](), constructor.new(_2292.StraightBevelPlanetGear))

    def all_parts_of_type_straight_bevel_sun_gear(self) -> 'List[_2293.StraightBevelSunGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelSunGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2293.StraightBevelSunGear.TYPE](), constructor.new(_2293.StraightBevelSunGear))

    def all_parts_of_type_worm_gear(self) -> 'List[_2294.WormGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2294.WormGear.TYPE](), constructor.new(_2294.WormGear))

    def all_parts_of_type_worm_gear_set(self) -> 'List[_2295.WormGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2295.WormGearSet.TYPE](), constructor.new(_2295.WormGearSet))

    def all_parts_of_type_zerol_bevel_gear(self) -> 'List[_2296.ZerolBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2296.ZerolBevelGear.TYPE](), constructor.new(_2296.ZerolBevelGear))

    def all_parts_of_type_zerol_bevel_gear_set(self) -> 'List[_2297.ZerolBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2297.ZerolBevelGearSet.TYPE](), constructor.new(_2297.ZerolBevelGearSet))

    def all_parts_of_type_cycloidal_assembly(self) -> 'List[_2311.CycloidalAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2311.CycloidalAssembly.TYPE](), constructor.new(_2311.CycloidalAssembly))

    def all_parts_of_type_cycloidal_disc(self) -> 'List[_2312.CycloidalDisc]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalDisc]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2312.CycloidalDisc.TYPE](), constructor.new(_2312.CycloidalDisc))

    def all_parts_of_type_ring_pins(self) -> 'List[_2313.RingPins]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.RingPins]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2313.RingPins.TYPE](), constructor.new(_2313.RingPins))

    def all_parts_of_type_belt_drive(self) -> 'List[_2319.BeltDrive]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.BeltDrive]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2319.BeltDrive.TYPE](), constructor.new(_2319.BeltDrive))

    def all_parts_of_type_clutch(self) -> 'List[_2321.Clutch]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Clutch]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2321.Clutch.TYPE](), constructor.new(_2321.Clutch))

    def all_parts_of_type_clutch_half(self) -> 'List[_2322.ClutchHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ClutchHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2322.ClutchHalf.TYPE](), constructor.new(_2322.ClutchHalf))

    def all_parts_of_type_concept_coupling(self) -> 'List[_2324.ConceptCoupling]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCoupling]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2324.ConceptCoupling.TYPE](), constructor.new(_2324.ConceptCoupling))

    def all_parts_of_type_concept_coupling_half(self) -> 'List[_2325.ConceptCouplingHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCouplingHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2325.ConceptCouplingHalf.TYPE](), constructor.new(_2325.ConceptCouplingHalf))

    def all_parts_of_type_coupling(self) -> 'List[_2326.Coupling]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Coupling]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2326.Coupling.TYPE](), constructor.new(_2326.Coupling))

    def all_parts_of_type_coupling_half(self) -> 'List[_2327.CouplingHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CouplingHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2327.CouplingHalf.TYPE](), constructor.new(_2327.CouplingHalf))

    def all_parts_of_type_cvt(self) -> 'List[_2329.CVT]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVT]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2329.CVT.TYPE](), constructor.new(_2329.CVT))

    def all_parts_of_type_cvt_pulley(self) -> 'List[_2330.CVTPulley]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVTPulley]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2330.CVTPulley.TYPE](), constructor.new(_2330.CVTPulley))

    def all_parts_of_type_part_to_part_shear_coupling(self) -> 'List[_2331.PartToPartShearCoupling]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCoupling]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2331.PartToPartShearCoupling.TYPE](), constructor.new(_2331.PartToPartShearCoupling))

    def all_parts_of_type_part_to_part_shear_coupling_half(self) -> 'List[_2332.PartToPartShearCouplingHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2332.PartToPartShearCouplingHalf.TYPE](), constructor.new(_2332.PartToPartShearCouplingHalf))

    def all_parts_of_type_pulley(self) -> 'List[_2333.Pulley]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Pulley]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2333.Pulley.TYPE](), constructor.new(_2333.Pulley))

    def all_parts_of_type_rolling_ring(self) -> 'List[_2339.RollingRing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2339.RollingRing.TYPE](), constructor.new(_2339.RollingRing))

    def all_parts_of_type_rolling_ring_assembly(self) -> 'List[_2340.RollingRingAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRingAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2340.RollingRingAssembly.TYPE](), constructor.new(_2340.RollingRingAssembly))

    def all_parts_of_type_shaft_hub_connection(self) -> 'List[_2341.ShaftHubConnection]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ShaftHubConnection]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2341.ShaftHubConnection.TYPE](), constructor.new(_2341.ShaftHubConnection))

    def all_parts_of_type_spring_damper(self) -> 'List[_2343.SpringDamper]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamper]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2343.SpringDamper.TYPE](), constructor.new(_2343.SpringDamper))

    def all_parts_of_type_spring_damper_half(self) -> 'List[_2344.SpringDamperHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamperHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2344.SpringDamperHalf.TYPE](), constructor.new(_2344.SpringDamperHalf))

    def all_parts_of_type_synchroniser(self) -> 'List[_2345.Synchroniser]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Synchroniser]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2345.Synchroniser.TYPE](), constructor.new(_2345.Synchroniser))

    def all_parts_of_type_synchroniser_half(self) -> 'List[_2347.SynchroniserHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2347.SynchroniserHalf.TYPE](), constructor.new(_2347.SynchroniserHalf))

    def all_parts_of_type_synchroniser_part(self) -> 'List[_2348.SynchroniserPart]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserPart]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2348.SynchroniserPart.TYPE](), constructor.new(_2348.SynchroniserPart))

    def all_parts_of_type_synchroniser_sleeve(self) -> 'List[_2349.SynchroniserSleeve]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserSleeve]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2349.SynchroniserSleeve.TYPE](), constructor.new(_2349.SynchroniserSleeve))

    def all_parts_of_type_torque_converter(self) -> 'List[_2350.TorqueConverter]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverter]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2350.TorqueConverter.TYPE](), constructor.new(_2350.TorqueConverter))

    def all_parts_of_type_torque_converter_pump(self) -> 'List[_2351.TorqueConverterPump]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterPump]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2351.TorqueConverterPump.TYPE](), constructor.new(_2351.TorqueConverterPump))

    def all_parts_of_type_torque_converter_turbine(self) -> 'List[_2353.TorqueConverterTurbine]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterTurbine]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2353.TorqueConverterTurbine.TYPE](), constructor.new(_2353.TorqueConverterTurbine))

    @staticmethod
    def load(file_path: 'str', load_full_fe_option: Optional['_1381.ExternalFullFEFileOption'] = _1381.ExternalFullFEFileOption.MESH_AND_EXPANSION_VECTORS) -> 'Design':
        ''' 'Load' is the original name of this method.

        Args:
            file_path (str)
            load_full_fe_option (mastapy.utility.ExternalFullFEFileOption, optional)

        Returns:
            mastapy.system_model.Design
        '''

        file_path = str(file_path)
        file_path = path.abspath(file_path)
        load_full_fe_option = conversion.mp_to_pn_enum(load_full_fe_option)
        method_result = Design.TYPE.Load(file_path if file_path else '', load_full_fe_option)
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    @staticmethod
    def load_example(example_string: 'str') -> 'Design':
        ''' 'LoadExample' is the original name of this method.

        Args:
            example_string (str)

        Returns:
            mastapy.system_model.Design
        '''

        example_string = str(example_string)
        method_result = Design.TYPE.LoadExample(example_string if example_string else '')
        return constructor.new_override(method_result.__class__)(method_result) if method_result is not None else None

    def compare_for_test_only(self, design: 'Design', sb: 'str') -> 'bool':
        ''' 'CompareForTestOnly' is the original name of this method.

        Args:
            design (mastapy.system_model.Design)
            sb (str)

        Returns:
            bool
        '''

        sb = str(sb)
        method_result = self.wrapped.CompareForTestOnly(design.wrapped if design else None, sb if sb else '')
        return method_result

    def change_gears_to_clones_where_suitable(self):
        ''' 'ChangeGearsToClonesWhereSuitable' is the original name of this method.'''

        self.wrapped.ChangeGearsToClonesWhereSuitable()

    def clear_undo_redo_stacks(self):
        ''' 'ClearUndoRedoStacks' is the original name of this method.'''

        self.wrapped.ClearUndoRedoStacks()

    def delete_all_inactive_gear_set_designs(self):
        ''' 'DeleteAllInactiveGearSetDesigns' is the original name of this method.'''

        self.wrapped.DeleteAllInactiveGearSetDesigns()

    def add_gear_set_configuration(self):
        ''' 'AddGearSetConfiguration' is the original name of this method.'''

        self.wrapped.AddGearSetConfiguration()

    def delete_multiple_gear_set_configurations(self):
        ''' 'DeleteMultipleGearSetConfigurations' is the original name of this method.'''

        self.wrapped.DeleteMultipleGearSetConfigurations()

    def add_shaft_detail_configuration(self):
        ''' 'AddShaftDetailConfiguration' is the original name of this method.'''

        self.wrapped.AddShaftDetailConfiguration()

    def delete_multiple_shaft_detail_configurations(self):
        ''' 'DeleteMultipleShaftDetailConfigurations' is the original name of this method.'''

        self.wrapped.DeleteMultipleShaftDetailConfigurations()

    def add_bearing_detail_configuration_all_bearings(self):
        ''' 'AddBearingDetailConfigurationAllBearings' is the original name of this method.'''

        self.wrapped.AddBearingDetailConfigurationAllBearings()

    def add_bearing_detail_configuration_rolling_bearings(self):
        ''' 'AddBearingDetailConfigurationRollingBearings' is the original name of this method.'''

        self.wrapped.AddBearingDetailConfigurationRollingBearings()

    def delete_multiple_bearing_detail_configurations(self):
        ''' 'DeleteMultipleBearingDetailConfigurations' is the original name of this method.'''

        self.wrapped.DeleteMultipleBearingDetailConfigurations()

    def add_fe_substructure_configuration(self):
        ''' 'AddFESubstructureConfiguration' is the original name of this method.'''

        self.wrapped.AddFESubstructureConfiguration()

    def delete_multiple_fe_substructure_configurations(self):
        ''' 'DeleteMultipleFESubstructureConfigurations' is the original name of this method.'''

        self.wrapped.DeleteMultipleFESubstructureConfigurations()

    def delete_all_gear_set_configurations_that_have_errors_or_warnings(self):
        ''' 'DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings' is the original name of this method.'''

        self.wrapped.DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings()

    def delete_all_gear_sets_designs_that_are_not_used_in_configurations(self):
        ''' 'DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations' is the original name of this method.'''

        self.wrapped.DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations()

    def compare_results_to_previous_masta_version(self):
        ''' 'CompareResultsToPreviousMASTAVersion' is the original name of this method.'''

        self.wrapped.CompareResultsToPreviousMASTAVersion()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.dispose()
