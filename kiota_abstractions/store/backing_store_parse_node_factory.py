# ------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation.  All Rights Reserved.
# Licensed under the MIT License.
# See License in the project root for license information.
# ------------------------------------------------------------------------------

from typing import Callable

from ..serialization import Parsable, ParseNodeFactory, ParseNodeProxyFactory
from .backed_model import BackedModel


class BackingStoreParseNodeFactory(ParseNodeProxyFactory):
    """Proxy implementation of ParseNodeFactory for the backing store that automatically sets the
    state of the backing store when deserializing.
    """

    def __init__(self, concrete: ParseNodeFactory) -> None:
        """ Initializes a new instance of the BackingStoreParseNodeFactory class given a concrete
        implementation ParseNodeFactory.
        """

        def func1(x):
            if isinstance(x, BackedModel) and x.backing_store:
                x.backing_store.is_initialization_completed = False

        def func2(x):
            if isinstance(x, BackedModel) and x.backing_store:
                x.backing_store.set_is_initialization_completed(True)

        super().__init__(concrete, func1, func2)
