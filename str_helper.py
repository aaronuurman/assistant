#!/usr/bin/env python3

def is_null_or_whitespace(str):
  """Check if string is null or whitespace."""
  if str and str.strip():
    return False
  else:
    return True
