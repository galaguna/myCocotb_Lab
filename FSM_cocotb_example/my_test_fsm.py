#=============================================================================
# Codigo de verificacion con Cocotb para una FSM
#=============================================================================
# Author: Gerardo A. Laguna S.
# Universidad Autonoma Metropolitana
# Unidad Lerma
# 23.julio.2025
#=============================================================================

import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

# Cocotb test to run with simulator.
# (multiple tests may be included)
@cocotb.test()
async def fsm_test(dut):

    c = Clock(dut.clk, 10, 'ns')
    await cocotb.start(c.start())
    
    expected_result=2

    # Init dut signals.
    dut.x.value = 0
    dut.rst.value = 1
    await cocotb.triggers.ClockCycles(dut.clk, 2, rising=True)
    dut.rst.value = 0
    
    # Planned actions:
    dut.x.value = 1
    while(dut.y.value == 0):
        await cocotb.triggers.ClockCycles(dut.clk, 1, rising=True)

    assert dut.state_reg.value == expected_result

    dut.x.value = 0

    # Finaly, wait for 3 clock
    await cocotb.triggers.ClockCycles(dut.clk, 3, rising=True)



