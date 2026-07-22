====================================
Widom test particle insertion method
====================================


Brief introduction about the Widom method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The excess chemical potential of a guest molecule in a porous host material can be calculated using the Widom test particle insertion method.

.. math::

   \mu^{ex} = \frac{1}{\beta} \ln{\frac{\int d\mathbf{s} \langle e^{-\beta \Delta U}\rangle_{host}}{\int d\mathbf{s}}}

where :math:`\langle ... \rangle_{host}` denotes the canonical ensemble average of the guest molecule in the host material and the integration :math:`\int d\mathbf{s}` runs over all :math:`\mathbf{s}`` possible configurations of the guest molecule with adsorption energy

.. math::

    \Delta U = U_{host + guess} - U_{host} - U_{guess}
        
This integral can be approximated by generating a fixed number of $N$ unbiased random configurations :math:`{\mathbf{s}_i}`, and converting the integral to the sum over this set of configurations

.. math::

    \begin{split}
    \mu^{ex} & \approx -\frac{1}{\beta} \ln\left(\frac{1}{N}\sum_{i=1}^N e^{-\beta \Delta U_i}\right) \\
                & \approx \frac{1}{\beta} \ln(\langle e^{-\beta \Delta U}\rangle)
    \end{split}

The Henry coefficient :math:`K_H` at a given temperature :math:`T` is related to the excess chemical potential:

.. math::
    K_H = \rho^{-1} \beta e^{-\beta \mu^{ex}} \approx \rho^{-1} \beta \langle e^{-\beta \Delta U}\rangle


where :math:`\rho` is the density of the material.

The enthalpy of adsorption at zero coverage (:math:`\Delta H^0_{ads}`) can then be calculated as

.. math::
    
    \Delta H_{ads}^0 = \frac{\partial \ln(K_H)}{\partial\beta} \approx \frac{\langle \Delta U e^{-\beta \Delta U}\rangle}{\langle e^{-\beta \Delta U}\rangle} - \frac{1}{\beta}
