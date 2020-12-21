import sys
sys.path.append("..")
from day16.common import csp
from common import *


if __name__ == "__main__":
    algn2ingrdnt = get_allergen_dict(get_input())
    csp(algn2ingrdnt)
    sorted_allergens = sorted([(k, v.pop()) for k, v in algn2ingrdnt.items()], key=lambda a: a[0])
    print(",".join([item[1] for item in sorted_allergens]))
