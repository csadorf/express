import numpy as np

from tests.unit import UnitTestBase
from express.properties.non_scalar.bandgaps import BandGaps

BAND_GAPS = {
    "values": [
        {
            "units": "eV",
            "kpointConduction": [
                0.0,
                0.0,
                0.0
            ],
            "type": "direct",
            "value": 2.4420081600000003,
            "kpointValence": [
                0.0,
                0.0,
                0.0
            ]
        },
        {
            "units": "eV",
            "kpointConduction": [
                -7.19668434e-17,
                -0.944862979,
                -0.944862979
            ],
            "type": "indirect",
            "value": 0.65023092000000027,
            "kpointValence": [
                0.0,
                0.0,
                0.0
            ]
        }
    ],
    "name": "band_gaps"
}


class BasisTest(UnitTestBase):
    def setUp(self):
        super(BasisTest, self).setUp()

    def tearDown(self):
        super(BasisTest, self).setUp()

    def test_band_gaps(self):
        raw_data = {
            "eigenvalues_at_kpoints": [
                {
                    "eigenvalues": [
                        {
                            "energies": [
                                -5.5990059,
                                6.26931638,
                                6.26931998,
                                6.26934533,
                                8.71135349,
                                8.71135587,
                                8.71135838,
                                9.41550185
                            ],
                            "occupations": [
                                1.0,
                                0.9999999999990231,
                                0.9999999999990226,
                                0.9999999999990189,
                                0.0,
                                0.0,
                                0.0,
                                0.0
                            ],
                            "spin": 0.5
                        }
                    ],
                    "kpoint": [
                        0,
                        0,
                        0
                    ],
                    "weight": 0.25
                },
                {
                    "eigenvalues": [
                        {
                            "energies": [
                                -3.30219959,
                                -0.66503974,
                                5.06084876,
                                5.0608702,
                                7.69496909,
                                9.49274379,
                                9.49275618,
                                13.89571002
                            ],
                            "occupations": [
                                1.0,
                                1.0,
                                1.0,
                                1.0,
                                2.191035831088034E-113,
                                0.0,
                                0.0,
                                0.0
                            ],
                            "spin": 0.5
                        }
                    ],
                    "kpoint": [
                        0.28867514,
                        0.20412412,
                        -0.49999997
                    ],
                    "weight": 0.5
                },
                {
                    "eigenvalues": [
                        {
                            "energies": [
                                -3.30220019,
                                -0.6650363,
                                5.06084821,
                                5.06086954,
                                7.69496137,
                                9.49273868,
                                9.49275401,
                                13.89571914
                            ],
                            "occupations": [
                                1.0,
                                1.0,
                                1.0,
                                1.0,
                                2.199010455040857E-113,
                                0.0,
                                0.0,
                                0.0
                            ],
                            "spin": 0.5
                        }
                    ],
                    "kpoint": [
                        0,
                        -0.61237246,
                        0
                    ],
                    "weight": 0.25
                },
                {
                    "eigenvalues": [
                        {
                            "energies": [
                                -1.51073812,
                                -1.51072293,
                                3.41069883,
                                3.41070722,
                                6.91957625,
                                6.91958498,
                                16.14829919,
                                16.1483028
                            ],
                            "occupations": [
                                1.0,
                                1.0,
                                1.0,
                                1.0,
                                4.579502952592552E-11,
                                4.573994582634171E-11,
                                0.0,
                                0.0
                            ],
                            "spin": 0.5
                        }
                    ],
                    "kpoint": [
                        0.28867514,
                        -0.40824834,
                        -0.49999997
                    ],
                    "weight": 0.5
                },
                {
                    "eigenvalues": [
                        {
                            "energies": [
                                -3.30221054,
                                -0.66501391,
                                5.06085301,
                                5.06085524,
                                7.69495606,
                                9.49273487,
                                9.49273798,
                                13.89571883
                            ],
                            "occupations": [
                                1.0,
                                1.0,
                                1.0,
                                1.0,
                                2.204511701557367E-113,
                                0.0,
                                0.0,
                                0.0
                            ],
                            "spin": 0.5
                        }
                    ],
                    "kpoint": [
                        -0.57735028,
                        0.20412421,
                        0
                    ],
                    "weight": 0.25
                },
                {
                    "eigenvalues": [
                        {
                            "energies": [
                                -1.51074222,
                                -1.5107195,
                                3.41069761,
                                3.41071003,
                                6.91957636,
                                6.91958424,
                                16.14830113,
                                16.14830247
                            ],
                            "occupations": [
                                1.0,
                                1.0,
                                1.0,
                                1.0,
                                4.579432877486831E-11,
                                4.574465149035778E-11,
                                0.0,
                                0.0
                            ],
                            "spin": 0.5
                        }
                    ],
                    "kpoint": [
                        -0.57735028,
                        -0.40824824,
                        0
                    ],
                    "weight": 0.25
                }
            ],
            "nspins": 1,
            "ibz_k_points": np.array([
                [0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
                [-7.19668434e-17, -1.27477992e-16, -9.44862979e-01],
                [0.00000000e+00, -9.44862979e-01, 0.00000000e+00],
                [-7.19668434e-17, -9.44862979e-01, -9.44862979e-01],
                [-9.44862979e-01, 1.21698145e-16, 0.00000000e+00],
                [-9.44862979e-01, -9.44862979e-01, 0.00000000e+00]
            ]),
            "fermi_energy": 6.6,
            "band_gaps_direct": None,
            "band_gaps_indirect": None
        }
        property_ = BandGaps("band_gaps", raw_data=raw_data)
        self.assertDeepAlmostEqual(property_.serialize_and_validate(), BAND_GAPS)
