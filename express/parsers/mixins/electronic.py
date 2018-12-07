from abc import abstractmethod


class ElectronicDataMixin(object):
    """
    Defines electronic interfaces.

    Note:
        THE FORMAT OF DATA STRUCTURE RETURNED MUST BE PRESERVED IN IMPLEMENTATION.
    """

    @abstractmethod
    def total_energy(self):
        """
        Returns total energy.

        Returns:
             float

        Example:
             -19.00890332
        """
        pass

    @abstractmethod
    def fermi_energy(self):
        """
        Returns fermi energy.

        Returns:
             float

        Example:
             6.6078556811104292
        """
        pass

    @abstractmethod
    def nspins(self):
        """
        Returns the number of spins.

        Returns:
             int

        Example:
             2
        """
        pass

    @abstractmethod
    def eigenvalues_at_kpoints(self):
        """
        Returns eigenvalues for all kpoints.

        Returns:
             list[dict]

        Example:
            [
                {
                    'kpoint': [-0.5, 0.5, 0.5],
                    'weight': 9.5238095E-002,
                    'eigenvalues': [
                        {
                            'energies': [-1.4498446E-001, ..., 4.6507387E-001],
                            'occupations': [1, ... , 0],
                            'spin': 0.5
                        }
                    ]
                },
                ...
            ]
        """
        pass

    @abstractmethod
    def dos(self):
        """
        Returns density of states.

        Returns:
            dict

        Example:
            {
                "energy": [
                    -6.005000114440918,
                    -5.954999923706055,
                    -5.90500020980835
                ],
                "partial": [
                    [
                        1.6499999980444308E-17,
                        1.3080000562020133E-16,
                        7.899999954541818E-16
                    ]
                ],
                "partial_info": [
                    {
                        "electronicState": "2py",
                        "element": "Si"
                    },
                    {
                        "electronicState": "2px",
                        "element": "Si"
                    },
                    {
                        "electronicState": "1s",
                        "element": "Si"
                    },
                    {
                        "electronicState": "2pz",
                        "element": "Si"
                    }
                ],
                "total": [
                    0.00012799999967683107,
                    0.0010100000072270632,
                    0.006130000110715628
                ]
            }
        """
        pass

    @abstractmethod
    def convergence_electronic(self):
        """
        Extracts convergence electronic.

        Returns:
             list[float]

        Example:
            [
                1.4018213061907816,
                0.5939946985677435,
                0.007003124785903934,
                0.0010198831091687887,
                4.2041606287774244e-05,
                7.619190783544846e-06
            ]
        """
        pass

    @abstractmethod
    def total_energy_contributions(self):
        """
        Extracts total energy contributions.

        Returns:
            dict

        Example:
            {
                "harrisFoulkes": {
                    "name": "harris_foulkes",
                    "value": -258.6293887585482
                },
                "ewald": {
                    "name": "ewald",
                    "value": -226.94126871332813
                },
                "oneElectron": {
                    "name": "one_electron",
                    "value": 68.65366986552296
                },
                "smearing": {
                    "name": "smearing",
                    "value": -0.0
                },
                "hartree": {
                    "name": "hartree",
                    "value": 17.72349166363712
                },
                "exchangeCorrelation": {
                    "name": "exchange_correlation",
                    "value": -118.06528742483022
                }
            }
        }
        """
        pass

    @abstractmethod
    def reaction_energies(self):
        """
        Returns reaction energies.

        Returns:
             list[float]

        Example:
             [
                0.0,
                0.0336637211,
                0.1282952413,
                0.2032895454,
                0.1282953846,
                0.0336637671,
                -5.3E-9
            ]
        """
        pass
