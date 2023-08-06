# Local imports
from qwilfish.constants import DEFAULT_START_SYMBOL
from qwilfish.grammar import opts
from qwilfish.grammar_utils import srange
from qwilfish.grammar_utils import to_binstr
from qwilfish.grammar_utils import fix_tlv_length
from qwilfish.grammar_utils import gen_random_data
from qwilfish.grammar_utils import del_rand_symbols
from qwilfish.grammar_utils import scramble_symbols
from qwilfish.session_builder import register_grammar

# TODO fuzz by changing endianness of fields and/or bytes
# TODO fuzz by inserting wrong TLVs

TL_BITLEN = 16 # number of bits for Type+Length fields

# Name of the plugin
PLUGIN_IDENTIFIER = "simplified_lldp_grammar"

def initialize():
    '''Will be called by the plugin loader.'''
    register_grammar(PLUGIN_IDENTIFIER, create)

def create():
    return ETHERNET_FRAME_GRAMMAR.copy()

FULL_FRAME_STR = "<lldp-tlv-chassiid>"
FULL_FRAME_STR += "<lldp-tlv-portid>"
FULL_FRAME_STR += "<lldp-tlv-ttl>"
FULL_FRAME_STR += "<lldp-tlv-end>"

ETHERNET_FRAME_GRAMMAR = {
    DEFAULT_START_SYMBOL:
        [("<ethernet-frame>", opts(post=to_binstr))],
    "<ethernet-frame>":
        ["<addr><vlan-tags><type-payload>"],
    "<addr>":
        ["<dst><src>"],
    "<dst>":
        [("<byte><byte><byte><byte><byte><byte>", opts(prob=0.1)),
          "<mef-multicast>"
        ],
    "<mef-multicast>":
        ["x01x80xC2x00x00x00", "x01x80xC2x00x00x03", "x01x80xC2x00x00x0E"],
    "<src>":
        ["<byte><byte><byte><byte><byte><byte>"],
    "<vlan-tags>":
        ["", "<q-tag><vlan-tags>", "<q-tag>"],
    "<q-tag>":
        ["<tpid><pcp><dei><vlan>"],
    "<tpid>":
        ["x81x00", "x88xA8"],
    "<pcp>":
        ["<bit><bit><bit>"],
    "<dei>":
        ["<bit>"],
    "<vlan>":
        ["<byte><bit><bit><bit><bit>"],
    "<type-payload>":
        ["<lldp-ethertype><lldp-payload>"],
    "<byte>":
        ["x<hex><hex>"],
    "<hex>":
        srange("0123456789ABCDEF"),
    "<bit>":
        ["0", "1"],
    "<lldp-ethertype>":
        ["x88xCC"],
    "<lldp-payload>":
        ["<lldp-payload-neat>"],
    "<lldp-payload-neat>":
        [FULL_FRAME_STR],
    "<tlv-len>":
        ["<bit><byte>"],
    "<lldp-tlv-chassiid>":
        [("0000001<tlv-len><chassiid-subtype><chassiid-data>",
         opts(post=fix_tlv_length(TL_BITLEN)))
        ],
    "<chassiid-subtype>":
        [("00000001", opts(mab=1)),
         ("00000010", opts(mab=1)),
         ("00000011", opts(mab=1)),
         ("00000100", opts(mab=1)),
         ("00000101", opts(mab=1)),
         ("00000110", opts(mab=1)),
         ("00000111", opts(mab=1))
        ],
    "<chassiid-data>":
        ["<randomized-tlv-data>"],
    "<lldp-tlv-portid>":
        [("0000010<tlv-len><portid-subtype><portid-data>",
          opts(post=fix_tlv_length(TL_BITLEN)))
        ],
    "<portid-subtype>":
        ["00000001",
         "00000010",
         "00000011",
         "00000100",
         "00000101",
         "00000110",
         "00000111"
        ],
    "<portid-data>":
        ["<randomized-tlv-data>"],
    "<lldp-tlv-ttl>":
        [("0000011<tlv-len><byte><byte>",
          opts(post=fix_tlv_length(TL_BITLEN)))
        ],
    "<lldp-tlv-end>":
        ["x00x00"],
    "<randomized-tlv-data>":
        [("", opts(pre=gen_random_data(0, 100)))]
}
