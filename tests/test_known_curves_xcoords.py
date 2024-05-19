from echec import echec
from echec.helpers import to_integer, byteswap

xcoords_curve25519 = [
    "0x9",
    "e6db6867583030db3594c1a424b15f7c726624ec26b3353b10a903a6d0ab1c4c",
    "c3da55379de9c6908e94ea4df28d084f32eccf03491c71f754b4075577a28552",
    "422c8e7a6227d7bca1350b3e2bb7279f7897b87bb6854b783c60e80311ae3079",
    "684cf59ba83309552800ef566f2f4d3c1c3887c49360e3875f2eb94d99532c51",
    "7c3911e0ab2586fd864497297e575e6f3bc601c0883c30df5f4dd2d24f665424",
    "8520f0098930a754748b7ddcb43ef75a0dbf3a0d26381af4eba4a98eaa9b4e6a",
    "de9edb7d7b7dc1b4d35b61c2ece435373f8343c85b78674dadfc7e146f882b4f",
    "4a5d9d5ba4ce2de1728e3bf480350f25e07e21c947d19e3376f09b3c1e161742",

    "48d5ddd4061257ba166fa3f9bbdb74f1a4e81c089384fa77f790709f0dfbc766",
    "0be7c1f5aad87d7e448662673298a443478b859745179eaf564c79c0ef6eee25",
    "c74950607a12327f3204d94b6825bfb068b7f8319a9e3708ed3d43ce8130c950",
]

def test_xcoords_curve25519():
    curves = echec.find_curves_from_xcoords(xcoords_curve25519)
    curves = [curve.name for curve in curves]
    assert "other/Curve25519" in curves


def test_byteswapped_xcoords_curve25519():
    xcoords = [byteswap(to_integer(x)) for x in xcoords_curve25519]
    curves = echec.find_curves_from_xcoords(xcoords)
    curves = [curve.name for curve in curves]
    assert "other/Curve25519" in curves


xcoords_curve448 = [
    5,
    "06fce640fa3487bfda5f6cf2d5263f8aad88334cbd07437f020f08f9"
        "814dc031ddbdc38c19c6da2583fa5429db94ada18aa7a7fb4ef8a086",
    "ce3e4ff95a60dc6697da1db1d85e6afbdf79b50a2412d7546d5f239f"
        "e14fbaadeb445fc66a01b0779d98223961111e21766282f73dd96b6f",
    "3f482c8a9f19b01e6c46ee9711d9dc14fd4bf67af30765c2ae2b846a"
        "4d23a8cd0db897086239492caf350b51f833868b9bc2b3bca9cf4113",
    "aa3b4749d55b9daf1e5b00288826c467274ce3ebbdd5c17b975e09d4"
        "af6c67cf10d087202db88286e2b79fceea3ec353ef54faa26e219f38",
    "077f453681caca3693198420bbe515cae0002472519b3e67661a7e89"
        "cab94695c8f4bcd66e61b9b9c946da8d524de3d69bd9d9d66b997e37",
    "9b08f7cc31b7e3e67d22d5aea121074a273bd2b83de09c63faa73d2c"
        "22c5d9bbc836647241d953d40c5b12da88120d53177f80e532c41fa0",
    "3eb7a829b0cd20f5bcfc0b599b6feccf6da4627107bdb0d4f345b430"
        "27d8b972fc3e34fb4232a13ca706dcb57aec3dae07bdc1c67bf33609",
    "07fff4181ac6cc95ec1c16a94a0f74d12da232ce40a77552281d282b"
        "b60c0b56fd2464c335543936521c24403085d59a449a5037514a879d",
]

def test_xcoords_curve448():
    curves = echec.find_curves_from_xcoords(xcoords_curve448)
    curves = [curve.name for curve in curves]
    assert "other/Curve448" in curves


def test_byteswapped_xcoords_curve448():
    xcoords = [byteswap(to_integer(x)) for x in xcoords_curve448]
    curves = echec.find_curves_from_xcoords(xcoords)
    curves = [curve.name for curve in curves]
    assert "other/Curve448" in curves


#   - There are two known curves that match this set of x-coords
#   - We don't test this one with the byte order swapped,
#     since one of the x's ends in a zero-byte;
#     reversing the order here and then again in find_curves_from_xcoords()
#     loses that byte and results in a different value.
xcoords_nistp256_e521 = [
    "6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296",
    "2442A5CC0ECD015FA3CA31DC8E2BBC70BF42D60CBCA20085E0822CB04235E970",
    "CB28E0999B9C7715FD0A80D8E47A77079716CBBF917DD72E97566EA1C066957C",
    "4F7497629362EFBBEE591206D036568F239789B234960635C6607EC699062600",
    "726E5684964DB8EA341D8679DFB70E04EDA404E994BA730FA43F1E78ED81211B",
    "CB28E0999B9C7715FD0A80D8E47A77079716CBBF917DD72E97566EA1C066957C",
]

def test_xcoords_nistp256_e521():
    curves = echec.find_curves_from_xcoords(xcoords_nistp256_e521)
    curves = [curve.name for curve in curves]
    assert "other/E-521" in curves
    assert "nist/P-256" in curves


xcoords_nistp384 = [
    0xAA87CA22BE8B05378EB1C71EF320AD746E1D3B628BA79B9859F741E082542A385502F25DBF55296C3A545E3872760AB7,
    0x96281BF8DD5E0525CA049C048D345D3082968D10FEDF5C5ACA0C64E6465A97EA5CE10C9DFEC21797415710721F437922,
    0xFB017B914E29149432D8BAC29A514640B46F53DDAB2C69948084E2930F1C8F7E08E07C9C63F2D21A07DCB56A6AF56EB3,
    0x94B9065777A3B5BE399CEE66A9DB4E648422E370F19ED1A9C699769E01EC9A30E544EB107D35F7C93FA8FB118DCB91ED,
    0x6A142FF2B0B8C5529B7F78E21B014764440ED8C0339B218713DB95003D1A8BA50811C3B841B34CA6E1785BC8DB9111F4,
    0xFB017B914E29149432D8BAC29A514640B46F53DDAB2C69948084E2930F1C8F7E08E07C9C63F2D21A07DCB56A6AF56EB3,
]

def test_xcoords_nistp384():
    curves = echec.find_curves_from_xcoords(xcoords_nistp384)
    curves = [curve.name for curve in curves]
    assert "nist/P-384" in curves


def test_byteswapped_xcoords_nistp384():
    xcoords = [byteswap(to_integer(x)) for x in xcoords_nistp384]
    curves = echec.find_curves_from_xcoords(xcoords)
    curves = [curve.name for curve in curves]
    assert "nist/P-384" in curves


xcoords_nistp521 = [
    "00C6858E06B70404E9CD9E3ECB662395B4429C648139053FB521F828AF606B4D3D"
        "BAA14B5E77EFE75928FE1DC127A2FFA8DE3348B3C1856A429BF97E7E31C2E5BD66",
    "0151518F1AF0F563517EDD5485190DF95A4BF57B5CBA4CF2A9A3F6474725A35F7A"
        "FE0A6DDEB8BEDBCD6A197E592D40188901CECD650699C9B5E456AEA5ADD19052A8",
    "0154FD3836AF92D0DCA57DD5341D3053988534FDE8318FC6AAAAB68E2E6F4339B1"
        "9F2F281A7E0B22C269D93CF8794A9278880ED7DBB8D9362CAEACEE544320552251",
    "00921F3ECEAF579CFDDA6AF9C1728E5BCA33F77B57F5984C624BFF10F244B57714"
        "4CA24E20310DEF2F777892DA1ED5DEA9A6EF0985D965AE98BCF129855C6C4F3311",
    "00AF23A77F50CC548CEBC50658FE4A0BA26FF9DE4E864DE27FD059B63AE14B5F87"
        "286BC77AAEBA324FF675A1FF7035B689AF383595F8B5A867432FFE8BF29CF60688",
    "0154FD3836AF92D0DCA57DD5341D3053988534FDE8318FC6AAAAB68E2E6F4339B1"
        "9F2F281A7E0B22C269D93CF8794A9278880ED7DBB8D9362CAEACEE544320552251",
]

def test_xcoords_nistp521():
    curves = echec.find_curves_from_xcoords(xcoords_nistp521)
    curves = [curve.name for curve in curves]
    assert "nist/P-521" in curves


def test_byteswapped_xcoords_nistp521():
    xcoords = [byteswap(to_integer(x)) for x in xcoords_nistp521]
    curves = echec.find_curves_from_xcoords(xcoords)
    curves = [curve.name for curve in curves]
    assert "nist/P-521" in curves
