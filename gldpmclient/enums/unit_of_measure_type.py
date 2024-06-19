# pylint: disable=line-too-long
from enum import StrEnum


class UnitOfMeasureType(StrEnum):
    OKTA_UNIT                      = "A59"  #: A unit of measurement of the cloudiness expressed in OKTA or OCTA, i.e. A unit of count defining the number of eighth-parts as a measure of the celestial dome cloud coverage.
    GIGAWATT                       = "A90"  #: GW unit as per UN/CEFACT recommendation 20.
    HECTOPASCAL                    = "A97"  #: A unit of measurement of the pressure expressed in hectopascal.
    AMPERE                         = "AMP"  #: The unit of electrical current in the International system of Units (SI) equivalent to one Coulomb per second.
    ONE                            = "C62"  #: A unit for dimensionless quantities, also called quantities of dimension one.
    CELSIUS                        = "CEL"  #: A unit of measurement of temperature expressed in degree Celsius.
    WATT_PER_SQUARE_METER          = "D54"  #: A unit of measurement of the density of heat flow rate expressed in watt per square meter.
    DEGREE_UNIT_OF_ANGLE           = "DD"   #: A unit of measurement of angles expressed in a 0 to 360 degree gradient.
    GIGAWATT_HOUR                  = "GWH"  #: GWh unit as per UN/CEFACT recommendation 20.
    CUBIC_HECTOMETRES              = "HMQ"  #: A unit of volume equal to one million cubic metres.
    K_KELVIN_                      = "KEL"  #: Temperature unit refer ISO 80000-5 (Quantities and units, Part 5: Thermodynamics).
    KILOMETRE                      = "KMT"  #: km unit as per UN/CEFACT recommendation 20.
    KILOVOLT_AMPERE_REACTIVE       = "KVR"  #: A unit of electrical reactive power represented by a current of one thousand amperes flowing due to a potential difference of one thousand volts where the sine of the phase angle between them is 1. The unity power factor is expressed in thousands of a volt ampere reactive.
    KILOVOLT                       = "KVT"  #: kV unit as per UN/CEFACT recommendation 20.
    KILOWATT_HOUR                  = "KWH"  #: A total amount of electrical energy transferred or consumed in one hour.
    KILOWATT                       = "KWT"  #: A unit of bulk power flow, which can be defined as the rate of energy transfer /consumption when a current of 1000 amperes flows due to a potential of 1000 volts at unity power factor expressed in thousands of a watt.
    MEGAVOLT_AMPERE_REACTIVE_HOURS = "MAH"  #: Total amount of reactive power across a power system.
    MEGAVOLT_AMPERE_REACTIVE       = "MAR"  #: A unit of electrical reactive power represented by a current of one thousand amperes flowing due to a potential difference of one thousand volts where the sine of the phase angle between them is 1.
    MEGAWATT                       = "MAW"  #: A unit of bulk power flow, which can be defined as the rate of energy transfer /consumption when a current of 1000 amperes flows due to a potential of 1000 volts at unity power factor expressed in millions of a watt.
    MILLIMETER                     = "MMT"  #: A unit of measurement of length expressed in millimeter.
    CUBIC_METRES_PER_SECOND        = "MQS"  #: The volume flow rate of cubic metre per second.
    CUBIC_METRE                    = "MTQ"  #: A Cubic metre.
    METRE                          = "MTR"  #: The length of a metre.
    METER_PER_SECOND               = "MTS"  #: A unit of measurement of the speed expressed in m/s.
    MEGAVOLT_AMPERE                = "MVA"  #: MVA unit as per UN/CEFACT recommendation 20.
    MEGAWATT_HOURS                 = "MWH"  #: The total amount of bulk energy transferred or consumed.
    PERCENT                        = "P1"   #: A unit of proportion equal to 0.01.
    WATT                           = "WTT"  #: The watt is the International System of Units (SI) standard unit of power (energy per unit time), the equivalent of one joule per second.
