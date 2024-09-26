#   ------------------------------------------------------------------------
#
#   Copyright (C) 2024  Marc Penninga
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   ------------------------------------------------------------------------


import sys

from . import curve

# Some dirty trickery to import all the classes defining elliptic curves
# into the current namespace, for easier access.
ns = sys.modules[__name__].__dict__
for cls in curve.CURVE_TYPES:
    ns[cls.__name__] = cls


KNOWN_CURVES = [

    ########    RECOMMENDED ELLIPTIC CURVES FOR FEDERAL GOVERNMENT USE  July 1999

    #   Also known as secg/secp192r1, x962/prime192v1
    Weierstrass(
        name="nist/P-192",
        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
    ),
    #   Also known as secg/secp224r1, wtls/wap-wsg-idm-ecid-wtls12, x963/ansip224r1
    Weierstrass(
        name="nist/P-224",
        p=0xffffffffffffffffffffffffffffffff000000000000000000000001,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe,
        b=0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4,
    ),
    #   Also known as secg/secp256r1, x962/prime256v1
    Weierstrass(
        name="nist/P-256",
        p=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
        a=0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc,
        b=0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
    ),
    #   Also known as secg/secp384r1, x963/ansip384r1
    Weierstrass(
        name="nist/P-384",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff,
        a=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000fffffffc,
        b=0xb3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef,
    ),
    #   Also known as secg/secp521r1, x963/ansip521r1
    Weierstrass(
        name="nist/P-521",
        p=0x01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        a=0x01fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc,
        b=0x0051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00,
    ),


    ########    ANSI x9.62 example curves.

    Weierstrass(
        name="x962/prime192v2",
        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0xcc22d6dfb95c6b25e49c0d6364a4e5980c393aa21668d953,
    ),
    Weierstrass(
        name="x962/prime192v3",
        p=0xfffffffffffffffffffffffffffffffeffffffffffffffff,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffc,
        b=0x22123dc2395a05caa7423daeccc94760a7d462256bd56916,
    ),
    Weierstrass(
        name="x962/prime239v1",
        p=0x7fffffffffffffffffffffff7fffffffffff8000000000007fffffffffff,
        a=0x7fffffffffffffffffffffff7fffffffffff8000000000007ffffffffffc,
        b=0x6b016c3bdcf18941d0d654921475ca71a9db2fb27d1d37796185c2942c0a,
    ),
    Weierstrass(
        name="x962/prime239v2",
        p=0x7fffffffffffffffffffffff7fffffffffff8000000000007fffffffffff,
        a=0x7fffffffffffffffffffffff7fffffffffff8000000000007ffffffffffc,
        b=0x617fab6832576cbbfed50d99f0249c3fee58b94ba0038c7ae84c8c832f2c,
    ),
    Weierstrass(
        name="x962/prime239v3",
        p=0x7fffffffffffffffffffffff7fffffffffff8000000000007fffffffffff,
        a=0x7fffffffffffffffffffffff7fffffffffff8000000000007ffffffffffc,
        b=0x255705fa2a306654b1f4cb03d6a750a30c250102d4988717d9ba15ab6d3e,
    ),


    ########    ANSI x9.63 example curves.

    #   Also known as secg/secp160k1
    Weierstrass(
        name="x963/ansip160k1",
        p=0xfffffffffffffffffffffffffffffffeffffac73,
        a=0x0,
        b=0x7,
    ),
    #   Also known as secg/secp160r1, wtls/wap-wsg-idm-ecid-wtls7
    Weierstrass(
        name="x963/ansip160r1",
        p=0xffffffffffffffffffffffffffffffff7fffffff,
        a=0xffffffffffffffffffffffffffffffff7ffffffc,
        b=0x1c97befc54bd7a8b65acf89f81d4d4adc565fa45,
    ),
    #   Also known as secg/secp160r2
    Weierstrass(
        name="x963/ansip160r2",
        p=0xfffffffffffffffffffffffffffffffeffffac73,
        a=0xfffffffffffffffffffffffffffffffeffffac70,
        b=0xb4e134d3fb59eb8bab57274904664d5af50388ba,
    ),
    #   Also known as secg/secp192k1
    Weierstrass(
        name="x963/ansip192k1",
        p=0xfffffffffffffffffffffffffffffffffffffffeffffee37,
        a=0x0,
        b=0x3,
    ),
    #   Also known as secg/secp224k1
    Weierstrass(
        name="x963/ansip224k1",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffeffffe56d,
        a=0x0,
        b=0x5,
    ),
    #   Also known as secg/secp256k1
    Weierstrass(
        name="x963/ansip256k1",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
        a=0x0,
        b=0x7,
    ),


    ########    SEC 2: Recommended Elliptic Curve Domain Parameters version 2.0  January 27, 2010

    #   A randomly generated curve. [SEC2v1](https://www.secg.org/SEC2-Ver-1.0.pdf) states 'E was chosen verifiably at random as specified in ANSI X9.62 [1] from the seed'.
    #   Also known as wtls/wap-wsg-idm-ecid-wtls6
    Weierstrass(
        name="secg/secp112r1",
        p=0xdb7c2abf62e35e668076bead208b,
        a=0xdb7c2abf62e35e668076bead2088,
        b=0x659ef8ba043916eede8911702b22,
    ),
    #   A randomly generated curve. [SEC2v1](https://www.secg.org/SEC2-Ver-1.0.pdf) states 'E was chosen verifiably at random as specified in ANSI X9.62 [1] from the seed'.
    Weierstrass(
        name="secg/secp112r2",
        p=0xdb7c2abf62e35e668076bead208b,
        a=0x6127c24c05f38a0aaaf65c0ef02c,
        b=0x51def1815db5ed74fcc34c85d709,
    ),
    #   A randomly generated curve. [SEC2v1](https://www.secg.org/SEC2-Ver-1.0.pdf) states 'E was chosen verifiably at random as specified in ANSI X9.62 [1] from the seed'.
    Weierstrass(
        name="secg/secp128r1",
        p=0xfffffffdffffffffffffffffffffffff,
        a=0xfffffffdfffffffffffffffffffffffc,
        b=0xe87579c11079f43dd824993c2cee5ed3,
    ),
    #   A randomly generated curve. [SEC2v1](https://www.secg.org/SEC2-Ver-1.0.pdf) states 'E was chosen verifiably at random as specified in ANSI X9.62 [1] from the seed'.
    Weierstrass(
        name="secg/secp128r2",
        p=0xfffffffdffffffffffffffffffffffff,
        a=0xd6031998d1b3bbfebf59cc9bbff9aee1,
        b=0x5eeefca380d02919dc2c6558bb6d8a5d,
    ),


    ########    ECC Brainpool Standard Curves and Curve Generation v. 1.0  19.10.2005

    Weierstrass(
        name="brainpool/brainpoolP160r1",
        p=0xe95e4a5f737059dc60dfc7ad95b3d8139515620f,
        a=0x340e7be2a280eb74e2be61bada745d97e8f7c300,
        b=0x1e589a8595423412134faa2dbdec95c8d8675e58,
    ),
    Weierstrass(
        name="brainpool/brainpoolP160t1",
        p=0xe95e4a5f737059dc60dfc7ad95b3d8139515620f,
        a=0xe95e4a5f737059dc60dfc7ad95b3d8139515620c,
        b=0x7a556b6dae535b7b51ed2c4d7daa7a0b5c55f380,
    ),
    Weierstrass(
        name="brainpool/brainpoolP192r1",
        p=0xc302f41d932a36cda7a3463093d18db78fce476de1a86297,
        a=0x6a91174076b1e0e19c39c031fe8685c1cae040e5c69a28ef,
        b=0x469a28ef7c28cca3dc721d044f4496bcca7ef4146fbf25c9,
    ),
    Weierstrass(
        name="brainpool/brainpoolP192t1",
        p=0xc302f41d932a36cda7a3463093d18db78fce476de1a86297,
        a=0xc302f41d932a36cda7a3463093d18db78fce476de1a86294,
        b=0x13d56ffaec78681e68f9deb43b35bec2fb68542e27897b79,
    ),
    Weierstrass(
        name="brainpool/brainpoolP224r1",
        p=0xd7c134aa264366862a18302575d1d787b09f075797da89f57ec8c0ff,
        a=0x68a5e62ca9ce6c1c299803a6c1530b514e182ad8b0042a59cad29f43,
        b=0x2580f63ccfe44138870713b1a92369e33e2135d266dbb372386c400b,
    ),
    Weierstrass(
        name="brainpool/brainpoolP224t1",
        p=0xd7c134aa264366862a18302575d1d787b09f075797da89f57ec8c0ff,
        a=0xd7c134aa264366862a18302575d1d787b09f075797da89f57ec8c0fc,
        b=0x4b337d934104cd7bef271bf60ced1ed20da14c08b3bb64f18a60888d,
    ),
    Weierstrass(
        name="brainpool/brainpoolP256r1",
        p=0xa9fb57dba1eea9bc3e660a909d838d726e3bf623d52620282013481d1f6e5377,
        a=0x7d5a0975fc2c3057eef67530417affe7fb8055c126dc5c6ce94a4b44f330b5d9,
        b=0x26dc5c6ce94a4b44f330b5d9bbd77cbf958416295cf7e1ce6bccdc18ff8c07b6,
    ),
    Weierstrass(
        name="brainpool/brainpoolP256t1",
        p=0xa9fb57dba1eea9bc3e660a909d838d726e3bf623d52620282013481d1f6e5377,
        a=0xa9fb57dba1eea9bc3e660a909d838d726e3bf623d52620282013481d1f6e5374,
        b=0x662c61c430d84ea4fe66a7733d0b76b7bf93ebc4af2f49256ae58101fee92b04,
    ),
    Weierstrass(
        name="brainpool/brainpoolP320r1",
        p=0xd35e472036bc4fb7e13c785ed201e065f98fcfa6f6f40def4f92b9ec7893ec28fcd412b1f1b32e27,
        a=0x3ee30b568fbab0f883ccebd46d3f3bb8a2a73513f5eb79da66190eb085ffa9f492f375a97d860eb4,
        b=0x520883949dfdbc42d3ad198640688a6fe13f41349554b49acc31dccd884539816f5eb4ac8fb1f1a6,
    ),
    Weierstrass(
        name="brainpool/brainpoolP320t1",
        p=0xd35e472036bc4fb7e13c785ed201e065f98fcfa6f6f40def4f92b9ec7893ec28fcd412b1f1b32e27,
        a=0xd35e472036bc4fb7e13c785ed201e065f98fcfa6f6f40def4f92b9ec7893ec28fcd412b1f1b32e24,
        b=0xa7f561e038eb1ed560b3d147db782013064c19f27ed27c6780aaf77fb8a547ceb5b4fef422340353,
    ),
    Weierstrass(
        name="brainpool/brainpoolP384r1",
        p=0x8cb91e82a3386d280f5d6f7e50e641df152f7109ed5456b412b1da197fb71123acd3a729901d1a71874700133107ec53,
        a=0x7bc382c63d8c150c3c72080ace05afa0c2bea28e4fb22787139165efba91f90f8aa5814a503ad4eb04a8c7dd22ce2826,
        b=0x4a8c7dd22ce28268b39b55416f0447c2fb77de107dcd2a62e880ea53eeb62d57cb4390295dbc9943ab78696fa504c11,
    ),
    Weierstrass(
        name="brainpool/brainpoolP384t1",
        p=0x8cb91e82a3386d280f5d6f7e50e641df152f7109ed5456b412b1da197fb71123acd3a729901d1a71874700133107ec53,
        a=0x8cb91e82a3386d280f5d6f7e50e641df152f7109ed5456b412b1da197fb71123acd3a729901d1a71874700133107ec50,
        b=0x7f519eada7bda81bd826dba647910f8c4b9346ed8ccdc64e4b1abd11756dce1d2074aa263b88805ced70355a33b471ee,
    ),
    Weierstrass(
        name="brainpool/brainpoolP512r1",
        p=0xaadd9db8dbe9c48b3fd4e6ae33c9fc07cb308db3b3c9d20ed6639cca703308717d4d9b009bc66842aecda12ae6a380e62881ff2f2d82c68528aa6056583a48f3,
        a=0x7830a3318b603b89e2327145ac234cc594cbdd8d3df91610a83441caea9863bc2ded5d5aa8253aa10a2ef1c98b9ac8b57f1117a72bf2c7b9e7c1ac4d77fc94ca,
        b=0x3df91610a83441caea9863bc2ded5d5aa8253aa10a2ef1c98b9ac8b57f1117a72bf2c7b9e7c1ac4d77fc94cadc083e67984050b75ebae5dd2809bd638016f723,
    ),
    Weierstrass(
        name="brainpool/brainpoolP512t1",
        p=0xaadd9db8dbe9c48b3fd4e6ae33c9fc07cb308db3b3c9d20ed6639cca703308717d4d9b009bc66842aecda12ae6a380e62881ff2f2d82c68528aa6056583a48f3,
        a=0xaadd9db8dbe9c48b3fd4e6ae33c9fc07cb308db3b3c9d20ed6639cca703308717d4d9b009bc66842aecda12ae6a380e62881ff2f2d82c68528aa6056583a48f0,
        b=0x7cbbbcf9441cfab76e1890e46884eae321f70c0bcb4981527897504bec3e36a62bcdfa2304976540f6450085f2dae145c22553b465763689180ea2571867423e,
    ),


    ########    GOST R 34.10-2001: RFC5832, GOST R 34.10-2012: RFC7836

    #   RFC5832
    Weierstrass(
        name="gost/gost256",
        p=0x8000000000000000000000000000000000000000000000000000000000000431,
        a=0x7,
        b=0x5fbff498aa938ce739b8e022fbafef40563f6e6a3472fc2a514c0ce9dae23b7e,
    ),
    #   RFC5832
    Weierstrass(
        name="gost/gost512",
        p=0x4531acd1fe0023c7550d267b6b2fee80922b14b2ffb90f04d4eb7c09b5d2d15df1d852741af4704a0458047e80e4546d35b8336fac224dd81664bbf528be6373,
        a=0x7,
        b=0x1cff0806a31116da29d8cfa54e57eb748bc5f377e49400fdd788b649eca1ac4361834013b2ad7322480a89ca58e0cf74bc9e540c2add6897fad0a3084f302adc,
    ),
    #   RFC7836
    Weierstrass(
        name="gost/id-tc26-gost-3410-12-512-paramSetA",
        p=0x00FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDC7,
        a=0x00FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDC4,
        b=0x00E8C2505DEDFC86DDC1BD0B2B6667F1DA34B82574761CB0E879BD081CFD0B6265EE3CB090F30D27614CB4574010DA90DD862EF9D4EBEE4761503190785A71C760,
    ),
    #   RFC7836
    Weierstrass(
        name="gost/id-tc26-gost-3410-12-512-paramSetB",
        p=0x008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006F,
        a=0x008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006C,
        b=0x687D1B459DC841457E3E06CF6F5E2517B97C7D614AF138BCBF85DC806C4B289F3E965D2DB1416D217F8B276FAD1AB69C50F78BEE1FA3106EFB8CCBC7C5140116,
    ),
    #   RFC4357
    Weierstrass(
        name="gost/id-GostR3410-2001-CryptoPro-A-ParamSet",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd97,
        a=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd94,
        b=0xa6,
    ),
    #   RFC4357
    Weierstrass(
        name="gost/id-GostR3410-2001-CryptoPro-B-ParamSet",
        p=0x8000000000000000000000000000000000000000000000000000000000000c99,
        a=0x8000000000000000000000000000000000000000000000000000000000000c96,
        b=0x3e1af419a269a5f866a7d3c25c3df80ae979259373ff2b182f49d4ce7e1bbc8b,
    ),
    #   RFC4357
    Weierstrass(
        name="gost/id-GostR3410-2001-CryptoPro-C-ParamSet",
        p=0x9b9f605f5a858107ab1ec85e6b41c8aacf846e86789051d37998f7b9022d759b,
        a=0x9b9f605f5a858107ab1ec85e6b41c8aacf846e86789051d37998f7b9022d7598,
        b=0x805a,
    ),
    #   RFC5832
    Edwards(
        name="gost/id-tc26-gost-3410-2012-256-paramSetA",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd97,
        d=0x605f6b7c183fa81578bc39cfad518132b9df62897009af7e522c32d6dc7bffb,
    ),
    #   RFC5832
    Edwards(
        name="gost/id-tc26-gost-3410-2012-512-paramSetC",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdc7,
        d=0x9e4f5d8c017d8d9f13a5cf3cdf5bfe4dab402d54198e31ebde28a0621050439ca6b39e0a515c06b304e2ce43e79e369e91a0cfc2bc2a22b4ca302dbb33ee7550,
    ),


    ########    Agence nationale de la sécurité des systèmes d'information: Publication d'un paramétrage de courbe elliptique visant des applications de passeport électronique et de l'administration électronique française. 21 November 2011

    Weierstrass(
        name="anssi/FRP256v1",
        p=0xf1fd178c0b3ad58f10126de8ce42435b3961adbcabc8ca6de8fcf353d86e9c03,
        a=0xf1fd178c0b3ad58f10126de8ce42435b3961adbcabc8ca6de8fcf353d86e9c00,
        b=0xee353fca5428a9300d4aba754a44c00fdfec0c9ae4b1a1803075ed967b7bb73f,
    ),


    ########    Wireless Application Protocol - Wireless Transport Layer Security (WAP-WTLS) curves: <https://www.wapforum.org/tech/documents/WAP-199-WTLS-20000218-a.pdf>

    Weierstrass(
        name="WTLS/wap-wsg-idm-ecid-wtls8",
        p=0xfffffffffffffffffffffffffde7,
        a=0x0,
        b=0x3,
    ),
    Weierstrass(
        name="WTLS/wap-wsg-idm-ecid-wtls9",
        p=0xfffffffffffffffffffffffffffffffffffc808f,
        a=0x0,
        b=0x3,
    ),


    ########    An assortment of some other curves.

    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Montgomery(
        name="other/M-159",
        p=0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA5,
        A=0x30496,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Montgomery(
        name="other/M-191",
        p=0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFED,
        A=0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBB35F,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Montgomery(
        name="other/M-221",
        p=0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFD,
        A=0x01c93a,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Montgomery(
        name="other/M-383",
        p=0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF45,
        A=0x1f82fe,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Montgomery(
        name="other/M-511",
        p=0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF45,
        A=0x081806,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Edwards(
        name="other/E-157",
        p=0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7B,
        d=0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5B6B,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Edwards(
        name="other/E-168",
        p=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFF,
        d=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC34,
    ),
     #   Curve from https://eprint.iacr.org/2013/647.pdf
   Edwards(
        name="other/E-190",
        p=0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDF,
        d=0x3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC2FF,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Edwards(
        name="other/E-222",
        p=0x3fffffffffffffffffffffffffffffffffffffffffffffffffffff8b,
        d=0x27166,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Edwards(
        name="other/E-382",
        p=0x3fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff97,
        d=0x3ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffef8e1,
    ),
    #   Curve from https://eprint.iacr.org/2013/647.pdf
    Edwards(
        name="other/E-521",
        p=0x1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0x1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffa4331,
    ),
    #   Curve from https://cr.yp.to/ecdh.html
    Montgomery(
        name="other/Curve25519",
        p=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed,
        A=0x76d06,
    ),
    #   Proposed by Barreto on Twitter, as a co-factor 1 alternative to Curve22519;
    #   named by Schwabe and Sprenkels (https://eprint.iacr.org/2019/1166.pdf)
    Weierstrass(
        name="other/Curve13318",
        p=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed,
        a=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffea,
        b=0x3406,
    ),
    #   Curve from https://github.com/relic-toolkit/relic
    Weierstrass(
        name="other/Curve22103",
        p=0x1ffffffffffffffffffffffffffffffffffffffffffffffffffffffd,
        a=0x155555555555555555555555555555555555555555555552174084FF,
        b=0x1425ED097B425ED097B425ED097B425ED097B425ED0BBA9428427967,
    ),
    #   Curve from https://github.com/relic-toolkit/relic
    Weierstrass(
        name="other/Curve4417",
        p=0x3fffffffffffffffffffffffffffffffffffffffffffffffffffffffb,
        a=0x4648D10B419379D50F4BA01869D9AE363285E01FE66920878EE075B0,
        b=0x4C4DCEDFAC09383A0311B98EE9637415B9134B4115FDB760C1A3D419,
    ),
    #   Curve from https://eprint.iacr.org/2013/325.pdf
    Weierstrass(
        name="other/Curve1174",
        p=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7,
        a=0x486BE25B34C8080922B969257EEB54C404F914A29067A5560BB9AEE0BC67A6D,
        b=0xE347A25BF875DD2F1F12D8A10334D417CC15E77893A99F4BF278CA563072E6,
    ),
    #   Curve from https://eprint.iacr.org/2013/325.pdf (birationally equivalent Edwards form)
    Edwards(
        name="other/Curve1174-Edwards",
        p=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7,
        d=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffb61,
    ),
    #   Curve from https://github.com/relic-toolkit/relic
    Weierstrass(
        name="other/Curve67254",
        p=0x3fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff97,
        a=0x2E32419A32377AF8E7F03148A106D112C8C2E26D31A89F46B743DEED322C7ADC3024AFE4B5AFD8DB7180281586549F4A,
        b=0x22F6EF3BE72A67FDC236D7173727CD2AF6D02A195753C44BDF451369B02EA0F963D9A775CAE6DC3AE9CCABB7F183C1AD,
    ),
    Montgomery(
        name="other/Curve383187",
        p=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff45,
        A=0x38251,
    ),
    #   Curve from https://ed25519.cr.yp.to
    Edwards(
        name="other/Ed25519",
        p=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed,
        d=0x52036cee2b6ffe738cc740797779e89800700a4d4141d8ab75eb4dca135978a3,
        t=0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffec,
    ),
    #   Curve from RFC7748 (Montgomery form)
    Montgomery(
        name="other/Curve448",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        A=0x262a6,
    ),
    #   Curve from RFC7748 (birationally equivalent Edwards form)
    Edwards(
        name="other/Ed448",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0xd78b4bdc7f0daf19f24f38c29373a2ccad46157242a50f37809b1da3412a12e79ccc9c81264cfe9ad080997058fb61c4243cc32dbaa156b9,
    ),
    #   Curve from https://eprint.iacr.org/2015/625.pdf
    Edwards(
        name="other/Ed448-Goldilocks",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffff6756,
    ),
    #   Curve from https://cr.yp.to/talks/2013.09.16/slides-djb-20130916-a4.pdf
    Edwards(
        name="other/Curve41417",
        p=0x3fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffef,
        d=0xe21,
    ),
    #   Curve used in: https://eprint.iacr.org/2010/354.pdf
    Weierstrass(
        name="other/Fp254BNa",
        p=0x2370fb049d410fbe4e761a9886e502417d023f40180000017e80600000000001,
        a=0x00,
        b=0x05,
    ),
    #   Curve described in https://www.iso.org/standard/80241.html
    Weierstrass(
        name="other/Fp224BN",
        p=0xfffffffffff107288ec29e602c4520db42180823bb907d1287127833,
        a=0x00,
        b=0x03,
    ),
    #   Curve described in https://www.iso.org/standard/80241.html
    Weierstrass(
        name="other/Fp256BN",
        p=0xfffffffffffcf0cd46e5f25eee71a49f0cdc65fb12980a82d3292ddbaed33013,
        a=0x00,
        b=0x03,
    ),
    #   Curve described in https://www.iso.org/standard/80241.html
    Weierstrass(
        name="other/Fp384BN",
        p=0xfffffffffffffffffff2a96823d5920d2a127e3f6fbca024c8fbe29531892c79534f9d306328261550a7cabd7cccd10b,
        a=0x00,
        b=0x03,
    ),
    #   Curve described in https://www.iso.org/standard/80241.html
    Weierstrass(
        name="other/Fp512BN",
        p=0xfffffffffffffffffffffffffff9ec7f01c60ba1d8cb5307c0bbe3c111b0ef455146cf1eacbe98b8e48c65deab236fe1916a55ce5f4c6467b4eb280922adef33,
        a=0x00,
        b=0x03,
    ),
    #   A prime order curve from MIRACL: https://github.com/miracl/MIRACL/blob/master/docs/miracl-explained/miracl-standard-curves.md. Has no generator specified.
    Weierstrass(
        name="other/ssc-160",
        p=0xc90fdaa22168c234c4c6628b80dc1cd129024e1f,
        a=0xc90fdaa22168c234c4c6628b80dc1cd129024e1c,
        b=0xadf85458a2bb4a9aafdc5620273d3cf1d8b9c841,
    ),
    #   A prime order curve from MIRACL: https://github.com/miracl/MIRACL/blob/master/docs/miracl-explained/miracl-standard-curves.md. Has no generator specified.
    Weierstrass(
        name="other/ssc-192",
        p=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cd13,
        a=0xc302f41d932a36cda7a3463093d18db78fce476de1a86294,
        b=0xadf85458a2bb4a9aafdc5620273d3cf1d8b9c583ce2d36a6,
    ),
    #   A prime order curve from MIRACL: https://github.com/miracl/MIRACL/blob/master/docs/miracl-explained/miracl-standard-curves.md. Has no generator specified.
    Weierstrass(
        name="other/ssc-224",
        p=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbedf,
        a=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbedc,
        b=0xadf85458a2bb4a9aafdc5620273d3cf1d8b9c583ce2d3695a9e13a03,
    ),
    #   A prime order curve from MIRACL: https://github.com/miracl/MIRACL/blob/master/docs/miracl-explained/miracl-standard-curves.md. Has no generator specified.
    Weierstrass(
        name="other/ssc-256",
        p=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139c0b,
        a=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139c08,
        b=0xadf85458a2bb4a9aafdc5620273d3cf1d8b9c583ce2d3695a9e13641146434e1,
    ),
    #   A prime order curve from MIRACL: https://github.com/miracl/MIRACL/blob/master/docs/miracl-explained/miracl-standard-curves.md. Has no generator specified.
    Weierstrass(
        name="other/ssc-288",
        p=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a098b,
        a=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a0988,
        b=0xadf85458a2bb4a9aafdc5620273d3cf1d8b9c583ce2d3695a9e13641146433fbcc939f36,
    ),
    #   A prime order curve from MIRACL: https://github.com/miracl/MIRACL/blob/master/docs/miracl-explained/miracl-standard-curves.md. Has no generator specified.
    Weierstrass(
        name="other/ssc-320",
        p=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3408b3,
        a=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3408b0,
        b=0xadf85458a2bb4a9aafdc5620273d3cf1d8b9c583ce2d3695a9e13641146433fbcc939dce249b40a4,
    ),
    #   A prime order curve from MIRACL: https://github.com/miracl/MIRACL/blob/master/docs/miracl-explained/miracl-standard-curves.md. Has no generator specified.
    Weierstrass(
        name="other/ssc-384",
        p=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a437b,
        a=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a4378,
        b=0xadf85458a2bb4a9aafdc5620273d3cf1d8b9c583ce2d3695a9e13641146433fbcc939dce249b3ef97d2fe363630c7791,
    ),
    #   A prime order curve from MIRACL: https://github.com/miracl/MIRACL/blob/master/docs/miracl-explained/miracl-standard-curves.md. Has no generator specified.
    Weierstrass(
        name="other/ssc-512",
        p=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c5ef,
        a=0xc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c5ec,
        b=0xadf85458a2bb4a9aafdc5620273d3cf1d8b9c583ce2d3695a9e13641146433fbcc939dce249b3ef97d2fe363630c75d8f681b202aec4617ad3df1ed5d5fd6a8d,
    ),
    #   Tweedledum pairing friendly curve from <https://github.com/daira/tweedle>.
    Weierstrass(
        name="other/Tweedledum",
        p=0x40000000000000000000000000000000038aa1276c3f59b9a14064e200000001,
        a=0x00,
        b=0x05,
    ),
    #   Tweedledee pairing friendly curve from <https://github.com/daira/tweedle>.
    Weierstrass(
        name="other/Tweedledee",
        p=0x40000000000000000000000000000000038aa127696286c9842cafd400000001,
        a=0x00,
        b=0x05,
    ),
    #   JubJub curve from <https://z.cash/technology/jubjub/>.
    Edwards(
        name="other/JubJub",
        p=0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001,
        d=0x2a9318e74bfa2b48f5fd9207e6bd7fd4292d7f6d37579d2601065fd6d6343eb1,
        t=0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000000,
    ),
    #   Pallas curve from the [Pasta curves](https://electriccoin.co/blog/the-pasta-curves-for-halo-2-and-beyond/).
    Weierstrass(
        name="other/Pallas",
        p=0x40000000000000000000000000000000224698fc094cf91b992d30ed00000001,
        a=0x00,
        b=0x05,
    ),
    #   Vesta curve from the [Pasta curves](https://electriccoin.co/blog/the-pasta-curves-for-halo-2-and-beyond/).
    Weierstrass(
        name="other/Vesta",
        p=0x40000000000000000000000000000000224698fc0994a8dd8c46eb2100000001,
        a=0x00,
        b=0x05,
    ),
    #   The Million Dollar Curve
    Edwards(
        name="other/MDC201601",
        p=0xf13b68b9d456afb4532f92fdd7a5fd4f086a9037ef07af9ec13710405779ec13,
        d=0x571304521965b68a7cdfbfccfb0cb9625f1270f63f21f041ee9309250300cf89,
    ),
    #   BADA55 curve from the https://bada55.cr.yp.to/bada55-20150927.pdf
    Weierstrass(
        name="other/BADA55-R-256",
        p=0xf1fd178c0b3ad58f10126de8ce42435b3961adbcabc8ca6de8fcf353d86e9c03,
        a=0xf1fd178c0b3ad58f10126de8ce42435b3961adbcabc8ca6de8fcf353d86e9c00,
        b=0xbada55bada55bada55bada55bada55bada55bada55bada55bada55bada55bd48,
    ),
    #   BADA55 curve from the https://bada55.cr.yp.to/bada55-20150927.pdf
    Weierstrass(
        name="other/BADA55-VR-224",
        p=0xffffffffffffffffffffffffffffffff000000000000000000000001,
        a=0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe,
        # original b must be reduced modulo p
        b=0xfd9ca54c0738b8a6fb8cf4cdb328e75983d6da1b78b6223463375562,
        # b=0xbada55ecfd9ca54c0738b8a6fb8cf4ccf84e916d83d6da1b78b622351e11ab4e,
    ),
    #   BADA55 curve from the https://bada55.cr.yp.to/bada55-20150927.pdf
    Weierstrass(
        name="other/BADA55-VR-256",
        p=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
        a=0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc,
        b=0xbada55ecd8bbead3add6c534f92197deb47fceb9be7e0e702a8d1dd56b5d0b0c,
    ),
    #   BADA55 curve from the https://bada55.cr.yp.to/bada55-20150927.pdf
    Weierstrass(
        name="other/BADA55-VR-384",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000ffffffff,
        a=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffff0000000000000000fffffffc,
        b=0xbada55ec3be2ad1f9eeea5881ecf95bbf3ac392526f01d4cd13e684c63a17cc4d5f271642ad83899113817a61006413d,
    ),
    #   BADA55 curve from the https://bada55.cr.yp.to/bada55-20150927.pdf
    Weierstrass(
        name="other/BADA55-VPR-224",
        p=0xffffffffffffffffffffffffffffffff000000000000000000000001,
        # original a and b should (implicitly) be reduced modulo p
        a=0x8110b017fda88a224f3f64f3964926308dec9784b13c08f09f4ffc4a,
        # a=0x7144ba12ce8a0c3befa053edbada555a42391fc64f052376e041c7d4af23195ebd8d83625321d452e8a0c3bb0a048a26115704e45dceb346a9f4bd9741d14d49,
        b=0x5587342f92ba3091a9ba09ad867f4cef85778edb831054f9cb5b3ed5,
        # b=0x5c32ec7fc48ce1802d9b70dbc3fa574eaf015fce4e99b43ebe3468d6efb2276ba3669aff6ffc0f4c6ae4ae2e5d74c3c0af97dce17147688dda89e734b56944a2,
    ),
    #   BADA55 curve from the https://bada55.cr.yp.to/bada55-20150927.pdf
    Weierstrass(
        name="other/BADA55-VPR2-224",
        p=0xffffffffffffffffffffffffffffffff000000000000000000000001,
        # original a and b should (implicitly) be reduced modulo p
        a=0xcba97952a45146601a34bef5b927d70fe1f0f34f8c992bf5a8c5991c,
#        a=0x8f0ff20e1e3cf4905d492e04110683948bfc236790bbb59e6e6b33f24f348ed2e16c64ee79f9fd27e9a367ff6415b41189e4fb6bada555455dc44c4f87011eef,
        b=0xe4f459b931bd2fe7ee2db9d01d18081a0be0c0039e41f26c7995bd7c,
#        b=0xe85067a95547e30661c854a43ed80f36289043ffc73da78a97e37fb96a2717009088656b948865a660ff3959330d8a1ca1e4de31b7b7d496a4cde555e57d05c,
    ),
    #   Tom-256 curve from https://eprint.iacr.org/2021/1183.pdf
    Weierstrass(
        name="other/Tom-256",
        p=0xffffffff0000000100000000000000017e72b42b30e7317793135661b1c4b117,
        a=0xffffffff0000000100000000000000017e72b42b30e7317793135661b1c4b114,
        b=0xb441071b12f4a0366fb552f8e21ed4ac36b06aceeb354224863e60f20219fc56,
    ),
    #   Tom-384 curve from https://eprint.iacr.org/2021/1183.pdf
    Weierstrass(
        name="other/Tom-384",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffeaf5f689f8669fb41b08d5f5edffd26599c434bbd978917c5,
        a=0x821dfdc940e7f074ac481f8b2870c48962cce56abd72dfc42813a944cea15df78dc0a2d97fbf031ed26c9076826940ba,
        b=0x9b5b584b655fdcb087d37f8c4fee893c0499223db5e004c674ea0dee48a4ec0c9e9f684099f2a51c62a2cce400cb1e4b,
    ),
    #   Tom-521 curve from https://eprint.iacr.org/2021/1183.pdf
    Weierstrass(
        name="other/Tom-521",
        p=0x200000000000000000000000000000000000000000000000000000000000000002c54be78524c33584f734a266748b2063accf5028e6778dc5056476d0690853249,
        a=0xef6432c21701cc48c63fb9263e14ba76d4a94ba14d173b134e3032b0e2e543180eb6725125992a7d00162a5f57d21918b0766364eeb53c53bb12f405dac1d527e2,
        b=0x3cbc65d1e0245d79703b18e9aaea1ac6d67f87a2cd4bd84b9e6df6a45a979c481825ca5a857270fc890352f9fac7fd6020deaabb28d099718f0f77a4eec222871d,
    ),


    ########    Microsoft Nothing Up My Sleeve (NUMS) curves from: <https://eprint.iacr.org/2014/130> and <https://tools.ietf.org/html/draft-black-numscurves-02>

    Weierstrass(
        name="nums/numsp256d1",
        p=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff43,
        a=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff40,
        b=0x25581,
    ),
    Edwards(
        name="nums/numsp256t1",
        p=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff43,
        d=0x3bee,
        t=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff42,
    ),
    Weierstrass(
        name="nums/numsp384d1",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffec3,
        a=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffec0,
        b=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff77bb,
    ),
    Edwards(
        name="nums/numsp384t1",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffec3,
        d=0x5158a,
        t=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffec2,
    ),
    Weierstrass(
        name="nums/numsp512d1",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdc7,
        a=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdc4,
        b=0x1d99b,
    ),
    Edwards(
        name="nums/numsp512t1",
        p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdc7,
        d=0x9baa8,
        t=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdc6,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-256-mont",
        p=0xffa7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0x350a,
        t=0xffa7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-254-mont",
        p=0x3f80ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0x367b,
        t=0x3f80fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-255-mers",
        p=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd03,
        d=0xea97,
        t=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd02,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-384-mont",
        p=0xb0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0x6f17,
        t=0xb0fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-382-mont",
        p=0x3ffaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0xaf381,
        t=0x3ffafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-383-mers",
        p=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5b,
        d=0x7fed6,
        t=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5a,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-512-mont",
        p=0xfe14ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0x12a9c,
        t=0xfe14fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-510-mont",
        p=0x3eddffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        d=0x8da1e,
        t=0x3eddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Edwards(
        name="nums/ed-511-mers",
        p=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe1f,
        d=0x10bf7d,
        t=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe1e,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-256-mont",
        p=0xffa7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        a=0xffa7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc,
        b=0x14e6a,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-254-mont",
        p=0x3f80ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        a=0x3f80fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc,
        b=-0x2f72,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-255-mers",
        p=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd03,
        a=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd00,
        b=-0x51bd,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-384-mont",
        p=0xb0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        a=0xb0fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc,
        b=0x6c96,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-382-mont",
        p=0x3ffaffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        a=0x3ffafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc,
        b=-0x20a72,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-383-mers",
        p=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5b,
        a=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe58,
        b=0x17dbc,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-512-mont",
        p=0xfe14ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        a=0xfe14fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc,
        b=0x185ed,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-510-mont",
        p=0x3eddffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff,
        a=0x3eddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc,
        b=0x988d,
    ),
    #   Curve from https://eprint.iacr.org/2014/130.pdf. No generator present.
    Weierstrass(
        name="nums/w-511-mers",
        p=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe1f,
        a=0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe1c,
        b=0x879da,
    ),


    ########    MNT (Miyaji, Nakabayashi, and Takano curves) example curves from: New explicit conditions of elliptic curve traces for FR-reduction - https://dspace.jaist.ac.jp/dspace/bitstream/10119/4432/1/73-48.pdf.

    Weierstrass(
        name="mnt/mnt1",
        p=0x26dccacc5041939206cf2b7dec50950e3c9fa4827af,
        a=0x22ffbb20cc052993fa27dc507800b624c650e4ff3d2,
        b=0x1c7be6fa8da953b5624efc72406af7fa77499803d08,
    ),
    Weierstrass(
        name="mnt/mnt2/1",
        p=0x5affffffffffff4b46081000000059bb1bf600b7,
        a=0x3dd24a7e5c0bdfaccc215e22760469c73ee9d879,
        b=0x478c31a992b294e19f6e4416f958646dddede5e3,
    ),
    Weierstrass(
        name="mnt/mnt2/2",
        p=0x5affffffffffff4b46081000000059bb1bf600b7,
        a=0x07b29491c1a02cd87844f5098d0381f6c45d6523,
        b=0x41cc630bd66ac817d43358b108ad3d214037993c,
    ),
    Weierstrass(
        name="mnt/mnt3/1",
        p=0x8afffffffffffeeb0fa77000000089f0dd49fac7,
        a=0x6d01fd0a017c62075ae999977379867e07f2a6d4,
        b=0x7701535c00fd965341d38bba4cfbdcf9a4651825,
    ),
    Weierstrass(
        name="mnt/mnt3/2",
        p=0x8afffffffffffeeb0fa77000000089f0dd49fac7,
        a=0x5fbe0085bd2b23afcd5b9c7704aeed2bfdbe89e4,
        b=0x3fd4005928c76d1fde3d12fa031f48c7fe7f0698,
    ),
    Weierstrass(
        name="mnt/mnt3/3",
        p=0x8afffffffffffeeb0fa77000000089f0dd49fac7,
        a=0x2ddf23acb05a91bda6ba9c20d7a584aa25075ce0,
        b=0x1f8125c46a31e79fd6cc25298b23ab130cd22b5a,
    ),
    Weierstrass(
        name="mnt/mnt4",
        p=0xa2ffffffffffffffffffffffffc298b00000000000000000000005c866cf,
        a=0x4be28760aa064734852cb4ff51ef2928a7a3cd75087c35cb1433714f7407,
        b=0x329704eb1c042f7858c878aa369f70c5c517de4e05a823dcb8224b8a4d5a,
    ),
    Weierstrass(
        name="mnt/mnt5/1",
        p=0xd2fffffffffffffffffffffffe9058d000000000000000000000a0271007,
        a=0xd149265d4687dcab1f2046e0947e51ac5e8e7f25916d35539d4df2e9017a,
        b=0x489e7783a1f584712bd4f6d48cf2d1ca2c975678936e639083991c5fc369,
    ),
    Weierstrass(
        name="mnt/mnt5/2",
        p=0xd2fffffffffffffffffffffffe9058d000000000000000000000a0271007,
        a=0x26caaced434c5a4c2c9c1b09e0ddc167548a95516e7c81b20702485c9809,
        b=0x6031c89e2cdd91881dbd675beac3f3df8db1b8e0f45301215a01baf56ab3,
    ),
    Weierstrass(
        name="mnt/mnt5/3",
        p=0xd2fffffffffffffffffffffffe9058d000000000000000000000a0271007,
        a=0x44cfc0f3bc92ec82f818b443b564cf25dee3ebae7902e370f9e80283d3bd,
        b=0x2ddfd5f7d30c9daca565cd8278eddf6e9497f27450ac97a0a69aac57e27e,
    ),


    ########    BN (Barreto, Naehrig curves) from: A Family of Implementation-Friendly BN Elliptic Curves - <https://eprint.iacr.org/2010/429.pdf>.

    Weierstrass(
        name="bn/bn158",
        p=0x24240D8241D5445106C8442084001384E0000013,
        a=0x0000000000000000000000000000000000000000,
        b=0x0000000000000000000000000000000000000011,
    ),
    Weierstrass(
        name="bn/bn190",
        p=0x240001B0000948001E60004134005F10005DC0003A800013,
        a=0x000000000000000000000000000000000000000000000000,
        b=0x000000000000000000000000000000000000000000001001,
    ),
    Weierstrass(
        name="bn/bn222",
        p=0x23DC0D7DC02402CDE486F4C00015B5215C0000004C6CE00000000067,
        a=0x00000000000000000000000000000000000000000000000000000000,
        b=0x00000000000000000000000000000000000000000000000000000101,
    ),
    #   Also known as other/Fp254BNb
    Weierstrass(
        name="bn/bn254",
        p=0x2523648240000001BA344D80000000086121000000000013A700000000000013,
        a=0x0000000000000000000000000000000000000000000000000000000000000000,
        b=0x0000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn286",
        p=0x240900D8991B25B0E2CB51DDA534A205391892080A008108000853813800138000000013,
        a=0x000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn318",
        p=0x24009000D800900024075015F015F0075000008F411E808F4000000004E484E4800000000000101B,
        a=0x00000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x00000000000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn350",
        p=0x23FFB80035FFEE24020A01CAFD738EC3F24B475EBC0AD0F6A0530FD78443FDF01A3FF64084000004E0000013,
        a=0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn382",
        p=0x240026400F3D82B2E42DE125B00158405B710818AC00000840046200950400000000001380052E000000000000000013,
        a=0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn414",
        p=0x240024000D7EE23F2823CA035D31B144364C75E59AEFFF60544845142000765EFFF7C0000021138004DFFFFFD900000000000013,
        a=0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn446",
        p=0x2400000000000000002400000002D00000000D800000021C0000001800000000870000000B0400000057C00000015C000000132000000067,
        a=0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101,
    ),
    Weierstrass(
        name="bn/bn478",
        p=0x23FFFFFFFFFFFFFEDFFFFFFFEE0001B3600000006BFFF5DB835FFF5D28085442328002888F96F2944D7DED781430FFD780065FFF010020FFFD900013,
        a=0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn510",
        p=0x2400000000000000003F000000000001B0002958000000000237000C0F0000084000F8100151A400073800242D00001380019440000000000888000000000013,
        a=0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101,
    ),
    Weierstrass(
        name="bn/bn542",
        p=0x2400090000D80009000024000090001B01B1B051090510001B00D8001B0510D8A2084511080008D000090510005110800108138025380001B00000084000001380000013,
        a=0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn574",
        p=0x2400023FFFFB7FFF4C00002400167FFFEE01AEE014423FAEFFFB5C000A200050FFFF2808400041FFFE73FFF7C000210000000000001380004DFFFD90000000000000000000000013,
        a=0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn606",
        p=0x23FFFFFFFFFFFEE00000000000036000000241AFFB7FFFFFF275E0024000001B1440000D94482DF27FFFC9AEDF0000000036512100245142137FFFFFB75D7BD900000000000000246C844E13,
        a=0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002,
    ),
    Weierstrass(
        name="bn/bn638",
        p=0x23FFFFFDC000000D7FFFFFB8000001D3FFFFF942D000165E3FFF94870000D52FFFFDD0E00008DE55C00086520021E55BFFFFF51FFFF4EB800000004C80015ACDFFFFFFFFFFFFECE00000000000000067,
        a=0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        b=0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101,
    ),


    ########    BLS curves. A family of pairing friendly curves, with embedding degree = 12 or 24.

    #   Curve from Zexe paper: https://eprint.iacr.org/2018/962, params taken from: https://eips.ethereum.org/EIPS/eip-2539
    Weierstrass(
        name="bls/BLS12-377",
        p=0x01ae3a4617c510eac63b05c06ca1493b1a22d9f300f5138f1ef3622fba094800170b5d44300000008508c00000000001,
        a=0x00,
        b=0x01,
    ),
    #   Curve from https://electriccoin.co/blog/new-snark-curve/. As used in ZCash.
    Weierstrass(
        name="bls/BLS12-381",
        p=0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab,
        a=0x00,
        b=0x04,
    ),
    #   Curve from https://github.com/relic-toolkit/relic.
    Weierstrass(
        name="bls/BLS12-446",
        p=0x3cdee0fb28c5e535200fc34965aad6400095a4b78a02fe320f75a64bbac71602824e6dc3e23acdee56ee4528c573b5cc311c0026aab0aaab,
        a=0x00,
        b=0x01,
    ),
    #   Curve from https://github.com/relic-toolkit/relic.
    Weierstrass(
        name="bls/BLS12-455",
        p=0x55555955557955572aa00e0f95b49203003f665e3a5b1d56234bd93954fcb314b8b3db9994ace86d1ba6c589556b2aa956aaa00001800002ab,
        a=0x00,
        b=0x0a,
    ),
    #   Curve from https://github.com/relic-toolkit/relic. Also in https://eprint.iacr.org/2012/232.pdf.
    Weierstrass(
        name="bls/BLS12-638",
        p=0x3cb868653d300b3fe80015554dd25db0fc01dcde95d4000000631bbd421715013955555555529c005c75d6c2ab00000000000ac79600d2abaaaaaaaaaaaaaa93eaf3ff000aaaaaaaaaaaaaaabeab000b,
        a=0x00,
        b=0x04,
    ),
    #   Curve from https://github.com/relic-toolkit/relic. Also in https://eprint.iacr.org/2012/232.pdf.
    Weierstrass(
        name="bls/BLS24-477",
        p=0x167278fac63bd5b007ebb8f693a2ab3dbd9f92cf437c399d928e94bfe9a04a009fda9e8cf9226901de62aea9dcea48bf1a0ebbf8860a5e7ad000152b,
        a=0x00,
        b=0x04,
    ),
    #   Curve from https://ethresear.ch/t/introducing-bandersnatch-a-fast-elliptic-curve-built-over-the-bls12-381-scalar-field/9957
    Edwards(
        name="bls/Bandersnatch",
        p=0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001,
        d=0x6389c12633c267cbc66e3bf86be3b6d8cb66677177e54f92b369f2f5188d58e7,
        t=-0x05,
    ),


    ########    Curves used in the Chinese ShangMi commercial standards SM2 and SM9

    # Curve from the GMT 0003.5-2012 SM2 standard
    Weierstrass(
        name="sca/SM2",
        p=0xfffffffeffffffffffffffffffffffffffffffff00000000ffffffffffffffff,
        a=0xfffffffeffffffffffffffffffffffffffffffff00000000fffffffffffffffc,
        b=0x28e9fa9e9d9f5e344d5a9e4bcf6509a7f39789f515ab8f92ddbcbd414d940e93,
    ),
    # Two unknown curves mentioned in the GMT 0003.1-2012 SM2 standard
    Weierstrass(
        name="sca/SM2-unknown-192",
        p=0xbdb6f4fe3e8b1d9e0da8c0d46f4c318cefe4afe3b6b8551f,
        a=0xbb8e5e8fbc115e139fe6a814fe48aaa6f0ada1aa5df91985,
        b=0x1854bebdc31b21b7aefc80ab0ecd10d5b1b3308e6dbf11c1,
    ),
    Weierstrass(
        name="sca/SM2-unknown-256",
        p=0x8542d69e4c044f18e8b92435bf6ff7de457283915c45517d722edb8b08f1dfc3,
        a=0x787968b4fa32c3fd2417842e73bbfeff2f3c848b6831d7e0ec65228b3937e498,
        b=0x63e4c6d3b23b0c849cf84241484bfe48f61d59a5b16ba06e6e12d1da27c5249a,
    ),
    # Curve from SM9: a pairing-friendly curve for Identity-Based cryptography
    Weierstrass(
        name="sca/SM9",
        p=0xb640000002a3a6f1d603ab4ff58ec74521f2934b1a7aeedbe56f9b27e351457d,
        a=0x00,
        b=0x05,
    ),


    ########    Curves mentioned in other RFCs

    # Curve defined in RFC6509, for the Sakai-Kasahara Key Exchange; related to SM9?
    Weierstrass(
        name="rfc6509/SAKKE",
        p=0x997abb1f0a563fda65c61198dad0657a416c0ce19cb48261be9ae358b3e01a2ef40aab27e2fc0f1b228730d531a59cb0e791b39ff7c88a19356d27f4a666a6d0e26c6487326b4cd4512ac5cd65681ce1b6aff4a831852a82a7cf3c521c3c09aa9f94d6af56971f1ffce3e82389857db080c5df10ac7ace87666d807afea85feb,
        a=-3,
        b=0,
    ),
]

KNOWN_PRIMES = [curve.p for curve in KNOWN_CURVES]
