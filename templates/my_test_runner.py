# my_test_runner.py
#******************************************************************************
# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
#******************************************************************************
# Variation of code avaliable at:
# https://docs.cocotb.org/en/stable/quickstart.html
#******************************************************************************

import os
from pathlib import Path

from cocotb.runner import get_runner


def test_my_design_runner():
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent

    sources = [proj_path / "top_src_file.v"]

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="top_module",
    )

    runner.test(hdl_toplevel="top_module", test_module="my_test_design,")


if __name__ == "__main__":
    test_my_design_runner()
