class Tuppsub(tuple):
    pass


class ProtectedTuple(tuple):
    pass


class ProtectedList(list):
    pass


class ProtectedDict(dict):
    pass


class ProtectedSet(set):
    pass


def aa_flatten_dict_tu(
    v,
    listitem,
    forbidden=(list, tuple, set, frozenset),
    allowed=(
        str,
        int,
        float,
        complex,
        bool,
        bytes,
        type(None),
        ProtectedTuple,
        ProtectedList,
        ProtectedDict,
        ProtectedSet,
        Tuppsub,
    ),
):

    if isinstance(v, dict) or (
        hasattr(v, "items") and hasattr(v, "keys")
    ):  # we check right away if it is a dict or something similar (with keys/items). If we miss something, we will
        # only get the keys back.
        for k, v2 in v.items():
            newtu = listitem + (k,)  # we accumulate all keys in a tuple

            # and check if there are more dicts (nested) in this dict
            yield from aa_flatten_dict_tu(
                v2, listitem=newtu, forbidden=forbidden, allowed=allowed
            )
    elif isinstance(
        v, forbidden
    ):  # if we have an iterable without keys (list, tuple, set, frozenset) we have to enumerate them to be able to
        # access the original dict values later: di['blabla'][0] instead of di['blabla']

        for indi, v2 in enumerate(v):

            if isinstance(v2, allowed):
                yield v2, listitem
            #  if the value is not in our allowed data types, we have to check if it is an iterable
            else:
                yield from aa_flatten_dict_tu(
                    v2,
                    listitem=(listitem + (indi,)),
                    forbidden=forbidden,
                    allowed=allowed,
                )
    elif isinstance(v, allowed):
        #  if the datatype is allowed, we yield it
        yield Tuppsub((v, listitem))

    # Brute force to check if we have an iterable. We have to get all iterables!
    else:
        try:
            for indi2, v2 in enumerate(v):

                try:
                    if isinstance(v2, allowed):
                        yield v2, listitem

                    else:
                        yield aa_flatten_dict_tu(
                            v2,
                            listitem=(listitem + (indi2,)),
                            forbidden=forbidden,
                            allowed=allowed,
                        )
                except Exception:
                    # if there is an exception, it is probably not an iterable, so we yield it
                    yield v2, listitem
        except Exception:
            # if there is an exception, it is probably not an iterable, so we yield it
            yield v, listitem


def fla_tu(
    item,
    walkthrough=(),  # accumulate nested keys
    forbidden=(list, tuple, set, frozenset),  # forbidden to yield, need to be flattened
    allowed=(  # Data types we don't want to touch!
        str,
        int,
        float,
        complex,
        bool,
        bytes,
        type(None),
        ProtectedTuple,  #
        ProtectedList,
        ProtectedDict,
        ProtectedSet,
        Tuppsub  # This is the secret - Inherit from tuple and exclude it from being flattened -
        # ProtectedTuple does the same thing
    ),
    dict_variation=(  # we don't check with isinstance(), rather with type(), that way we don't have to import collections.
        "collections.defaultdict",
        "collections.UserDict",
        "collections.OrderedDict",
    ),
):

    if isinstance(item, allowed):  # allowed items, so let's yield them
        yield item, walkthrough
    elif isinstance(item, forbidden):
        for ini, xaa in enumerate(item):
            try:
                yield from fla_tu(
                    xaa,
                    walkthrough=(walkthrough + (ini,)),
                    forbidden=forbidden,
                    allowed=allowed,
                    dict_variation=dict_variation,
                )  # if we have an iterable, we check recursively for other iterables

            except Exception:

                yield xaa, Tuppsub(
                    (walkthrough + Tuppsub((ini,)))
                )  # we just yield the value (value, (key1,key2,...))  because it is probably not an iterable
    elif isinstance(
        item, dict
    ):  # we need to pass dicts to aa_flatten_dict_tu(), they need a special treatment, if not, we only get the keys from the dict back

        yield from aa_flatten_dict_tu(
            item, listitem=walkthrough, forbidden=forbidden, allowed=allowed
        )
    # let's try to catch all different dict variations by using ( hasattr(item, "items") and hasattr(item, "keys").
    # If we dont pass it to aa_flatten_dict_tu(), we only get the keys back.
    #
    # -> (hasattr(item, "items") and hasattr(item, "keys") -> Maybe better here:     elif isinstance( item, dict ):
    elif (str(type(item)) in dict_variation) or (
        hasattr(item, "items") and hasattr(item, "keys")
    ):
        yield from aa_flatten_dict_tu(
            dict(item), listitem=walkthrough, forbidden=forbidden, allowed=allowed
        )

    # isinstance(item, pd.DataFrame) maybe better?
    elif "DataFrame" in str(type(item)):

        yield from aa_flatten_dict_tu(
            item.copy().to_dict(),  # pandas needs to be converted to dict first, if not, we only get the columns back. Copying might not be necessary
            listitem=walkthrough,
            forbidden=forbidden,
            allowed=allowed,
        )

    # # many iterables are hard to identify using isinstance() / type(), so we have to use brute force to check if it is
    # an iterable. If one iterable escapes, we are screwed!
    else:
        try:
            for ini2, xaa in enumerate(item):
                try:
                    if isinstance(xaa, allowed):  # yield only for allowed data types

                        yield xaa, Tuppsub(
                            (walkthrough + (ini2,))
                        )  # yields (value, (key1,key2,...)) -> always same format -> first value, then all keys in another tuple
                    else:  # if it is not in the allowed data types, we check recursively for other iterables
                        yield from fla_tu(
                            xaa,
                            walkthrough=Tuppsub(
                                (walkthrough + Tuppsub(ini2,))
                            ),  # yields (value, (key1,key2,...))
                            forbidden=forbidden,
                            allowed=allowed,
                            dict_variation=dict_variation,
                        )
                except Exception:

                    yield xaa, Tuppsub(
                        (walkthrough + (ini2,))
                    )  # in case of an exception, we yield  (value, (key1,key2,...))
        except Exception:

            yield item, Tuppsub(
                (walkthrough + Tuppsub(item,))
            )  # in case of an exception, we yield  (value, (key1,key2,...))


def flatten_nested_something_to_list_of_tuples(nested_whatever) -> tuple:
    flattenddict = list((fla_tu(nested_whatever)))
    return [list(x)[0] if "generator" in str(type(x)) else x for x in flattenddict]