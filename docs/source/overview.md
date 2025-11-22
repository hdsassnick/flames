# Overview

`FLAMES` is a computational-chemistry toolkit focused on simulation adsorption by techiniques such as Grand Canonical Monte Carlo (GCMC), Widom insertions, and molecular dynamics (MD). The main motivation of its development is the integration with machine-learning potentials and other methods for calculating the energy such tight-binding and DFT. It leverages ASE as its core structure and calculator interface and provides `simulators` that can run GCMC, Widom, and MD simulations with various move types, thermostats, and barostats.

## Main capabilities

- Grand Canonical Monte Carlo (GCMC): insertion/deletion/movement moves with energy evaluations through ASE calculators.
- Widom insertion method for Henry coefficients and adsorption enthalpy.
- MD integrations and thermostats/barostats for combined MD+GCMC workflows.
- Support for classical force-fields (LJ, UFF, TraPPE) and machine-learning potentials (MACE, DeepMD) via ASE calculator adapters.
- Utilities for geometry optimization, overlap detection, and thermodynamic conversions.

## Design & conventions

- Structural objects are `ase.Atoms` throughout the codebase.
- Energies use ASE defaults (eV), distances in Angstrom, temperatures in Kelvin, and pressure in bar.
- Functions and classes use type hints; calculators conform to ASE `Calculator` interface with energies in eV and forces in eV/Angstrom.
- Randomness: `numpy.random` is used. The `Generator` from `numpy.random` is used for simulations so every movement can be made deterministic by setting one single random seed.
- The simulations can use `tqdm` for progress bars and support both console and file logging.

## Top-level layout of the repository

- `flames/` : Main package containing simulation code and utilities.
- `examples/` : Example scripts (Widom, rigid GCMC, MD+GCMC, calculators examples).
- `docs/` : Sphinx documentation sources and built docs.
- `tests/` : Unit tests (pytest).
- `environment.yml`, `pyproject.toml` : Environment / packaging metadata.
- `data/` (inside `flames/`) : molecular structures and force-field parameter files.

## Key modules (in `flames/`)

- `gcmc.py` : Implements the GCMC class and main Grand Canonical Monte Carlo routines. Handles insertion, deletion, and move proposals; uses Boltzmann acceptance criteria and chemical potential/fugacity coupling.

- `widom.py` : Widom insertion class/tool for computing Henry coefficients and adsorption enthalpies via test-particle insertions.

- `ase_utils.py` : Helpers for ASE integration and MD thermostats/barostats. Includes `nPT_Berendsen`, `nPT_NoseHoover`, `nVT_Berendsen`, and structural relaxation utilities such as `crystalOptimization`.

- `lj.py` : Lennard-Jones interaction utilities and potential functions for classical force-field interactions.

- `utilities.py` : Core utility functions used across simulations:
  - `random_position`, `random_rotation` — Monte Carlo move generators.
  - `vdw_overlap` — overlap detection for molecule insertions.
  - `enthalpy_of_adsorption` — thermodynamic property calculations.
  - vdw radii and support routines used by insertion logic.

- `calculators.py` : Adapters and helpers for using calculators (classical and ML). Ensures compatibility with ASE calculator interface (e.g., MACE, LAMMPS, CP2K wrappers used in examples).

- `base_simulator.py` : Shared simulation scaffolding and abstractions used by GCMC/Widom/MD workflows.

- `operations.py` : Higher-level operations combining moves, analysis, and bookkeeping for simulation workflows.

- `logger.py` : Logging helpers and file output utilities used by simulations to track progress and results.

- `exceptions.py` : Domain-specific exception classes for robust error handling in simulation flows.

- `eos.py` : Equation-of-state utilities and thermodynamic conversions used for fugacity/chemical-potential handling.

- `version.py` : Package version information.

## Data and examples

- `flames/data/` contains sample molecule coordinates (e.g., `co2.xyz`, `H2O.xyz`), charge files, and force-field parameter JSONs (e.g., `TraPPE_lj_params.json`, `UFF_lj_params.json`).
- `examples/` includes runnable small scripts demonstrating typical workflows:
  - `Basic/1-Widom/run_widom.py`
  - `Basic/2-Rigid_GCMC/run_GCMC.py`
  - `Calculators/` shows classical and ML calculator usage (DeepMD, CP2K, etc.).

## Testing and docs

- Tests: run with `pytest` (examples in `tests/`, e.g., `utilities_test.py`).
- Documentation: Sphinx sources in `docs/`. Build docs with `make html` in the `docs/` directory.

Quick commands:

```bash
# install (editable) with developer deps
pip install -e ".[dev]"

# run tests
pytest -q

# build docs
( cd docs && make html )
```

## Developer notes

- Follow existing style and patterns when adding modules — keep changes minimal and focused.
- Add unit tests in `tests/` for any new utility or simulator behavior.
- When adding expensive calculator integrations, prefer mocking in tests.
