================================================
DigiTwin CO2 Sample Project
================================================

Reproducible code and data for this publication Digital Twin applications using the SIMULTAN data model and Python

This repository contains the three packages CO2_Prediction, MonitoringFaker and SimultanCO2Prediction to calculate the trend of the CO2-concentration in a
zone ventilated by windows with real-time data.

CO2_Prediction:
---------------
Classes and methods to calculate the CO2 concentration trend for a zone were implemented. The calculation of the trend is done with a simple analytical model, where the air flow rate is calculated as a function of the opening area and the temperature difference between the inside and outside according to OENORM B 8110-3. With the calculated air volume flow, the CO2-concentration inside and outside and the CO2-emission in the zone, the trend of the CO2-concentration can be calculated for constant boundary conditions. In addition, classes for a database and sensors were implemented using SQLalchemy, which can read and write the latest measured value of a sensor in a database. The measurements are then used as a boundary condition for the calculation of the CO2 concentration.

MonitoringFaker
---------------
Generate measurement values for sensors, which initializes the databases for the sensors in the imported project and writes artificially generated measurement values to the databases.

SimultanCO2Prediction
---------------------
Package, which integrates the SIMULTAN data-model in the CO2_Prediction-package.

Installation
------------

Install via pip:

.. code-block::

    pip install DigiTwin_CO2_SampleProject

    or:

    pip install https://github.com/DerMaxxiKing/DigiTwin_CO2_SampleProject

    Update:
    pip install DigiTwin_CO2_SampleProject -U

This installs the packages CO2_Prediction, MonitoringFaker and SimultanCO2Prediction

If errors occur, try to update PySimultan:

.. code-block::

    pip install PySimultan -U

Usage:
^^^^^^

Download the Simultan Model from Github.
Open your Simultan Project and adapt the paths to the databases.

Run fake measurement generation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run in cmd:

.. code-block::

    run_measurement_generator -project <path_to_your_projcet> -username <username> -password <your_password>


Run CO2 trend calculation:
~~~~~~~~~~~~~~~~~~~~~~~~~~

Run in cmd:

.. code-block::

    run_co2_prediction -project <path_to_your_projcet> -username <username> -password <your_password>


SIMULTAN model
^^^^^^^^^^^^^^^^^
The SIMULTAN model can be found here:

.. code-block::

    Resources
    ├── database_test.simultan


Databases
^^^^^^^^^^^^^^^^^
The database with the measurements can be found here:

.. code-block::

    Resources
    ├── measurements.db


The database with the weather data can be found here:

.. code-block::

    Resources
    ├── weather_database.db
