#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class SexType:
  MALE = 1
  FEMALE = 2

  _VALUES_TO_NAMES = {
    1: "MALE",
    2: "FEMALE",
  }

  _NAMES_TO_VALUES = {
    "MALE": 1,
    "FEMALE": 2,
  }


class User:
  """
  Attributes:
   - firstname
   - lastname
   - user_id
   - sex
   - active
   - description
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'firstname', None, None, ), # 1
    (2, TType.STRING, 'lastname', None, None, ), # 2
    (3, TType.I32, 'user_id', None, 0, ), # 3
    (4, TType.I32, 'sex', None, None, ), # 4
    (5, TType.BOOL, 'active', None, False, ), # 5
    (6, TType.STRING, 'description', None, None, ), # 6
  )

  def __init__(self, firstname=None, lastname=None, user_id=thrift_spec[3][4], sex=None, active=thrift_spec[5][4], description=None,):
    self.firstname = firstname
    self.lastname = lastname
    self.user_id = user_id
    self.sex = sex
    self.active = active
    self.description = description

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.firstname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.lastname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.user_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.sex = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.active = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.description = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('User')
    if self.firstname != None:
      oprot.writeFieldBegin('firstname', TType.STRING, 1)
      oprot.writeString(self.firstname)
      oprot.writeFieldEnd()
    if self.lastname != None:
      oprot.writeFieldBegin('lastname', TType.STRING, 2)
      oprot.writeString(self.lastname)
      oprot.writeFieldEnd()
    if self.user_id != None:
      oprot.writeFieldBegin('user_id', TType.I32, 3)
      oprot.writeI32(self.user_id)
      oprot.writeFieldEnd()
    if self.sex != None:
      oprot.writeFieldBegin('sex', TType.I32, 4)
      oprot.writeI32(self.sex)
      oprot.writeFieldEnd()
    if self.active != None:
      oprot.writeFieldBegin('active', TType.BOOL, 5)
      oprot.writeBool(self.active)
      oprot.writeFieldEnd()
    if self.description != None:
      oprot.writeFieldBegin('description', TType.STRING, 6)
      oprot.writeString(self.description)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InvalidValueException(Exception):
  """
  Attributes:
   - error_code
   - error_msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'error_code', None, None, ), # 1
    (2, TType.STRING, 'error_msg', None, None, ), # 2
  )

  def __init__(self, error_code=None, error_msg=None,):
    self.error_code = error_code
    self.error_msg = error_msg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.error_code = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.error_msg = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InvalidValueException')
    if self.error_code != None:
      oprot.writeFieldBegin('error_code', TType.I32, 1)
      oprot.writeI32(self.error_code)
      oprot.writeFieldEnd()
    if self.error_msg != None:
      oprot.writeFieldBegin('error_msg', TType.STRING, 2)
      oprot.writeString(self.error_msg)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
