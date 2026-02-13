import json
import os

import numpy as np
from ase.io import read
from mace.calculators import MACECalculator

from flames import VERSION
from flames.tmmc import TMMC

MOFS_PATH = os.path.dirname(__file__) + "/mofs/"
ADSORBATES_PATH = os.path.dirname(__file__) + "/adsorbates/"
MODELS_PATH = os.path.dirname(__file__) + "/models/"


# -----------------------------
# SIMPLE TMMC RUN AND RESTART
# -----------------------------
def test_tmmc_run(tmpdir):
    vdw_radii = [0.0, 0.38, 2.5, 0.86, 0.53, 1.01, 0.88, 0.86, 0.89, 0.82, 2.5, 1.15, 1.28, 1.53]
    ins_energy_list = [
        0.060006250000014916,
        0.9857875000000149,
        -0.20171249999998508,
        0.3256312500000149,
        1.509225000000015,
    ]
    del_energy_list = [
        0.5649937499983935,
        0.7173374999983935,
        0.9517124999983935,
        0.5649937499983935,
        0.7173374999983935,
    ]
    ref_results = {
        "simulation": {
            "code_version": VERSION,
            "random_seed": 10,
            "temperature_K": 298.15,
            "n_steps": 5,
        }
    }
    framework = read(MOFS_PATH + "MOF-303_5xH2O.xsf")
    adsorbate = read(ADSORBATES_PATH + "H2O.xyz")
    model = MACECalculator(
        model_paths=MODELS_PATH + "MOF-303_mace.model", device="cpu", default_dtype="float32"
    )
    tmmc = TMMC(
        model=model,
        framework_atoms=framework,
        adsorbate_atoms=adsorbate,
        temperature=298.15,
        pressure=1e5,
        device="cpu",
        vdw_radii=vdw_radii,
        vdw_factor=1.15,
        save_frequency=1,
        output_folder=tmpdir,
        random_seed=10,
    )
    tmmc.set_adsorbate(adsorbate, n_adsorbates=5, adsorbate_energy=adsorbate.info["total_energy"])

    assert abs(tmmc.adsorbate_energy - adsorbate.info["total_energy"]) < 1e-12
    assert tmmc.n_adsorbate_atoms == 3
    assert tmmc.n_adsorbates == 5

    tmmc.run(5)
    np.testing.assert_array_equal(tmmc.total_ins_energy_list, ins_energy_list)
    np.testing.assert_array_equal(tmmc.total_del_energy_list, del_energy_list)
    np.testing.assert_array_equal(tmmc.volume_list, [framework.get_volume()] * 5)
    np.testing.assert_array_equal(np.load(str(tmpdir) + "/ins_ernergy_0005.npy"), ins_energy_list)
    np.testing.assert_array_equal(np.load(str(tmpdir) + "/del_ernergy_0005.npy"), del_energy_list)
    np.testing.assert_array_equal(
        np.load(str(tmpdir) + "/volume_0005.npy"), [framework.get_volume()] * 5
    )

    tmmc.save_results()
    results = json.load(open(str(tmpdir) + "/results_298.15_0005.json"))
    results["simulation"].pop("enlapsed_time_hours")
    assert results == ref_results

    tmmc = TMMC(
        model=model,
        framework_atoms=framework,
        adsorbate_atoms=adsorbate,
        temperature=298.15,
        pressure=1e5,
        device="cpu",
        vdw_radii=vdw_radii,
        vdw_factor=1.15,
        save_frequency=1,
        output_folder=tmpdir,
        random_seed=10,
    )
    tmmc.set_adsorbate(adsorbate, n_adsorbates=5, adsorbate_energy=adsorbate.info["total_energy"])
    tmmc.restart()
    assert tmmc.base_iteration == 5
    np.testing.assert_array_equal(tmmc.total_ins_energy_list, ins_energy_list)
    np.testing.assert_array_equal(tmmc.total_del_energy_list, del_energy_list)
    np.testing.assert_array_equal(tmmc.volume_list, [framework.get_volume()] * 5)
    np.testing.assert_array_equal(np.load(str(tmpdir) + "/ins_ernergy_0005.npy"), ins_energy_list)
    np.testing.assert_array_equal(np.load(str(tmpdir) + "/del_ernergy_0005.npy"), del_energy_list)
    np.testing.assert_array_equal(
        np.load(str(tmpdir) + "/volume_0005.npy"), [framework.get_volume()] * 5
    )
