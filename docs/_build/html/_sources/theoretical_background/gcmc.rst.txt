=============================================
Grand-Canonical Monte Carlo (GCMC) Simulation
=============================================


Brief introduction about GCMC simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Grand-Canonical ensemble, the volume :math:`V`, the temperature :math:`T`, and chemical potential :math:`\mu` establish the thermodynamical equilibrium between the system and a bulk reservoir.
The Metropolis Monte Carlo method can be used within the Grand-Canonical ensemble to simulate the adsorption of molecules on nanoporous materials.

The configurational space can be evaluated throughout a set of random movements such as insertion, deletion, translation, and rotation. The acceptance probability rule for these movements to ensure a Boltzmann distribution of the states are:


- Insertion: A molecule is inserted into a random position

.. math::

   P_{acc}(N \rightarrow N+1) = \min \left[ 1, \frac{\beta f V}{N + 1} e^{-\beta \Delta U}\right]

            
- Deletion: A random molecule is deleted from the system

.. math::

   P_{acc}(N \rightarrow N - 1) = \min \left[ 1, \frac{N}{\beta f V} e^{-\beta \Delta U}\right]


- Rotation: A random molecule is rotated by a quaternion  $\mathbf{q}$

.. math::

   P_{acc}(S \rightarrow S'_\mathbf{q}) = \min \left[ 1, e^{-\beta \Delta U}\right]


- Translation: A random molecule is translated by a random vector $\mathbf{\vec{r}}$

.. math::

   P_{acc}(S \rightarrow S'_\mathbf{\vec{r}}) = \min \left[ 1, e^{-\beta \Delta U}\right]


- Reinsertion: A random molecule is deleted and inserted into a new random position

.. math::
   
   P_{acc}(S \rightarrow S') = \min \left[ 1, e^{-\beta \Delta U}\right]

            

where :math:`\Delta U` represents the difference on the potential energy between the old and new state, :math:`N` the number of adsorbate particles on the system, :math:`\beta = 1 / k_B T` the reciprocal thermodynamic temperature calculated based on the Boltzmann constant :math:`k_B` and the absolute temperature :math:`T`. More details on the implementation of these movements are provided on Supporting Information.
        
The fugacity of the adsorbing species, :math:`f`, is related to the chemical potential of the ideal reservoir as

.. math::
   
   f = \frac{q_{rot}}{\beta \Lambda ^ 3} e^{\beta \mu}, \quad  \Lambda = \left( \frac{\beta h^2}{2 \pi m}\right)^\frac{1}{2}


where :math:`q_{rot}` is the rotational partition function for a single and rigid molecule, and :math:`\Lambda` the thermal de Broglie wavelength, :math:`h` is the planks constant, and :math:`m` is the mass of the adsorbate molecule.

The Grand-Canonical ensemble can be specified in a more convenient way as a function of the pressure :math:`P`, instead of the chemical potential, by converting the pressure to fugacity using a fugacity coefficient :math:`\phi` calculated based on an empirical equation of state (EOS), such as the Pen-Robinson, for example.\autocite{peng1976new}

The enthalpy of adsorption :math:`\Delta H_{\text{ads}}` (or the heat of adsorption :math:`q = -\Delta H_{\text{ads}}`) can be calculated as

.. math::

   \Delta H_{\text{ads}} = \left( \frac{\partial U}{\partial N}\right)_{V,T} - \langle U_g \rangle - \langle U_h \rangle - RT


where :math:`U` represents the total energy of the system (framework and adsorbed molecules), :math:`\langle U_g \rangle` is the average energy of a single molecule in the gas phase, :math:`\langle U_h \rangle` is the average energy of the framework (host) system, :math:`R` is the universal gas constant and :math:`T` the temperature of the simulation.\autocite{vlugt2008computing, torres2017behavior}

The energy/particle fluctuations in the grand-canonical ensemble can be used to express the absolute differential energy (:math:`\partial U/\partial N`) as a function of the averages of the total energy and number of molecules \autocite{nicholson1982computer, myers2002thermodynamics, poursaeidesfahani2016computation} for a single component system as

.. math::
   \left( \frac{\partial U}{\partial N}\right)_{V,T} = \frac{\left( \frac{\partial U}{\partial \mu}\right)_{V,T}}{\left( \frac{\partial N}{\partial \mu}\right)_{V,T}} = \frac{\langle U \cdot N\rangle_\mu - \langle U \rangle_\mu \langle N\rangle_\mu}{\langle N^2\rangle_\mu - \langle N\rangle^2_\mu }


where :math:`\langle \dots \rangle_\mu` represents the averages in the grand-canonical ensemble (:math:`\mu` is the chemical potential), :math:`N` is the number of adsorbates on the simulation box, and :math:`U` is the total potential energy.

In simulations where both the framework structure and the adsorbed molecules have rigid bonds, the total internal energy of the host and the isolated molecule, :math:`U_h = U_g = 0`. Therefore, the enthalpy of adsorption can be calculated as  

.. math::
   
   \Delta H = \frac{\langle U \cdot N\rangle_\mu - \langle U \rangle_\mu \langle N\rangle_\mu}{\langle N^2\rangle_\mu - \langle N\rangle^2_\mu } - RT

This approximation is widely used in GCMC simulations and it has been shown that for non-flexible frameworks it has only a small influence on the adsorption at low loading.