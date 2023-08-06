'''_4313.py

AssemblyModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2179, _2218
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6536, _6669
from mastapy.system_model.analyses_and_results.system_deflections import _2435, _2538
from mastapy.system_model.analyses_and_results.modal_analyses import (
    _4363, _4314, _4316, _4319,
    _4326, _4325, _4329, _4334,
    _4337, _4348, _4350, _4352,
    _4356, _4362, _4364, _4372,
    _4379, _4382, _4383, _4384,
    _4389, _4394, _4397, _4398,
    _4399, _4407, _4401, _4403,
    _4408, _4414, _4417, _4420,
    _4423, _4427, _4431, _4434,
    _4443, _4446, _4306
)
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4447
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'AssemblyModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyModalAnalysis',)


class AssemblyModalAnalysis(_4306.AbstractAssemblyModalAnalysis):
    '''AssemblyModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2179.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.Assembly.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6536.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6536.AssemblyLoadCase.TYPE not in self.wrapped.AssemblyLoadCase.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to AssemblyLoadCase. Expected: {}.'.format(self.wrapped.AssemblyLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyLoadCase.__class__)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2435.AssemblySystemDeflection':
        '''AssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2435.AssemblySystemDeflection.TYPE not in self.wrapped.SystemDeflectionResults.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_results to AssemblySystemDeflection. Expected: {}.'.format(self.wrapped.SystemDeflectionResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SystemDeflectionResults.__class__)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def full_fe_meshes_for_calculating_modes(self) -> 'List[_4363.FEPartModalAnalysis]':
        '''List[FEPartModalAnalysis]: 'FullFEMeshesForCalculatingModes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FullFEMeshesForCalculatingModes, constructor.new(_4363.FEPartModalAnalysis))
        return value

    @property
    def calculate_full_fe_results_by_mode(self) -> 'List[_4447.CalculateFullFEResultsForMode]':
        '''List[CalculateFullFEResultsForMode]: 'CalculateFullFEResultsByMode' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CalculateFullFEResultsByMode, constructor.new(_4447.CalculateFullFEResultsForMode))
        return value

    @property
    def bearings(self) -> 'List[_4314.BearingModalAnalysis]':
        '''List[BearingModalAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4314.BearingModalAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_4316.BeltDriveModalAnalysis]':
        '''List[BeltDriveModalAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4316.BeltDriveModalAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4319.BevelDifferentialGearSetModalAnalysis]':
        '''List[BevelDifferentialGearSetModalAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4319.BevelDifferentialGearSetModalAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_4326.BoltModalAnalysis]':
        '''List[BoltModalAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4326.BoltModalAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_4325.BoltedJointModalAnalysis]':
        '''List[BoltedJointModalAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4325.BoltedJointModalAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_4329.ClutchModalAnalysis]':
        '''List[ClutchModalAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4329.ClutchModalAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_4334.ConceptCouplingModalAnalysis]':
        '''List[ConceptCouplingModalAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4334.ConceptCouplingModalAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4337.ConceptGearSetModalAnalysis]':
        '''List[ConceptGearSetModalAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4337.ConceptGearSetModalAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_4348.CVTModalAnalysis]':
        '''List[CVTModalAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4348.CVTModalAnalysis))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_4350.CycloidalAssemblyModalAnalysis]':
        '''List[CycloidalAssemblyModalAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_4350.CycloidalAssemblyModalAnalysis))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_4352.CycloidalDiscModalAnalysis]':
        '''List[CycloidalDiscModalAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_4352.CycloidalDiscModalAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4356.CylindricalGearSetModalAnalysis]':
        '''List[CylindricalGearSetModalAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4356.CylindricalGearSetModalAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4362.FaceGearSetModalAnalysis]':
        '''List[FaceGearSetModalAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4362.FaceGearSetModalAnalysis))
        return value

    @property
    def fe_parts(self) -> 'List[_4363.FEPartModalAnalysis]':
        '''List[FEPartModalAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_4363.FEPartModalAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4364.FlexiblePinAssemblyModalAnalysis]':
        '''List[FlexiblePinAssemblyModalAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4364.FlexiblePinAssemblyModalAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4372.HypoidGearSetModalAnalysis]':
        '''List[HypoidGearSetModalAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4372.HypoidGearSetModalAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4379.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetModalAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4379.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4382.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4382.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_4383.MassDiscModalAnalysis]':
        '''List[MassDiscModalAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4383.MassDiscModalAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_4384.MeasurementComponentModalAnalysis]':
        '''List[MeasurementComponentModalAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4384.MeasurementComponentModalAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_4389.OilSealModalAnalysis]':
        '''List[OilSealModalAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4389.OilSealModalAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4394.PartToPartShearCouplingModalAnalysis]':
        '''List[PartToPartShearCouplingModalAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_4394.PartToPartShearCouplingModalAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_4397.PlanetCarrierModalAnalysis]':
        '''List[PlanetCarrierModalAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4397.PlanetCarrierModalAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_4398.PointLoadModalAnalysis]':
        '''List[PointLoadModalAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4398.PointLoadModalAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_4399.PowerLoadModalAnalysis]':
        '''List[PowerLoadModalAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4399.PowerLoadModalAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4407.ShaftHubConnectionModalAnalysis]':
        '''List[ShaftHubConnectionModalAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4407.ShaftHubConnectionModalAnalysis))
        return value

    @property
    def ring_pins(self) -> 'List[_4401.RingPinsModalAnalysis]':
        '''List[RingPinsModalAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_4401.RingPinsModalAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4403.RollingRingAssemblyModalAnalysis]':
        '''List[RollingRingAssemblyModalAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4403.RollingRingAssemblyModalAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_4408.ShaftModalAnalysis]':
        '''List[ShaftModalAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4408.ShaftModalAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4414.SpiralBevelGearSetModalAnalysis]':
        '''List[SpiralBevelGearSetModalAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4414.SpiralBevelGearSetModalAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_4417.SpringDamperModalAnalysis]':
        '''List[SpringDamperModalAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4417.SpringDamperModalAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4420.StraightBevelDiffGearSetModalAnalysis]':
        '''List[StraightBevelDiffGearSetModalAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4420.StraightBevelDiffGearSetModalAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4423.StraightBevelGearSetModalAnalysis]':
        '''List[StraightBevelGearSetModalAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4423.StraightBevelGearSetModalAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_4427.SynchroniserModalAnalysis]':
        '''List[SynchroniserModalAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4427.SynchroniserModalAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_4431.TorqueConverterModalAnalysis]':
        '''List[TorqueConverterModalAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4431.TorqueConverterModalAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4434.UnbalancedMassModalAnalysis]':
        '''List[UnbalancedMassModalAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4434.UnbalancedMassModalAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4443.WormGearSetModalAnalysis]':
        '''List[WormGearSetModalAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4443.WormGearSetModalAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4446.ZerolBevelGearSetModalAnalysis]':
        '''List[ZerolBevelGearSetModalAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4446.ZerolBevelGearSetModalAnalysis))
        return value

    def calculate_all_selected_strain_and_kinetic_energies(self):
        ''' 'CalculateAllSelectedStrainAndKineticEnergies' is the original name of this method.'''

        self.wrapped.CalculateAllSelectedStrainAndKineticEnergies()

    def calculate_all_strain_and_kinetic_energies(self):
        ''' 'CalculateAllStrainAndKineticEnergies' is the original name of this method.'''

        self.wrapped.CalculateAllStrainAndKineticEnergies()
