﻿'''_4630.py

AssemblyCompoundModalAnalysisAtASpeed
'''


from typing import List

from mastapy.system_model.part_model import _2113, _2152
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4501
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _4631, _4633, _4636, _4642,
    _4643, _4644, _4649, _4654,
    _4664, _4666, _4668, _4672,
    _4678, _4679, _4680, _4687,
    _4694, _4697, _4698, _4699,
    _4701, _4703, _4708, _4709,
    _4710, _4719, _4712, _4714,
    _4718, _4724, _4725, _4730,
    _4733, _4736, _4740, _4744,
    _4748, _4751, _4623
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'AssemblyCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysisAtASpeed',)


class AssemblyCompoundModalAnalysisAtASpeed(_4623.AbstractAssemblyCompoundModalAnalysisAtASpeed):
    '''AssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2113.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2113.Assembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2113.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2113.Assembly.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4501.AssemblyModalAnalysisAtASpeed]':
        '''List[AssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4501.AssemblyModalAnalysisAtASpeed))
        return value

    @property
    def bearings(self) -> 'List[_4631.BearingCompoundModalAnalysisAtASpeed]':
        '''List[BearingCompoundModalAnalysisAtASpeed]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4631.BearingCompoundModalAnalysisAtASpeed))
        return value

    @property
    def belt_drives(self) -> 'List[_4633.BeltDriveCompoundModalAnalysisAtASpeed]':
        '''List[BeltDriveCompoundModalAnalysisAtASpeed]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4633.BeltDriveCompoundModalAnalysisAtASpeed))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4636.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysisAtASpeed]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4636.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def bolts(self) -> 'List[_4642.BoltCompoundModalAnalysisAtASpeed]':
        '''List[BoltCompoundModalAnalysisAtASpeed]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4642.BoltCompoundModalAnalysisAtASpeed))
        return value

    @property
    def bolted_joints(self) -> 'List[_4643.BoltedJointCompoundModalAnalysisAtASpeed]':
        '''List[BoltedJointCompoundModalAnalysisAtASpeed]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4643.BoltedJointCompoundModalAnalysisAtASpeed))
        return value

    @property
    def clutches(self) -> 'List[_4644.ClutchCompoundModalAnalysisAtASpeed]':
        '''List[ClutchCompoundModalAnalysisAtASpeed]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4644.ClutchCompoundModalAnalysisAtASpeed))
        return value

    @property
    def concept_couplings(self) -> 'List[_4649.ConceptCouplingCompoundModalAnalysisAtASpeed]':
        '''List[ConceptCouplingCompoundModalAnalysisAtASpeed]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4649.ConceptCouplingCompoundModalAnalysisAtASpeed))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4654.ConceptGearSetCompoundModalAnalysisAtASpeed]':
        '''List[ConceptGearSetCompoundModalAnalysisAtASpeed]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4654.ConceptGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def cv_ts(self) -> 'List[_4664.CVTCompoundModalAnalysisAtASpeed]':
        '''List[CVTCompoundModalAnalysisAtASpeed]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4664.CVTCompoundModalAnalysisAtASpeed))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_4666.CycloidalAssemblyCompoundModalAnalysisAtASpeed]':
        '''List[CycloidalAssemblyCompoundModalAnalysisAtASpeed]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_4666.CycloidalAssemblyCompoundModalAnalysisAtASpeed))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_4668.CycloidalDiscCompoundModalAnalysisAtASpeed]':
        '''List[CycloidalDiscCompoundModalAnalysisAtASpeed]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_4668.CycloidalDiscCompoundModalAnalysisAtASpeed))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4672.CylindricalGearSetCompoundModalAnalysisAtASpeed]':
        '''List[CylindricalGearSetCompoundModalAnalysisAtASpeed]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4672.CylindricalGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4678.FaceGearSetCompoundModalAnalysisAtASpeed]':
        '''List[FaceGearSetCompoundModalAnalysisAtASpeed]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4678.FaceGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def fe_parts(self) -> 'List[_4679.FEPartCompoundModalAnalysisAtASpeed]':
        '''List[FEPartCompoundModalAnalysisAtASpeed]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_4679.FEPartCompoundModalAnalysisAtASpeed))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4680.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysisAtASpeed]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4680.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4687.HypoidGearSetCompoundModalAnalysisAtASpeed]':
        '''List[HypoidGearSetCompoundModalAnalysisAtASpeed]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4687.HypoidGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4694.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4694.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4697.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4697.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def mass_discs(self) -> 'List[_4698.MassDiscCompoundModalAnalysisAtASpeed]':
        '''List[MassDiscCompoundModalAnalysisAtASpeed]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4698.MassDiscCompoundModalAnalysisAtASpeed))
        return value

    @property
    def measurement_components(self) -> 'List[_4699.MeasurementComponentCompoundModalAnalysisAtASpeed]':
        '''List[MeasurementComponentCompoundModalAnalysisAtASpeed]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4699.MeasurementComponentCompoundModalAnalysisAtASpeed))
        return value

    @property
    def oil_seals(self) -> 'List[_4701.OilSealCompoundModalAnalysisAtASpeed]':
        '''List[OilSealCompoundModalAnalysisAtASpeed]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4701.OilSealCompoundModalAnalysisAtASpeed))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_4703.PartToPartShearCouplingCompoundModalAnalysisAtASpeed]':
        '''List[PartToPartShearCouplingCompoundModalAnalysisAtASpeed]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_4703.PartToPartShearCouplingCompoundModalAnalysisAtASpeed))
        return value

    @property
    def planet_carriers(self) -> 'List[_4708.PlanetCarrierCompoundModalAnalysisAtASpeed]':
        '''List[PlanetCarrierCompoundModalAnalysisAtASpeed]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4708.PlanetCarrierCompoundModalAnalysisAtASpeed))
        return value

    @property
    def point_loads(self) -> 'List[_4709.PointLoadCompoundModalAnalysisAtASpeed]':
        '''List[PointLoadCompoundModalAnalysisAtASpeed]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4709.PointLoadCompoundModalAnalysisAtASpeed))
        return value

    @property
    def power_loads(self) -> 'List[_4710.PowerLoadCompoundModalAnalysisAtASpeed]':
        '''List[PowerLoadCompoundModalAnalysisAtASpeed]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4710.PowerLoadCompoundModalAnalysisAtASpeed))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4719.ShaftHubConnectionCompoundModalAnalysisAtASpeed]':
        '''List[ShaftHubConnectionCompoundModalAnalysisAtASpeed]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4719.ShaftHubConnectionCompoundModalAnalysisAtASpeed))
        return value

    @property
    def ring_pins(self) -> 'List[_4712.RingPinsCompoundModalAnalysisAtASpeed]':
        '''List[RingPinsCompoundModalAnalysisAtASpeed]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_4712.RingPinsCompoundModalAnalysisAtASpeed))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4714.RollingRingAssemblyCompoundModalAnalysisAtASpeed]':
        '''List[RollingRingAssemblyCompoundModalAnalysisAtASpeed]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4714.RollingRingAssemblyCompoundModalAnalysisAtASpeed))
        return value

    @property
    def shafts(self) -> 'List[_4718.ShaftCompoundModalAnalysisAtASpeed]':
        '''List[ShaftCompoundModalAnalysisAtASpeed]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4718.ShaftCompoundModalAnalysisAtASpeed))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4724.SpiralBevelGearSetCompoundModalAnalysisAtASpeed]':
        '''List[SpiralBevelGearSetCompoundModalAnalysisAtASpeed]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4724.SpiralBevelGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def spring_dampers(self) -> 'List[_4725.SpringDamperCompoundModalAnalysisAtASpeed]':
        '''List[SpringDamperCompoundModalAnalysisAtASpeed]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4725.SpringDamperCompoundModalAnalysisAtASpeed))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4730.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4730.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4733.StraightBevelGearSetCompoundModalAnalysisAtASpeed]':
        '''List[StraightBevelGearSetCompoundModalAnalysisAtASpeed]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4733.StraightBevelGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def synchronisers(self) -> 'List[_4736.SynchroniserCompoundModalAnalysisAtASpeed]':
        '''List[SynchroniserCompoundModalAnalysisAtASpeed]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4736.SynchroniserCompoundModalAnalysisAtASpeed))
        return value

    @property
    def torque_converters(self) -> 'List[_4740.TorqueConverterCompoundModalAnalysisAtASpeed]':
        '''List[TorqueConverterCompoundModalAnalysisAtASpeed]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4740.TorqueConverterCompoundModalAnalysisAtASpeed))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4744.UnbalancedMassCompoundModalAnalysisAtASpeed]':
        '''List[UnbalancedMassCompoundModalAnalysisAtASpeed]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4744.UnbalancedMassCompoundModalAnalysisAtASpeed))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4748.WormGearSetCompoundModalAnalysisAtASpeed]':
        '''List[WormGearSetCompoundModalAnalysisAtASpeed]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4748.WormGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4751.ZerolBevelGearSetCompoundModalAnalysisAtASpeed]':
        '''List[ZerolBevelGearSetCompoundModalAnalysisAtASpeed]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4751.ZerolBevelGearSetCompoundModalAnalysisAtASpeed))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4501.AssemblyModalAnalysisAtASpeed]':
        '''List[AssemblyModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4501.AssemblyModalAnalysisAtASpeed))
        return value
