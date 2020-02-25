import types

def flatten(iterable):
    return getElementsOfFunctionOnList(flattenSubList, iterable)

def flattenSubList(iterable):
    for element in iterable:
        if isinstance(element, list):
            for i in getElementsOfFunctionOnList(flattenSubList, element):
                yield i
        elif element is not None:
            yield element

def getElementsOfFunctionOnList(function, parameter):
    if not isinstance(function, types.FunctionType):
        raise Exception('The first parameter of getElementsOfFunctionOnList function must contains a generator!')

    returnedList = []

    for element in function(parameter):
        returnedList.append(element)

    return returnedList
