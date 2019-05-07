"""Tools to help with relaying rail"""


def tRail(railLF=0, trans40ft=0):
    """Calculate Total Linear Feet of Rail"""
    railLinearFeet = railLF
    transitions40Feet = int(trans40ft * 40)
    print("Total Rail = " + str(railLinearFeet + transitions40Feet))
    return railLinearFeet + transitions40Feet


def tSR_I(totalLFrail, startingES):
    """Tangent Single Rail Increasing"""
    endingES = startingES + totalLFrail
    return endingES


def tSR_D(totalLFrail, startingES):
    """Tangent Single Rail Decreasing"""
    endingES = startingES - totalLFrail
    return endingES


def tBR_I(totalLFrail, startingES):
    """Tangent Both Rails Increasing"""
    totalLFeach = int(totalLFrail / 2)
    endingES = startingES + totalLFeach
    return endingES


def tBR_D(totalLFrail, startingES):
    """Tangent Both Rails Decreasing"""
    totalLFeach = int(totalLFrail / 2)
    endingES = startingES - totalLFeach
    return endingES


def cSR_I(totalLFrail, curveLength, startCurveES):
    """For Curve Single Rail Increasing"""
    totalLeftOverRail = totalLFrail - curveLength
    railEachSideCurve = int(totalLeftOverRail / 2)

    if railEachSideCurve < 100 and railEachSideCurve >= 0:
        return startCurveES, int(startCurveES + curveLength)

    else:
        endCurveES = startCurveES + curveLength
        beginRelayES = startCurveES - railEachSideCurve
        endRelayES = endCurveES + railEachSideCurve
        return beginRelayES, endRelayES, "Rail left each side of curve: " + str(railEachSideCurve)


def cSR_D(totalLFrail, curveLength, startCurveES):
    """For Curve Single Rail Decreasing"""
    totalLeftOverRail = totalLFrail - curveLength
    railEachSideCurve = int(totalLeftOverRail / 2)

    if railEachSideCurve < 100 and railEachSideCurve >= 0:
        return startCurveES, int(startCurveES - curveLength)

    else:    
        endCurveES = startCurveES - curveLength
        beginRelayES = startCurveES + railEachSideCurve
        endRelayES = endCurveES - railEachSideCurve
        return beginRelayES, endRelayES, "Rail left each side of curve: " + str(railEachSideCurve)


def cBR_I(totalLFrail, curveLength, startCurveES):
    """For Curve Both Rails Increasing"""
    totalLFeach = int(totalLFrail / 2)
    totalLeftOverRail = totalLFeach - curveLength
    railEachSideCurve = int(totalLeftOverRail / 2)

    if railEachSideCurve < 100 and railEachSideCurve >= 0:
        return startCurveES, int(startCurveES + curveLength)

    else:
        endCurveES = startCurveES + curveLength
        beginRelayES = startCurveES - railEachSideCurve
        endRelayES = endCurveES + railEachSideCurve
        return beginRelayES, endRelayES, "Rail left each side of curve per rail: " + str(railEachSideCurve)


def cBR_D(totalLFrail, curveLength, startCurveES):
    """For Curve Both Rails Decreasing"""
    totalLFeach = int(totalLFrail / 2)
    totalLeftOverRail = totalLFeach - curveLength
    railEachSideCurve = int(totalLeftOverRail / 2)

    if railEachSideCurve < 100 and railEachSideCurve >= 0:
        return startCurveES, int(startCurveES - curveLength)

    else:
        endCurveES = startCurveES - curveLength
        beginRelayES = startCurveES + railEachSideCurve
        endRelayES = endCurveES - railEachSideCurve
        return beginRelayES, endRelayES, "Rail left each side of curve per rail: " + str(railEachSideCurve)


def getESofMP_I(existingMP, existingES, milePost, mileLengthFt=5280):
    """To Calculate Stationing of MP per Existing Stationing of
    Existing MP Where Stationing is INCREASING With MP Increasing"""
    stationing = existingES + ((milePost - existingMP) * mileLengthFt)
    return stationing


def getESofMP_D(existingMP, existingES, milePost, mileLengthFt=5280):
    """To Calculate Stationing of MP per Existing Stationing of
    Existing MP Where Stationing is DECREASING With MP Increasing"""
    stationing = existingES - ((milePost - existingMP) * mileLengthFt)
    return stationing
