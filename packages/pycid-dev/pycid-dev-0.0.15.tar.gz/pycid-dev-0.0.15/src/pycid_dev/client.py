#!/usr/bin/python3
import pyrebase
import os
import time
import datetime
import json

import requests

# Local imports
from pycid_dev.lib.tree.tree import Tree, deserialize
from pycid_dev.lib.craft.craft import Craft
from pycid_dev.lib.authentication.authentication import Authentication


class QueryException(Exception):
    """
    If query to the backend fails
    """

    def __init__(self, message="Unknown", errors={}):
        super().__init__(message)
        self.errors = errors


class LocalAuthenticationException(Exception):
    """
    If local auth stuffs fails
    """

    def __init__(self, message="Unknown", errors={}):
        super().__init__(message)
        self.errors = errors


class CidClient:

    kPublicConfig = {
        "apiKey": "AIzaSyDKAuaWu9qPNHU0Y9gACRDv3Esj6T8w3kE",
        "authDomain": "canarid-621aa.firebaseapp.com",
        "databaseURL": "https://canarid-621aa.firebaseio.com",
        "storageBucket": ""
    }

    def __init__(self, backend_url, path_to_auth=None):
        """
        Constructor
        """
        self._backend_url = backend_url

        self.firebase = pyrebase.initialize_app(self.kPublicConfig)

        # Note: we skip the refresh on init, instead we manually call refresh, if it actually needed to refresh,
        #       then we will sleep a second to make sure the new token propogates through the CID backend infra.
        self._authentication = Authentication(
            verbose=True, skip_refresh_on_init=True, auth_path=path_to_auth)

        if self._authentication.refresh():
            time.sleep(0.2)  # sleeping is not ideal but should do the trick

        self._user_info = self._fetch_user_info()

    # ##############################################################################
    # Public API
    # ##############################################################################

    def refresh_auth(self):
        self._authentication.refresh()

    #
    # User information queries
    #
    def trees_info(self):
        """
        Gets the trees available and the elements that it is composed of.
        """
        return self._user_info["user"]["trees"]

    def fetch_tree(self, tree_id):
        """
        Pull all data for a tree from the network. Push it into a new Craft

        :returns A Craft object

        NOTE: this performs a network query
        """
        # Find the elements that the tree is composed of
        tree = None
        for tree_info in self.trees_info():
            if tree_info["id"] == tree_id:
                tree = tree_info
        if not tree:
            raise ValueError("Provided tree id could not be found")

        # Pull down all the crates associated with the tree
        # TODO might want to keep these separated? or at a minimum store a mapping from node id to crate id that it belongs to
        aggregate_crate = []
        for crate in tree["crate_ids"]:
            aggregate_crate += self._fetch_instance_crate(crate)["payload"]["crates"]

        # Pull down and create the tree associated with the tree
        if len(tree["frame_ids"]) > 1:
            raise ValueError("The Python client does not support multiple frames at this time")
        the_tree = self._fetch_instance_tree(tree["frame_ids"][0])

        return Craft(tree["name"], tree["id"], aggregate_crate, the_tree,
                     {"component_resync_query": self._component_resync_query,
                      "component_resync_execute": self._component_resync_execute,
                      "component_attribute_edit": self._component_attribute_edit,
                      "component_attribute_remove": self._component_attribute_remove,
                      })

    def get_account_info(self):
        """
        Just return the raw firebase information for the user. Maybe its a lot of info but it is not obscured anyway at the moment so just show 'em.
        """
        return self.firebase.auth().get_account_info(self._authentication.get_secret_token_id())

    # ##############################################################################
    # Underlying client network requests
    # ##############################################################################

    #
    # Resync stuff
    #
    def _component_resync_query(self, id, crate_id):
        """
        :param payload: The payload to attach while requesting
        """
        return self._smart_post("/v1/instance/node/resync/query", payload={
            "id": id,
            "crate_id": crate_id
        })

    def _component_resync_execute(self, id, crate_id):
        """
        :param payload: The payload to attach while requesting
        """
        return self._smart_post("/v1/instance/node/resync/execute", payload={
            "id": id,
            "crate_id": crate_id
        })

    #
    # Attribute stuff
    #
    def _component_attribute_edit(self,
                                  id,
                                  attribute_name,
                                  attribute_id,
                                  value,
                                  traits,
                                  aux,
                                  crate_id):
        """
        :param payload: The payload to attach while requesting
        """
        # We must note that the trait has been overridden if it was inherited.
        if traits["type"] != "custom":
            OVERRIDDEN_KEY = "overridden"
            traits[OVERRIDDEN_KEY] = True

        return self._smart_post("/v1/instance/node/attribute/edit", payload={
            "id": id,
            "name": attribute_name,
            "attribute_id": attribute_id,
            "value": value,
            "traits": traits,
            "aux": aux,
            "crate_id": crate_id
        })

    def _component_attribute_remove(self, id, attribute_id, crate_id):
        """
        :param payload: The payload to attach while requesting
        """
        return self._smart_post("/v1/instance/node/attribute/remove", payload={
            "id": id,
            "attribute_id": attribute_id,
            "crate_id": crate_id
        })

    # ##############################################################################
    # Private Helpers
    # ##############################################################################

    def _smart_post(self, end_point, payload={}):
        payload.update({"username": "test_user",  # TODO remove this trash
                        "password": "test_password",
                        "isThirdParty": True})

        result = requests.post(f"{self._backend_url}{end_point}",
                               headers={
                                   "Authorization": "Bearer "+self._authentication.get_secret_token_id()},
                               json=payload
                               )
        if result.status_code != 200:
            raise QueryException(
                f"Failed to post {end_point}: {str(result.status_code)}: {result.text}")

        return result.json()

    def _fetch_user_info(self):
        return self._smart_post("/v1/user/information")

    def _fetch_instance_crate(self, crate_id):
        # TODO this api is named funy}
        return self._smart_post("/v1/instance/nodes", payload={"crate_ids": [crate_id], })

    def _fetch_instance_tree(self, frame_id):
        # TODO this api is named funy}
        return self._smart_post("/v1/tree/frame/query", payload={"frame_id": frame_id, })
