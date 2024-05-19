import subprocess


def test_no_args():
    p = subprocess.run("echec",
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       shell=True,
                       encoding="utf_8")
    assert p.returncode == 97
    assert p.stdout.lower().startswith("usage:")


def test_odd_number_of_args():
    p = subprocess.run("echec 1 2 3 4 5",
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT,
                       shell=True,
                       encoding="utf_8")
    assert p.returncode == 97
    assert p.stdout.lower().startswith("usage:")


def test_integer_point():
    p = subprocess.run(
        args=" ".join(
            ["echec",
             "0x188DA80EB03090F67CBF20EB43A18800F4FF0AFD82FF1012",
             "0x7192B95FFC8DA78631011ED6B24CDD573F977A11E794811"]),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf_8",
        shell=True,
    )
    assert p.returncode == 0
    assert p.stderr == ""
    assert p.stdout.find("nist/P-192") >= 0


def test_string_point():
    p = subprocess.run(
        args=["echec",
              "6B17D1F2E12C4247F8BCE6E563A440F2"
                "77037D812DEB33A0F4A13945D898C296",
              "4FE342E2FE1A7F9B8EE7EB4A7C0F9E16"
                "2BCE33576B315ECECBB6406837BF51F5"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf_8",
    )
    assert p.returncode == 0
    assert p.stderr == ""
    assert p.stdout.find("nist/P-256") >= 0


def test_xcoords():
    p = subprocess.run(
        args=["echec",
              "--xcoords",
              "0x9",
              "e6db6867583030db3594c1a424b15f7c"
                "726624ec26b3353b10a903a6d0ab1c4c",
              "c3da55379de9c6908e94ea4df28d084f"
                "32eccf03491c71f754b4075577a28552",
              "422c8e7a6227d7bca1350b3e2bb7279f"
                "7897b87bb6854b783c60e80311ae3079",
              "684cf59ba83309552800ef566f2f4d3c"
                "1c3887c49360e3875f2eb94d99532c51",
              "7c3911e0ab2586fd864497297e575e6f"
                "3bc601c0883c30df5f4dd2d24f665424",
              "8520f0098930a754748b7ddcb43ef75a"
                "0dbf3a0d26381af4eba4a98eaa9b4e6a",
              "de9edb7d7b7dc1b4d35b61c2ece43537"
                "3f8343c85b78674dadfc7e146f882b4f",
              "4a5d9d5ba4ce2de1728e3bf480350f25"
                "e07e21c947d19e3376f09b3c1e161742"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf_8",
    )
    assert p.returncode == 0
    assert p.stderr == ""
    assert p.stdout.find("other/Curve25519") >= 0


def test_unknown_curve():
    p = subprocess.run(
        args=["echec",
              "7c3fbf0ee39cd305da9b83186801f8acdf8b9a8458b29981"
                "d1f930fea56c952db87e8a59a4c59e4fa7762d93a473bac5",
              "6782558937d9d14100699dd9e4d4449a97a143c664aecf5c"
                "c03e6c250a26ac26e8d4fbc89435e6bff27be4cc15e4a720",
              "7ad3cf2218d5ea17ca55f26d90f5a6239b486ad600ed72d7"
                "b3861e4f5c38ca491eb929b8a4226b0803187d7ec405b45d",
              "12af7efa3022b998f987229b2ad02bebb19dc0f672b85bad"
                "92ae6476e546be063c1ae5f7ea3ff533b54e5d364d4d92bd",
              "28c8fa34d67b9985cfdb592b70b3aa7077e87a5100406a5b"
                "f7f7f5c4a0a159051119b8de4c8b51739200c66da56a90f1",
              "40e64279565d5f5ab2aa4db4374f0ef49a3e0611e3ae80bb"
                "b9fc159a7a71e998b7e4c6f88c99e7fa23b41c50dc1c153b",
              "09c50f67faef4f3d0f26f54d573852857acc7a0673a8d577"
                "41477d0a792131a989daeeb1825c23eec2390b86b0becaa5",
              "635cd2174bb44fdf4f895008b6cdefbbfcb22508800fec24"
                "6339dc8d0f4dec008bfe4b798d4ac12d5fbc4d802c6dc8f8"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf_8",
    )
    assert p.returncode == 0
    assert p.stderr == ""
    assert p.stdout.find("other/M-383") >= 0


def test_no_results():
    p = subprocess.run(
        args=["echec",
              "0x290b68edf9429f0072ee7db616db7058"
                "150c9ef9e43170ade3a73ef9505da9fd",
              "0xeeff1fee1574aa1b6259fd72edb5ecc1"
                "90a8bb56d8cb5669f667e07897828882",
              "0x4274904abefccec99ca6192e97b87b70"
                "cfee1093340267f446c789b8d75312f3",
              "0x2505eb8282c57351d2a6ab7e8fd9046b"
                "a620ffe08c793a8e3535d97670a69d6f",
              "0x97f69cfdfd11d022934ca4c082fac3db"
                "9b99796d828c617a6243591f32ad2225",
              "0x368ca25b79e95a4d743e8822b36b89d2"
                "403b2fb1ce176bd5734a0fb959a04056",
              "0x5ab52fdecfa048eef4cbb0871de9499f"
                "51b51ef6dec1b15a0d6d0f298d9ea62f",
              "0x473807637cc1bed7bf90354c71546b78"
                "1722d6c1b58844df30a6bf6c57ecbc4d"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf_8",
    )
    assert p.returncode == 1
    assert p.stdout == "No curves found\n"
