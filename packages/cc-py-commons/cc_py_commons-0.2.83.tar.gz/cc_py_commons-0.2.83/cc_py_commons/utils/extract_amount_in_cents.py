import math

from cc_py_commons.utils.logger import logger


def execute(value):
  parsed_value = value

  try:
    if type(value) is str:
      if len(value) > 0:
        if value == '0':
          return 0
        clean_value = value.replace(',', '').replace('$', '')
        if '.' in clean_value:
          clean_value = clean_value.split('.')[0]
        parsed_value = float(clean_value)
    else:
      parsed_value = float(value)

  except Exception as e:
    logger.warning(f"extract_amount_in_cents: Failed to process value: {value}")

  if parsed_value and not isinstance(parsed_value, str) and not math.isnan(parsed_value):
    return int(parsed_value * 100) # convert to cents
  else:
    return None
