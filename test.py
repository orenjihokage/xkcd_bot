from comics_parser import parse_comics
from icecream import ic


ic(parse_comics(321))

try:
    ic(parse_comics(9988))
except Exception as e:
    ic("No such comics.")
