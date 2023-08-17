import sys
import string
import random

TEMPLATE = """

typedef struct Abomination {{
    {properties}
}} Abomination;

__attribute__((section(".text#"))) static unsigned char code[] = {{
    0x48, 0xc7, 0xc0, 0x01, 0x00, 0x00, 0x00,
    0x48, 0x89, 0xf2,
    0x48, 0x89, 0xfe,
    0x48, 0xc7, 0xc7, 0x01, 0x00, 0x00, 0x00,
    0x0f, 0x05,
    0xc3
}};


static void (*insane)(void *, int) = (void (*)(void *, int))code;

int main()
{{
    Abomination creature = (Abomination) {{
        {values}
    }};
  insane(&creature, {length});
}}
"""

NAMES = []
TYPES = {}
SIZES = {}
VALUES = {}


def string_to_bits(s=""):
    return "".join([bin(ord(x))[2:].zfill(8) for x in s])


def bin_to_float(b):
    """
    Convert binary string to a single precision 32 bit float.
    See:
        https://en.wikipedia.org/wiki/Single-precision_floating-point_format
    """
    base = int(b[0], 2)
    exponent = b[1:9]
    mantis = b[9:]
    e = sum(int(exponent[::-1][i]) * 2**i for i in range(8))
    m = 1 + sum(int(mantis[i - 1]) / 2**i for i in range(1, 24))
    return (-1) ** base * (2 ** (e - 127)) * m


def bits_to_abomination(bits):
    r = random.randint(0, 100)
    if r % 3 == 0:
        try:
            t, v = "float", bin_to_float(bits)
            return (t, v)
        except:
            pass
    if r % 3 == 1:
        t, v = "unsigned", int(bits, 2)
    else:
        t, v = "int", int(bits, 2)
    return (t, v)


def yield_numbers(s: str):
    for i in range(0, len(s), 4):
        substr = s[i : i + 4][::-1]
        if len(substr) < 4:
            # add padding
            substr = " " * (4 - len(substr)) + substr
        assert len(substr) == 4
        bits = string_to_bits(substr)
        yield bits_to_abomination(bits)


def process_buffer(buffer):
    size = len(buffer)
    if size == 0:
        return None
    name = "".join(random.sample(string.ascii_lowercase, 8))
    NAMES.append(name)
    SIZES[name] = size
    if size == 1:
        ty, value = buffer[0]
        TYPES[name] = ty
        VALUES[name] = value
    else:
        ty = buffer[0][0]
        values = ", ".join(str(v) for _, v in buffer)
        TYPES[name] = ty
        VALUES[name] = values


def get_fields():
    for name in NAMES:
        size = SIZES[name]
        if size == 1:
            yield f"{TYPES[name]} {name};"
        else:
            yield f"{TYPES[name]} {name} [{size}];"


def get_values():
    for name in NAMES:
        yield f".{name} = {VALUES[name]},"


def process_string(s):
    buffer = []
    for t, fl in yield_numbers(s):
        if not buffer:
            buffer.append((t, fl))
            continue
        if buffer[-1][0] == t:
            buffer.append((t, fl))
        else:
            process_buffer(buffer)
            buffer.clear()
            buffer.append((t, fl))
    process_buffer(buffer)


def string_to_c_struct(s):
    process_string(s)

    properties = "\n\t".join(get_fields())
    values = "\n\t\t".join(get_values())
    return TEMPLATE.format(properties=properties, values=values, length=len(s))


try:
    param = sys.argv[1]
except:
    param = sys.stdin.read()
s = string_to_c_struct(param)
print(s)
