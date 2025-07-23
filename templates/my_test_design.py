#my_test_design.py 
import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

# Cocotb test to run with simulator.
# (multiple tests may be included)
@cocotb.test()
async def my_cocotb_test(dut):

    c = Clock(dut.clk, 10, 'ns')
    await cocotb.start(c.start())
    
#    expected_result= ...

    # Init dut signals.
    
    # Premedited actions:

#    assert dut.y.value == expected_result


    # Final actions:



