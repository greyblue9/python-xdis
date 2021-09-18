#!/usr/bin/python3

import sys
if not sys.modules.__contains__('xdis.opcodes'):
  import _frozen_importlib, importlib
  mspec = _frozen_importlib.ModuleSpec("xdis.opcodes", next(iter(filter(
    lambda x: x.__name__ == 'PathFinder', sys.meta_path)))())
  m = importlib.util.module_from_spec(mspec)
  sys.modules['xdis.opcodes'] = m
else:
  m = sys.modules['xdis.opcodes']
import xdis.opcodes

from . import base
m.__dict__["base"] = base
sys.modules["xdis.opcodes.base"] = base
import xdis.opcodes.base
setattr(m, "base", base)

from . import opcode_10
m.__dict__["opcode_10"] = opcode_10
sys.modules["xdis.opcodes.opcode_10"] = opcode_10
import xdis.opcodes.opcode_10
setattr(m, "opcode_10", opcode_10)

from . import opcode_11
m.__dict__["opcode_11"] = opcode_11
sys.modules["xdis.opcodes.opcode_11"] = opcode_11
import xdis.opcodes.opcode_11
setattr(m, "opcode_11", opcode_11)

from . import opcode_13
m.__dict__["opcode_13"] = opcode_13
sys.modules["xdis.opcodes.opcode_13"] = opcode_13
import xdis.opcodes.opcode_13
setattr(m, "opcode_13", opcode_13)

from . import opcode_14
m.__dict__["opcode_14"] = opcode_14
sys.modules["xdis.opcodes.opcode_14"] = opcode_14
import xdis.opcodes.opcode_14
setattr(m, "opcode_14", opcode_14)

from . import opcode_15
m.__dict__["opcode_15"] = opcode_15
sys.modules["xdis.opcodes.opcode_15"] = opcode_15
import xdis.opcodes.opcode_15
setattr(m, "opcode_15", opcode_15)

from . import opcode_16
m.__dict__["opcode_16"] = opcode_16
sys.modules["xdis.opcodes.opcode_16"] = opcode_16
import xdis.opcodes.opcode_16
setattr(m, "opcode_16", opcode_16)

from . import opcode_20
m.__dict__["opcode_20"] = opcode_20
sys.modules["xdis.opcodes.opcode_20"] = opcode_20
import xdis.opcodes.opcode_20
setattr(m, "opcode_20", opcode_20)

from . import opcode_21
m.__dict__["opcode_21"] = opcode_21
sys.modules["xdis.opcodes.opcode_21"] = opcode_21
import xdis.opcodes.opcode_21
setattr(m, "opcode_21", opcode_21)

from . import opcode_22
m.__dict__["opcode_22"] = opcode_22
sys.modules["xdis.opcodes.opcode_22"] = opcode_22
import xdis.opcodes.opcode_22
setattr(m, "opcode_22", opcode_22)

from . import opcode_23
m.__dict__["opcode_23"] = opcode_23
sys.modules["xdis.opcodes.opcode_23"] = opcode_23
import xdis.opcodes.opcode_23
setattr(m, "opcode_23", opcode_23)

from . import opcode_24
m.__dict__["opcode_24"] = opcode_24
sys.modules["xdis.opcodes.opcode_24"] = opcode_24
import xdis.opcodes.opcode_24
setattr(m, "opcode_24", opcode_24)

from . import opcode_25
m.__dict__["opcode_25"] = opcode_25
sys.modules["xdis.opcodes.opcode_25"] = opcode_25
import xdis.opcodes.opcode_25
setattr(m, "opcode_25", opcode_25)

from . import opcode_26
m.__dict__["opcode_26"] = opcode_26
sys.modules["xdis.opcodes.opcode_26"] = opcode_26
import xdis.opcodes.opcode_26
setattr(m, "opcode_26", opcode_26)

from . import opcode_26pypy
m.__dict__["opcode_26pypy"] = opcode_26pypy
sys.modules["xdis.opcodes.opcode_26pypy"] = opcode_26pypy
import xdis.opcodes.opcode_26pypy
setattr(m, "opcode_26pypy", opcode_26pypy)

from . import opcode_27
m.__dict__["opcode_27"] = opcode_27
sys.modules["xdis.opcodes.opcode_27"] = opcode_27
import xdis.opcodes.opcode_27
setattr(m, "opcode_27", opcode_27)

from . import opcode_27pypy
m.__dict__["opcode_27pypy"] = opcode_27pypy
sys.modules["xdis.opcodes.opcode_27pypy"] = opcode_27pypy
import xdis.opcodes.opcode_27pypy
setattr(m, "opcode_27pypy", opcode_27pypy)

from . import opcode_2x
m.__dict__["opcode_2x"] = opcode_2x
sys.modules["xdis.opcodes.opcode_2x"] = opcode_2x
import xdis.opcodes.opcode_2x
setattr(m, "opcode_2x", opcode_2x)

