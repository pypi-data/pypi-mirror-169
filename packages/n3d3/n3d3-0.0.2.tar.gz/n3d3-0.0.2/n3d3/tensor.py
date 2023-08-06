from typing import Union, Any
import n3d3.libN3D3 as libN3D3

class tensor:

    _tensor_generators = {
        "f": libN3D3.Tensor_float,
        "float": libN3D3.Tensor_float,
        "short": libN3D3.Tensor_short,
        "s": libN3D3.Tensor_short,
        "long": libN3D3.Tensor_long,
        "l": libN3D3.Tensor_long,
        "i": libN3D3.Tensor_int,
        "int": libN3D3.Tensor_int,
        # "b": libN3D3.Tensor_bool,
        # "bool": libN3D3.Tensor_bool,
        "d": libN3D3.Tensor_double,
        "double": libN3D3.Tensor_double,
        "uchar": libN3D3.Tensor_unsigned_char,
        "char": libN3D3.Tensor_char,
    }

    def __init__(self, dims:Union[list, tuple], value:Any=None, datatype:str="float"):
        self._datatype = datatype
        generators = self._tensor_generators
        if datatype in generators:
            if not value:
                self._tensor = generators[datatype](dims)
            else:
                self._tensor = generators[datatype](dims, value)
        else:
            raise TypeError(f"Unrecognized Tensor datatype {str(datatype)}")

    def __str__(self)->str:
        output = "n3d3.tensor([\n"
        output += str(self._tensor)
        output += "]"
        output += ", datatype=" + self.data_type()
        output += ")"
        return output

    def __repr__(self)->str:
        return str(self._tensor)


    def data_type(self):
        """Return the data type of the object stored by the tensor.
        """
        return self._datatype
  
