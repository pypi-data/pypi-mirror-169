'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._919 import StraightBevelGearDesign
    from ._920 import StraightBevelGearMeshDesign
    from ._921 import StraightBevelGearSetDesign
    from ._922 import StraightBevelMeshedGearDesign
