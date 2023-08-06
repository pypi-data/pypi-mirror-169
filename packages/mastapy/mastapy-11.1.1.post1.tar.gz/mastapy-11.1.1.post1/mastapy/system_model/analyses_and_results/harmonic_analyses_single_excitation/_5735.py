'''_5735.py

AssemblyHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model import _2179, _2218
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6536, _6669
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _5736, _5738, _5741, _5748,
    _5747, _5751, _5756, _5759,
    _5769, _5771, _5773, _5777,
    _5783, _5784, _5785, _5793,
    _5800, _5803, _5804, _5805,
    _5807, _5811, _5814, _5815,
    _5816, _5825, _5818, _5820,
    _5824, _5830, _5833, _5836,
    _5839, _5843, _5847, _5850,
    _5854, _5857, _5728
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'AssemblyHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyHarmonicAnalysisOfSingleExcitation',)


class AssemblyHarmonicAnalysisOfSingleExcitation(_5728.AbstractAssemblyHarmonicAnalysisOfSingleExcitation):
    '''AssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyHarmonicAnalysisOfSingleExcitation.TYPE'):
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
    def bearings(self) -> 'List[_5736.BearingHarmonicAnalysisOfSingleExcitation]':
        '''List[BearingHarmonicAnalysisOfSingleExcitation]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5736.BearingHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def belt_drives(self) -> 'List[_5738.BeltDriveHarmonicAnalysisOfSingleExcitation]':
        '''List[BeltDriveHarmonicAnalysisOfSingleExcitation]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5738.BeltDriveHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5741.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5741.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def bolts(self) -> 'List[_5748.BoltHarmonicAnalysisOfSingleExcitation]':
        '''List[BoltHarmonicAnalysisOfSingleExcitation]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5748.BoltHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def bolted_joints(self) -> 'List[_5747.BoltedJointHarmonicAnalysisOfSingleExcitation]':
        '''List[BoltedJointHarmonicAnalysisOfSingleExcitation]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5747.BoltedJointHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def clutches(self) -> 'List[_5751.ClutchHarmonicAnalysisOfSingleExcitation]':
        '''List[ClutchHarmonicAnalysisOfSingleExcitation]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5751.ClutchHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def concept_couplings(self) -> 'List[_5756.ConceptCouplingHarmonicAnalysisOfSingleExcitation]':
        '''List[ConceptCouplingHarmonicAnalysisOfSingleExcitation]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5756.ConceptCouplingHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5759.ConceptGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[ConceptGearSetHarmonicAnalysisOfSingleExcitation]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5759.ConceptGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def cv_ts(self) -> 'List[_5769.CVTHarmonicAnalysisOfSingleExcitation]':
        '''List[CVTHarmonicAnalysisOfSingleExcitation]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5769.CVTHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_5771.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation]':
        '''List[CycloidalAssemblyHarmonicAnalysisOfSingleExcitation]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_5771.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_5773.CycloidalDiscHarmonicAnalysisOfSingleExcitation]':
        '''List[CycloidalDiscHarmonicAnalysisOfSingleExcitation]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_5773.CycloidalDiscHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5777.CylindricalGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[CylindricalGearSetHarmonicAnalysisOfSingleExcitation]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5777.CylindricalGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5783.FaceGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[FaceGearSetHarmonicAnalysisOfSingleExcitation]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5783.FaceGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def fe_parts(self) -> 'List[_5784.FEPartHarmonicAnalysisOfSingleExcitation]':
        '''List[FEPartHarmonicAnalysisOfSingleExcitation]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_5784.FEPartHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5785.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation]':
        '''List[FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5785.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5793.HypoidGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[HypoidGearSetHarmonicAnalysisOfSingleExcitation]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5793.HypoidGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5800.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5800.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5803.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5803.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def mass_discs(self) -> 'List[_5804.MassDiscHarmonicAnalysisOfSingleExcitation]':
        '''List[MassDiscHarmonicAnalysisOfSingleExcitation]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5804.MassDiscHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def measurement_components(self) -> 'List[_5805.MeasurementComponentHarmonicAnalysisOfSingleExcitation]':
        '''List[MeasurementComponentHarmonicAnalysisOfSingleExcitation]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5805.MeasurementComponentHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def oil_seals(self) -> 'List[_5807.OilSealHarmonicAnalysisOfSingleExcitation]':
        '''List[OilSealHarmonicAnalysisOfSingleExcitation]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5807.OilSealHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5811.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation]':
        '''List[PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5811.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def planet_carriers(self) -> 'List[_5814.PlanetCarrierHarmonicAnalysisOfSingleExcitation]':
        '''List[PlanetCarrierHarmonicAnalysisOfSingleExcitation]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5814.PlanetCarrierHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def point_loads(self) -> 'List[_5815.PointLoadHarmonicAnalysisOfSingleExcitation]':
        '''List[PointLoadHarmonicAnalysisOfSingleExcitation]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5815.PointLoadHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def power_loads(self) -> 'List[_5816.PowerLoadHarmonicAnalysisOfSingleExcitation]':
        '''List[PowerLoadHarmonicAnalysisOfSingleExcitation]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5816.PowerLoadHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5825.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation]':
        '''List[ShaftHubConnectionHarmonicAnalysisOfSingleExcitation]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5825.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def ring_pins(self) -> 'List[_5818.RingPinsHarmonicAnalysisOfSingleExcitation]':
        '''List[RingPinsHarmonicAnalysisOfSingleExcitation]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_5818.RingPinsHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5820.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation]':
        '''List[RollingRingAssemblyHarmonicAnalysisOfSingleExcitation]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5820.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def shafts(self) -> 'List[_5824.ShaftHarmonicAnalysisOfSingleExcitation]':
        '''List[ShaftHarmonicAnalysisOfSingleExcitation]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5824.ShaftHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5830.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5830.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def spring_dampers(self) -> 'List[_5833.SpringDamperHarmonicAnalysisOfSingleExcitation]':
        '''List[SpringDamperHarmonicAnalysisOfSingleExcitation]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5833.SpringDamperHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5836.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5836.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5839.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[StraightBevelGearSetHarmonicAnalysisOfSingleExcitation]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5839.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def synchronisers(self) -> 'List[_5843.SynchroniserHarmonicAnalysisOfSingleExcitation]':
        '''List[SynchroniserHarmonicAnalysisOfSingleExcitation]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5843.SynchroniserHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def torque_converters(self) -> 'List[_5847.TorqueConverterHarmonicAnalysisOfSingleExcitation]':
        '''List[TorqueConverterHarmonicAnalysisOfSingleExcitation]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5847.TorqueConverterHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5850.UnbalancedMassHarmonicAnalysisOfSingleExcitation]':
        '''List[UnbalancedMassHarmonicAnalysisOfSingleExcitation]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5850.UnbalancedMassHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5854.WormGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[WormGearSetHarmonicAnalysisOfSingleExcitation]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5854.WormGearSetHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5857.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation]':
        '''List[ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5857.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation))
        return value
