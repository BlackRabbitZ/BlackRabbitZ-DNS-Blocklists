#!/usr/bin/env python3
"""Compatibility entry point for the classified category builder.

The canonical implementation lives in scripts/build-categories.py.
This wrapper exists so older workflows or local commands that still call
build-categories-classified.py continue to work instead of failing.
"""
from __future__ import annotations
import runpy
from pathlib import Path

TARGET = Path(__file__).with_name("build-categories.py")
if not TARGET.is_file():
    raise SystemExit(f"ERROR: canonical builder missing: {TARGET}")
runpy.run_path(str(TARGET), run_name="__main__")
