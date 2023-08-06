import re
from typing import Any
from typing import Dict
from typing import List
from typing import Set

KEYWORDS = ["include"]


async def apply(
    hub,
    name: str,
    state: Dict[str, Any],
    sls_ref: str,
    cfn: str,
    resolved: Set[str],
) -> List[str]:
    """
    Parse through the includes and download not-yet-resolved includes

    :param hub:
    :param name: The state run name
    :param state: A rendered block from the sls
    :param sls_ref: A reference to another sls within the given sources
    :param cfn: The cache file name, or the location of sls within the given sources
    :param resolved: a set of refs that have already been resolved
    """
    # Maintain unresolved as a list to keep the sls file order. This order is used during param override.
    unresolved = []
    unresolved_lookup = set()
    include = state.pop("include", [])
    if not isinstance(include, List):
        hub.idem.RUNS[name]["errors"].append(
            f"Include Declaration in SLS {sls_ref} is not formed as a list but as a {type(include)}"
        )
        return unresolved

    for inc_sls in include:
        if inc_sls.startswith("."):
            # TODO: Need to revisit this use case, the following code seems to have some failure edge cases
            match = re.match(r"^(\.+)(.*)$", inc_sls)
            if match:
                levels, include = match.groups()
            else:
                hub.idem.RUNS[name]["errors"].append(
                    f'Badly formatted include {inc_sls} found in SLS "{sls_ref}"'
                )
                continue
            level_count = len(levels)
            p_comps = sls_ref.split(".")
            if cfn.endswith("/init.sls"):
                p_comps.append("init")
            if level_count > len(p_comps):
                hub.idem.RUNS[name]["errors"].append(
                    f'Attempted relative include of "{inc_sls}" within SLS {sls_ref} goes beyond top level package'
                )
                continue
            inc_sls = ".".join(p_comps[:-level_count] + [include])
        # Make sure unresolved contains a unique set of sls files' reference
        if inc_sls not in resolved and inc_sls not in unresolved_lookup:
            unresolved.append(inc_sls)
            unresolved_lookup.add(inc_sls)
    return unresolved
