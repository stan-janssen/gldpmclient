# pylint: disable=line-too-long
from enum import StrEnum


class AssetType(StrEnum):
    TIELINE                         = "A01"  #: A high voltage line used for cross border energy interconnections.
    LINE                            = "A02"  #: A specific electric line within a country.
    RESOURCE_OBJECT                 = "A03"  #: A resource that can either produce or consume energy.
    GENERATION                      = "A04"  #: A resource that can produce energy.
    LOAD                            = "A05"  #: A resource that can consume energy.
    PHASE_SHIFT_TRANSFORMER         = "A06"  #: An electrical device for controlling the power flow through specific lines in a power transmission network.
    CIRCUIT_BREAKER                 = "A07"  #: An electrical switch designed to protect an electrical circuit from damage caused by overcurrent/overload or short circuit.
    BUSBAR                          = "A08"  #: A specific element within a substation to connect grid elements for energy distribution purposes.
    CAPACITOR                       = "A09"  #: A transmission element designed to inject reactive power into the transmission network.
    INDUCTOR                        = "A10"  #: A transmission element designed to compensate reactive power in the transmission network.
    POWER_PLANT_CONNECTION          = "A11"  #: All the network equipment that link the generating unit to the grid.
    FACTS                           = "A12"  #: Flexible Alternating Current Transmission System
    BIOMASS                         = "B01"  #: A resource using biomass for energy.
    FOSSIL_BROWN_COAL_LIGNITE       = "B02"  #: A resource using Fossil Brown coal/Lignite for energy.
    FOSSIL_COAL_DERIVED_GAS         = "B03"  #: A resource using Fossil Coal-derived gas for energy.
    FOSSIL_GAS                      = "B04"  #: A resource using Fossil Gas for energy.
    FOSSIL_HARD_COAL                = "B05"  #: A resource using Fossil Hard coal for energy.
    FOSSIL_OIL                      = "B06"  #: A resource using Fossil Oil for energy.
    FOSSIL_OIL_SHALE                = "B07"  #: A resource using Fossil Oil shale for energy.
    FOSSIL_PEAT                     = "B08"  #: A resource using Fossil Peat for energy.
    GEOTHERMAL                      = "B09"  #: A resource using Geothermal for energy.
    HYDRO_PUMPED_STORAGE            = "B10"  #: A resource using Hydro Pumped Storage for energy.
    HYDRO_RUN_OF_RIVER_AND_POUNDAGE = "B11"  #: A resource using Hydro Run-of-river and poundage for energy.
    HYDRO_WATER_RESERVOIR           = "B12"  #: A resource using Hydro Water Reservoir for energy.
    MARINE                          = "B13"  #: A resource using Marine for energy.
    NUCLEAR                         = "B14"  #: A resource using Nuclear for energy.
    OTHER_RENEWABLE                 = "B15"  #: A resource using Other renewable for energy.
    SOLAR                           = "B16"  #: A resource using Solar for energy.
    WASTE                           = "B17"  #: A resource using Waste for energy.
    WIND_OFFSHORE                   = "B18"  #: A resource using Wind Offshore for energy.
    WIND_ONSHORE                    = "B19"  #: A resource using Wind Onshore for energy.
    OTHER                           = "B20"  #: A resource using other sources for producing energy.
    AC_LINK                         = "B21"  #: Overhead line or cable which is used to transmit electrical power via Alternative Current.
    DC_LINK                         = "B22"  #: Overhead line or cable which is used to transmit electrical power via Direct Current.
    SUBSTATION                      = "B23"  #: An assembly of equipment in an electric power system through which electric energy is passed for transmission, transformation, distribution or switching.
    TRANSFORMER                     = "B24"  #: Electrical device that transfers energy from one voltage level to another voltage level.
