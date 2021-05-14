# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['term'] = """
    type: group
    short-summary: Manage marketplace agreement with marketplaceordering
"""

helps['term show'] = """
    type: command
    short-summary: "Get marketplace terms."
    examples:
      - name: GetMarketplaceTerms
        text: |-
               az term show --product "offid" --plan "planid" --publisher "pubid"
"""

helps['term accept'] = """
    type: command
    short-summary: "Accept marketplace terms."
    examples:
      - name: SetMarketplaceTerms
        text: |-
               az term accept --product "offid" --plan "planid" --publisher "pubid"
"""