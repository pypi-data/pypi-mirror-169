﻿'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1516 import ScriptingSetup
    from ._1517 import UserDefinedPropertyKey
    from ._1518 import UserSpecifiedData
