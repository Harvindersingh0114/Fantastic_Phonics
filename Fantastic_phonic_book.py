#!/usr/bin/env python
import logging

from ricecooker.chefs import JsonTreeChef
from ricecooker.config import LOGGER


# LOGGING SETTINGS
################################################################################
logging.getLogger("cachecontrol.controller").setLevel(logging.WARNING)
logging.getLogger("requests.packages").setLevel(logging.WARNING)
LOGGER.setLevel(logging.DEBUG)


# CSV SAMPLE CHANNEL LINE COOK
################################################################################

class SampleJsonTreeChef(JsonTreeChef):
    """
    Sushi chef reads the metadata and file references from RICECOOKER_JSON_TREE.
    """
    RICECOOKER_JSON_TREE = 'Fantastic_phonics_book.json'
    # no custom methods needed: uses generic `JsonTreeChef` main and run methods

    def pre_run(self, args, options):
        print('Fantastic_phonics_book.json is executing!!!')


# CLI
################################################################################

if __name__ == '__main__':
    chef = SampleJsonTreeChef()
    chef.main()
