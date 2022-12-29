#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from test014_engine_helpers import *

sim = gate.Simulation()
define_simulation(sim)

# go
se = gate.SimulationEngine(sim, spawn_process=True)
output = se.start()

# get output
is_ok = test_output(output)

gate.test_ok(is_ok)