from . import opcode_30
m.__dict__["opcode_30"] = opcode_30
sys.modules["xdis.opcodes.opcode_30"] = opcode_30
import xdis.opcodes.opcode_30
setattr(m, "opcode_30", opcode_30)

from . import opcode_31
m.__dict__["opcode_31"] = opcode_31
sys.modules["xdis.opcodes.opcode_31"] = opcode_31
import xdis.opcodes.opcode_31
setattr(m, "opcode_31", opcode_31)

from . import opcode_32
m.__dict__["opcode_32"] = opcode_32
sys.modules["xdis.opcodes.opcode_32"] = opcode_32
import xdis.opcodes.opcode_32
setattr(m, "opcode_32", opcode_32)

from . import opcode_32pypy
m.__dict__["opcode_32pypy"] = opcode_32pypy
sys.modules["xdis.opcodes.opcode_32pypy"] = opcode_32pypy
import xdis.opcodes.opcode_32pypy
setattr(m, "opcode_32pypy", opcode_32pypy)

from . import opcode_33
m.__dict__["opcode_33"] = opcode_33
sys.modules["xdis.opcodes.opcode_33"] = opcode_33
import xdis.opcodes.opcode_33
setattr(m, "opcode_33", opcode_33)

from . import opcode_33pypy
m.__dict__["opcode_33pypy"] = opcode_33pypy
sys.modules["xdis.opcodes.opcode_33pypy"] = opcode_33pypy
import xdis.opcodes.opcode_33pypy
setattr(m, "opcode_33pypy", opcode_33pypy)

from . import opcode_34
m.__dict__["opcode_34"] = opcode_34
sys.modules["xdis.opcodes.opcode_34"] = opcode_34
import xdis.opcodes.opcode_34
setattr(m, "opcode_34", opcode_34)

from . import opcode_35
m.__dict__["opcode_35"] = opcode_35
sys.modules["xdis.opcodes.opcode_35"] = opcode_35
import xdis.opcodes.opcode_35
setattr(m, "opcode_35", opcode_35)

from . import opcode_35pypy
m.__dict__["opcode_35pypy"] = opcode_35pypy
sys.modules["xdis.opcodes.opcode_35pypy"] = opcode_35pypy
import xdis.opcodes.opcode_35pypy
setattr(m, "opcode_35pypy", opcode_35pypy)

from . import opcode_36
m.__dict__["opcode_36"] = opcode_36
sys.modules["xdis.opcodes.opcode_36"] = opcode_36
import xdis.opcodes.opcode_36
setattr(m, "opcode_36", opcode_36)

from . import opcode_36pypy
m.__dict__["opcode_36pypy"] = opcode_36pypy
sys.modules["xdis.opcodes.opcode_36pypy"] = opcode_36pypy
import xdis.opcodes.opcode_36pypy
setattr(m, "opcode_36pypy", opcode_36pypy)

from . import opcode_37
m.__dict__["opcode_37"] = opcode_37
sys.modules["xdis.opcodes.opcode_37"] = opcode_37
import xdis.opcodes.opcode_37
setattr(m, "opcode_37", opcode_37)

from . import opcode_38
m.__dict__["opcode_38"] = opcode_38
sys.modules["xdis.opcodes.opcode_38"] = opcode_38
import xdis.opcodes.opcode_38
setattr(m, "opcode_38", opcode_38)

from . import opcode_3x
m.__dict__["opcode_3x"] = opcode_3x
sys.modules["xdis.opcodes.opcode_3x"] = opcode_3x
import xdis.opcodes.opcode_3x
setattr(m, "opcode_3x", opcode_3x)

from . import opcode_39
m.__dict__["opcode_39"] = opcode_39
sys.modules["xdis.opcodes.opcode_39"] = opcode_39
import xdis.opcodes.opcode_39
setattr(m, "opcode_39", opcode_39)


from six import iterbytes, iteritems, iterkeys, iterlists, itertools, itervalues, viewitems, viewkeys, viewvalues, with_metaclass, text_type
from collections import namedtuple
OpcodeInfo = namedtuple('OpcodeInfo', ['opcode', 'name', 'byte'])
opcode_info = dict((x[1], OpcodeInfo(opcode=x[0], name=x[1], byte=bytearray((x[0],)))) for x in enumerate(opcode_3x.opname))
import collections
tgtmod = opcode_39
tgtdict = tgtmod.__dict__
py3x_mods_dict = __import__('collections').OrderedDict(reversed(sorted(list(dict(filter(lambda x: x[0].startswith('opcode_3'), viewitems(m.__dict__))).items()))))
py_ver_op_keys = list(py3x_mods_dict.keys())
all_updated = [updated := [((tgtdict.__setitem__(k, v), (k, v))[1] if not tgtdict.__contains__(k) else None) for (k, v) in py3x_mods_dict[py_ver_op_key].__dict__.items()] for py_ver_op_key in py_ver_op_keys];


