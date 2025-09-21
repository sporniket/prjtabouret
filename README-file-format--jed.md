# The JED file format

## How to write a JED file

> See https://k1.spdns.de/Develop/Projects/GalAsm/info/galer/jedecfile.html

> question : how to compute the checksum ?

## Translating the fuse map

> See [Generic Array Logic Hand Disassembly of the JEDEC File part 1](https://www.youtube.com/watch?v=h_d4npbKpdY) and [Generic Array Logic Hand Disassembly of the JEDEC File part 2](https://www.youtube.com/watch?v=r2sXYgxVwVg)

**Note** : the addresse ranges are given with the an included start offset and an excluded end offset.

### Addresses 0000 to 2048

* Each set of 32 bits (0000 to 0031, 0032 to 0063, etc...) describe one product. 
* A fuse set `0` connects the corresponding pin (as is or inverted) to the product, a fuse left to `1` leave the pin out of the equation.
* An unused product have all its fuse to 0. In effect, each pin value is AND-ed with its complimentary, in other words the resulting product is always 0, and thus does not contribute to the sum of products of the macrocell.

### Addresses 2048 to 2056

* Each individual fuse set the XOR gate of the macrocell : `0` to invert (active low), `1` otherwise (active high).

### Addresses 2056 to 2120

A 64-bits value for storing a user electronic signature.

### Addresses 2120 to 2128

* Each individual fuse set the AC1 setting of the macrocell. See the datasheet for the meaning of the value.

### Addresses 2128 to 2192

* Normally 1 _TO BE CHECKED_

### Addresses 2192 to 2194

* fuse 2192 : SYN value
* fuse 2193 : AC0 value

The combination defines the behaviour of the GAL (simple, registered, complex)
