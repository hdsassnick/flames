===============================================
Transition Matrix Monte Carlo (TMMC) Simulation
===============================================


Brief introduction about TMMC simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Flat-histogram schemes, such as the transition matrix Monte Carlo (TMMC) method, aim to determine the macrostate probability distribution (MPD) as the centerpiece from which to derive all ensemble properties.

To do so, each transition from one macrostate with :math:`N` molecules to a neighboring macrostate with :math:`N + \delta` molecules (with :math:`\delta\in\{-1, 1\}``) is recorded (regardless of its acceptance) and contributes to the collection matrix :math:`C`,

.. math::
      
   C_\mathrm{new}(N\rightarrow N + \delta) = C(N\rightarrow N + \delta) + P_{acc}(N\rightarrow N + \delta),
   
with :math:`P_{acc}` being the transition probability for the insertion or deletion of molecule. Equally, the matrix element, representing the rejection of a transition is updated as well,

.. math::

   C_\mathrm{new}(N\rightarrow N) = C(N\rightarrow N) + 1 - P_{acc}(N\rightarrow N'),

ultimately, resulting in a tri-diagonal matrix. Finally, the MPD :math:`\Pi` can be constructed via the relation,

.. math::

   \mathrm{ln}\; \Pi(N + 1; \mu, V, T) = 
   \mathrm{ln}\; \Pi(N; \mu, V, T) + \mathrm{ln}\left(\frac{P(N\rightarrow N + 1)}{P(N + 1 \rightarrow N)}\right)

with the macrostate transition probabilities :math:`P(N \rightarrow N + \delta)` calculated as,

.. math::

   P(N\rightarrow N + \delta) = \frac{C(N\rightarrow N + \delta)}{\sum_{\Delta\in{{-1, 0, 1}}} C(N\rightarrow N + \Delta)}

The lower bound of :math:`\Pi` is given by :math:`N_{min} = 0` adsorbed molecules, and the upper bound is selected to include a small probability tail.
The ensemble average of any physical property :math:`A` can be readily obtained from :math:`\Pi`,

.. math::

   \langle A\rangle(\mu, V, T) = \frac{\sum_N A(N, V, T) \Pi(N; \mu, V, T)}{\sum_N \Pi(N; \mu, V, T)}

To propagate the system on the molecular level, TMMC can be combined with GCMC (denoted as GC-TMMC) or molecular dynamics simulations.

The key advantage of TMMC over standard GCMC approaches lies in its faster convergence, achieved by utilizing rejected moves to sample the macrostates as well.