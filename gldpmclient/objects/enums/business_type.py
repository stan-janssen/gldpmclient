# pylint: disable=line-too-long
from enum import Enum


class BusinessType(Enum):
    PRODUCTION                                                         = "A01"  #: The nature of the business being described is production details.
    INTERNAL_TRADE                                                     = "A02"  #: The nature of the business being described is internal trade details.
    EXTERNAL_TRADE_EXPLICIT_CAPACITY                                   = "A03"  #: The nature of the business being described is external trade details between two areas with limited capacity requiring a capacity agreement identification.
    CONSUMPTION                                                        = "A04"  #: The nature of the business being described is consumption details.
    EXTERNAL_TRADE_TOTAL                                               = "A05"  #: The nature of the business being described is external trade total.
    EXTERNAL_TRADE_WITHOUT_EXPLICIT_CAPACITY                           = "A06"  #: The nature of the business being described is external trade details between two areas without requiring capacity allocation information.
    NET_PRODUCTION_CONSUMPTION                                         = "A07"  #: Net production/consumption - where signed values will be used. With the following rules: In area=Out area, In party=Out party, + means production and - means consumption.
    NET_INTERNAL_TRADE                                                 = "A08"  #: Net internal trade - where the direction from out party (seller) to in party (buyer) is positive and the opposite direction is negative (with minus signs).
    IPP_INDEPENDENT_POWER_PRODUCER                                     = "A09"  #: A time series concerning the production schedule from an IPP.
    TERTIARY_CONTROL                                                   = "A10"  #: A time series concerning tertiary reserve.
    PRIMARY_CONTROL                                                    = "A11"  #: A time series concerning primary reserve.
    SECONDARY_CONTROL                                                  = "A12"  #: A time series concerning secondary reserve.
    LOAD_PROFILE                                                       = "A13"  #: A time series concerning a load profile as calculated by a metered data aggregator.
    AGGREGATED_ENERGY_DATA                                             = "A14"  #: A time series concerning adjusted metered readings received from a metered data collector and aggregated and validated by a metered data aggregator.
    LOSSES                                                             = "A15"  #: A time series concerning losses that have been calculated for a tieline or an area.
    TRANSITS_CBT                                                       = "A16"  #: A time series concerning inter area transit flows determined for CBT requirements.
    SETTLEMENT_DEVIATION                                               = "A17"  #: A time series concerning the imbalance energy calculated by an imbalance settlement responsible.
    TECHNICAL_CONSTRAINT_DEVIATION                                     = "A18"  #: A time series defining the imbalance between schedules accepted by the system operator due to technical constraints and schedules declared by the balance responsible party.
    BALANCE_ENERGY_DEVIATION                                           = "A19"  #: A time series defining the imbalance between the schedule of a balance responsible party that has been corrected by the system operator after using balance energy bids and the schedule that was accepted by the system operator due to technical constraints.
    IMBALANCE_VOLUME                                                   = "A20"  #: A time series defining the imbalance between the actual meter readings and the schedule of the balance responsible party corrected by the system operator after using balance energy bids.
    INADVERTENT_DEVIATION                                              = "A21"  #: A time series concerning tieline deviation.
    FREQUENCY_CONTROL                                                  = "A22"  #: A time series concerning primary and secondary reserve (See ETSO TF Balance Management definition).
    BALANCE_MANAGEMENT                                                 = "A23"  #: A time series concerning energy balancing services (See ETSO TF Balance Management definition).
    TOTAL_TRADE                                                        = "A24"  #: A time series concerning the total of both the internal and external trades.
    GENERAL_CAPACITY_INFORMATION                                       = "A25"  #: A time series providing the total capacity available on a TSO border.
    AVAILABLE_TRANSFER_CAPACITY_ATC                                    = "A26"  #: Available transfer capacity as defined in the ETSO document "Definitions of Transfer Capacities in liberalised Electricity Markets" April 2001.
    NET_TRANSFER_CAPACITY_NTC                                          = "A27"  #: Net transfer capacity as defined in the ETSO document "Definitions of Transfer Capacities in liberalised Electricity Markets" April 2001.
    CONTROL_AREA_PROGRAM                                               = "A28"  #: A time series providing the total exchanges between two TSOs (including the commercial transactions, the compensation program and the losses compensation program). Note this definition might change when UCTE brings forward its coding requirements.
    ALREADY_ALLOCATED_CAPACITY_AAC                                     = "A29"  #: Already Allocated Capacity as defined in the ETSO document "Definitions of Transfer Capacities in liberalised Electricity Markets" April 2001.
    INTERNAL_INTER_AREA_TRADE                                          = "A30"  #: A trade that occurs between internal areas within a market balance area.
    OFFERED_CAPACITY                                                   = "A31"  #: The time series provides the offered capacity.
    CAPACITY_TRANSFER_NOTIFICATION                                     = "A32"  #: The time series provides information concerning the notification of the transfer of capacity to another market participant.
    AUTHORISED_AAC                                                     = "A33"  #: The time series in question provides the amount of transmission capacity rights to be nominated.
    CAPACITY_RIGHTS                                                    = "A34"  #: The time series in question provides the capacity rights allocated for a given border.
    MINIMUM_AUTHORISED_AAC                                             = "A35"  #: The time series in question provides the minimum amount of transmission capacity rights to be nominated.
    MAXIMUM_AUTHORISED_AAC                                             = "A36"  #: The time series in question provides the maximum amount of transmission capacity rights to be nominated.
    INSTALLED_GENERATION                                               = "A37"  #: The time series in question provides the installed generation.
    AVAILABLE_GENERATION                                               = "A38"  #: The time series in question provides the available generation.
    INTERCONNECTION_TRADE_RESPONSIBLE_DESIGNATION                      = "A40"  #: The Time series in question provides the designation of the ITR that may nominate the capacity in question.
    RELEASED_AAC                                                       = "A41"  #: The already allocated capacity (AAC) that has been released for resale.
    REQUESTED_CAPACITY_WITH_PRICE                                      = "A42"  #: The time series in question provides information concerning the requested capacity including price information.
    REQUESTED_CAPACITY_WITHOUT_PRICE                                   = "A43"  #: The time series in question provides information concerning the requested capacity but excludes price information.
    COMPENSATION_PROGRAM                                               = "A44"  #: Compensation of unintentional deviation is performed by exporting to / importing from the interconnected system during the compensation period by means of schedules as calculated during the accounting of unintentional deviations.
    SCHEDULE_ACTIVATED_RESERVES                                        = "A45"  #: The cross border or internal reserves that are to be activated through schedule nomination.
    SYSTEM_OPERATOR_REDISPATCHING                                      = "A46"  #: The cross border redispatching between System Operators that are to be activated through schedule nomination.
    MARKET_CAPACITY_PRICE                                              = "A47"  #: The price of the capacity offered on a given market.
    MARKET_CAPACITY_PRICE_DIFFERENTIAL                                 = "A48"  #: The difference between the price of capacity in a Market Balance Area receiving the capacity (In Area) and the price of capacity in a Market Balance Area providing the capacity (Out Area), i.e. In Area Price - Out Area price.
    INFLOW                                                             = "A49"  #: The volume of water that flows into a reservoir in a given interval.
    WATER_EXTRACTION                                                   = "A50"  #: The volume of water that can be extracted from a reservoir in a given interval.
    TURBINED_WATER                                                     = "A51"  #: The volume of water that can be turbined in a plant in a given interval.
    WATER_SPILLAGE                                                     = "A52"  #: The volume of water that is not turbined going through the spillway in a given interval.
    PLANNED_MAINTENANCE                                                = "A53"  #: Maintenance has been planned for the object in question with a forecast ending date.
    UNPLANNED_OUTAGE                                                   = "A54"  #: An unplanned outage has occurred on the object in question.
    USE_IT_OR_SELL_IT_UIOSI_PRICING                                    = "A55"  #: The time series provides information on the capacity resold in the "use it or sell it" process and its corresponding price.
    COMPENSATION_FOR_AUCTION_CANCELLATION_WHERE_CAPACITY_IS_FOR_RESALE = "A56"  #: The time series provides information on the compensation of the capacity for resale following an auction cancellation.
    RESALE_PRICING                                                     = "A57"  #: For each Physical Transmission Rights holder, this document contains the resold capacity and its corresponding price.
    CURTAILED_CAPACITY_COMPENSATION                                    = "A58"  #: The time series provides information to compensate a party when curtailment is applied on the capacity obtained in a previous auction, resale or transfer.
    USE_IT_OR_SELL_IT_UIOSI_COMPENSATION                               = "A59"  #: The time series provides information on the compensation for the capacity following an auction cancellation.
    MINIMUM_POSSIBLE                                                   = "A60"  #: The time series provides a schedule of minimum possible values for a Resource Object. The nature of the flow could be defined by the attribute Direction.
    MAXIMUM_AVAILABLE                                                  = "A61"  #: The time series provides a schedule of maximum available values for a Resource Object. The nature of the flow could be defined by the attribute Direction.
    SPOT_PRICE                                                         = "A62"  #: The time series provides the market spot prices from an auction.
    MINIMUM_ATC                                                        = "A63"  #: The Available Transmission Capacity that must be guaranteed because of regulatory constraints.
    METER_MEASUREMENT_DATA                                             = "A64"  #: The data as provided for a meter measurement source.
    ACCOUNTING_POINT_RELEVANT_DATA                                     = "A65"  #: The metered data that is to be considered relevant for accounting purposes.
    ENERGY_FLOW                                                        = "A66"  #: Energy flow information.
    POWER_PLANT_ENERGY_SCHEDULE                                        = "A67"  #: Energy flow scheduled for a power plant.
    COMPENSATION_REQUIREMENTS_FOR_THE_COMPENSATION_PERIOD              = "A68"  #: The time series provides the compensation requirements for a given compensation period.
    MARKET_COUPLING_RESULTS                                            = "A69"  #: The time series provides the results of a market coupling auction.
    PRODUCTION_UNAVAILABLE                                             = "A70"  #: Production capacity that normally would be available, but due to maintenance or similar is temporarily unavailable.
    SUPPLEMENTARY_AVAILABLE_GENERATION                                 = "A71"  #: The supplementary generation that is available.
    INTERRUPTIBLE_CONSUMPTION                                          = "A72"  #: The consumption that may be interrupted on request.
    SUMMARISED_MARKET_BALANCE_AREA_SCHEDULE                            = "A73"  #: A time series providing the total exchanges based on commercial transactions between two Market Balance Areas.
    LOAD_FREQUENCY_CONTROL_PROGRAM_SCHEDULE                            = "A74"  #: A time series providing the schedule information for the Load Frequency Control Program of a Control Area or a Control Block.
    TIMEFRAME_INDEPENDENT_SCHEDULE                                     = "A75"  #: A time series providing the total exchanges of Timeframe Independent Schedules between two System Operators.
    CONSUMPTION_CURTAILMENT                                            = "A76"  #: A time series providing the amount of voluntary consumption curtailed by the energy supplier of an end-consumer.
    PRODUCTION_DISPATCHABLE                                            = "A77"  #: The nature of the business being described is dispatchable production details, i.e. generation output that can be changed by a request (activation order) of the TSO according with the applicable Market Rules.
    CONSUMPTION_DISPATCHABLE                                           = "A78"  #: The nature of the business being described is dispatchable consumption details, i.e. consumption output that can be changed by a request (activation order) of the TSO according with the applicable Market Rules.
    PRODUCTION_NON_DISPATCHABLE                                        = "A79"  #: The nature of the business being described is non-dispatchable production details, i.e. generation output that cannot be modified by an activation order.
    CONSUMPTION_NON_DISPATCHABLE                                       = "A80"  #: The nature of the business being described is non-dispatchable consumption details, i.e. consumption output that cannot be modified by an activation order.
    TOTAL_TRANSFER_CAPACITY_TTC                                        = "A81"  #: The Total Transfer Capacity is the maximum exchange program between two areas compatible with operational security standards applicable at each system if future network conditions, generation and load patterns were perfectly known in advance.).
    MUTUAL_EMERGENCY_ASSISTANCE_SERVICE_MEAS                           = "A82"  #: The cross border Mutual Emergency Assistance Service between System Operators that are to be activated through schedule nomination.
    AUCTION_CANCELATION                                                = "A83"  #: The time series covers auction cancellation right.
    NOMINATION_CURTAILMENT                                             = "A84"  #: The time series covers nomination curtailment rights
    INTERNAL_REDISPATCH                                                = "A85"  #: Redispatch to relieve Market Balance Area internal congestion.
    CONTROL_AREA_BALANCE_ENERGY                                        = "A86"  #: A sum of secondary, tertiary control as well as other energy that was used to balance a control area.
    BALANCING_ENERGY_PRICE                                             = "A87"  #: Price of energy used to balance.
    ECONOMISED_SECONDARY_RESERVE                                       = "A88"  #: The activated secondary reserve that had been economised due to pooled reserve management.
    SPINNING_RESERVE                                                   = "A89"  #: The extra generating capacity that is available by increasing the production of generators that are already connected to the power system.
    SOLAR                                                              = "A90"  #: The business being described concerns solar power.
    POSITIVE_FORECAST_MARGIN                                           = "A91"  #: The business being described concerns a positive forecast margin.
    NEGATIVE_FORECAST_MARGIN                                           = "A92"  #: The business being described concerns a negative forecast margin.
    WIND_GENERATION                                                    = "A93"  #: The business being described concerns wind generation.
    SOLAR_GENERATION                                                   = "A94"  #: The business being described concerns solar generation.
    FREQUENCY_CONTAINMENT_RESERVE                                      = "A95"  #: The business being described concerns frequency containment reserve.
    AUTOMATIC_FREQUENCY_RESTORATION_RESERVE                            = "A96"  #: The business being described concerns automatic frequency restoration reserve.
    MANUAL_FREQUENCY_RESTORATION_RESERVE                               = "A97"  #: The business being described concerns manual frequency restoration reserve.
    REPLACEMENT_RESERVE                                                = "A98"  #: The business being described concerns replacement reserve.
    FINANCIAL_INFORMATION                                              = "A99"  #: The business being described concerns financial information.
    INTERCONNECTOR_NETWORK_EVOLUTION                                   = "B01"  #: The business being described concerns interconnector network evolution.
    INTERCONNECTOR_NETWORK_DISMANTLING                                 = "B02"  #: The business being described concerns interconnector network dismantling.
    COUNTER_TRADE                                                      = "B03"  #: The business being described concerns counter trades.
    CONGESTION_COSTS                                                   = "B04"  #: The business being described concerns congestion costs.
    CAPACITY_ALLOCATED_INCLUDING_PRICE                                 = "B05"  #: The business being described concerns capacity allocation and includes price information.
    DC_LINK_CONSTRAINT                                                 = "B06"  #: The business being described concerns DC link constraints.
    AUCTION_REVENUE                                                    = "B07"  #: The business being described concerns auction revenue.
    TOTAL_NOMINATED_CAPACITY                                           = "B08"  #: The business being described concerns the total nominated capacity.
    NET_POSITION                                                       = "B09"  #: The business being described concerns net position.
    CONGESTION_INCOME                                                  = "B10"  #: The business being described concerns congestion income.
    PRODUCTION_UNIT                                                    = "B11"  #: The business being described concerns a production unit.
    ROUNDED_MARKET_COUPLING_RESULTS                                    = "B12"  #: Rounded outputs of the market coupling to be sent to TSOs and Market Participants.
    ALLOCATION_REVENUE                                                 = "B13"  #: The time series provides information on the revenue generated by the allocations.
    PRODUCTION_DEVIATION                                               = "B14"  #: A time series concerning the imbalance energy between the metered production and the schedules calculated by an imbalance settlement responsible.
    CONSUMPTION_DEVIATION                                              = "B15"  #: A time series concerning the imbalance energy between metered consumption and the forecasted consumption calculated by an imbalance settlement responsible.
    TRANSMISSION_ASSET                                                 = "B16"  #: The business being described concerns a transmission asset.
    CONSUMPTION_UNIT                                                   = "B17"  #: The business being described concerns a consumption unit.
    IN_FEED_ATC                                                        = "B18"  #: Available Transfer Capacity at the in-feed side of a DC tieline.
    OUT_FEED_ATC                                                       = "B19"  #: Available Transfer Capacity at the out-feed side of a DC tieline.
    BALANCE_UP_REGULATION_PRICE                                        = "B20"  #: A time series concerning balance regulation market prices for up regulation.
    BALANCE_DOWN_REGULATION_PRICE                                      = "B21"  #: A time series concerning balance regulation market prices for down regulation.
    MAIN_DIRECTION                                                     = "B22"  #: A time series concerning the direction of balance regulations.
    CONSUMPTION_IMBALANCE_PRICE                                        = "B23"  #: A time series concerning imbalance prices for consumption.
    PRODUCTION_SALES_IMBALANCE_PRICE                                   = "B24"  #: A time series concerning imbalance prices for production sales.
    PRODUCTION_PURCHASE_IMBALANCE_PRICE                                = "B25"  #: A time series concerning imbalance prices for production purchase.
    AVERAGE_BALANCE_PRICE_BETWEEN_MBAS                                 = "B26"  #: A time series concerning the average prices between Market Balance Areas.
    PUMPED                                                             = "B27"  #: A time series concerning the electricity consumption related to pumping.
    LARGE_INSTALLATION_CONSUMPTION                                     = "B28"  #: A time series concerning consumption from large installation.
    METERING_GRID_AREA_MGA_IMBALANCE                                   = "B29"  #: A time series concerning imbalance between reported consumption, production and exchange in a Metering Grid Area.
    HVDC_LINK_SETTINGS                                                 = "B30"  #: The time series in question provides HVDC Link settings.
    TRANSMISSION_RELIABILITY_MARGIN_TRM                                = "B31"  #: A time series concerning Transmission Reliability Margin (TRM).
    IMBALANCE_COMPONENT_FOR_A_POOL                                     = "B32"  #: This information is used to provide to a pool manager the combined imbalance of all the pool participants.
    AREA_CONTROL_ERROR_ACE                                             = "B33"  #: The sum of the instantaneous difference between the actual and the set-point value of the measured total power value and Control Program including Virtual Tie-Lines for the power interchange of a LFC Area or a LFC Block and the frequency bias given by the product of the K-Factor of the LFC Area or the LFC Block and the Frequency Deviation.
    AREA_CONTROL_ERROR_AFTER_IMBALANCE_NETTING                         = "B34"  #: A time series concerning the Area Control Error after applying the imbalance netting energy correction.
    IMPLICIT_AND_EXPLICIT_TRADE_TOTAL                                  = "B35"  #: The sum of cross border schedules based on implicit and explicit trades including long term, yearly, monthly, weekly, daily processes.
    PRODUCTION_UNITS_OWN_CONSUMPTION                                   = "B36"  #: The consumption of one or more production units.
    CONSTRAINT_SITUATION                                               = "B37"  #: The timeseries describes the constraint situation for a given TimeInterval. A constraint situation can be: - composed of a list of network elements in outage associated for each outage to a list of network elements on which remedial actions have been carried out accordingly to contingency process - or it can be an external constraint.
    INITIAL_DOMAIN                                                     = "B38"  #: The timeseries describe the full flow based domain for a given TimeInterval. Critical network elements are displayed in details and their impact on the market is quantified.
    FLOW_BASED_DOMAIN_ADJUSTED_TO_LONG_TERM_SCHEDULES                  = "B39"  #: The timeseries describe the full flow based domain for a given TimeInterval adjusted to the latest update of the schedules. Critical network elements are displayed in details and their impact on the market is quantified.
    NETWORK_ELEMENT_CONSTRAINT                                         = "B40"  #: The timeSeries describes limiting elements which are overloaded.
    CALCULATION_OPPOSITION_RED_FLAG                                    = "B41"  #: The timeSeries describes a party who is opposed to the calculation result and imposes its transfer capacity value.
    BASE_CASE_PROPORTIONAL_SHIFT_KEY                                   = "B42"  #: The GSK or LSK are proportional to the base case generation or load.
    PROPORTIONAL_TO_PARTICIPATION_FACTORS_SHIFT_KEY                    = "B43"  #: The GSK or LSK are proportional to the participation factors.
    PROPORTIONAL_TO_THE_REMAINING_CAPACITY_SHIFT_KEY                   = "B44"  #: The GSK is proportional to the remaining available capacity.
    MERIT_ORDER_SHIFT_KEY                                              = "B45"  #: The GSK is proportional to a merit order list.
    WIND_SPEED                                                         = "B46"  #: The TimeSeries provides information on the wind speed.
    WIND_DIRECTION                                                     = "B47"  #: The TimeSeries provides information on the wind direction.
    SOLAR_IRRADIANCE                                                   = "B48"  #: The TimeSeries provides information on the power per unit area produced by the sun in the form of electromagnetic radiation.
    AIR_TEMPERATURE                                                    = "B49"  #: The TimeSeries provides information on the air temperature.
    CLOUDINESS                                                         = "B50"  #: The TimeSeries provides information on the cloudiness, i.e. the level of coverage of the sky with clouds.
    AIR_HUMIDITY                                                       = "B51"  #: The TimeSeries provides information on the level of humidity of the air.
    ATMOSPHERIC_PRESSURE                                               = "B52"  #: The TimeSeries provides information on the atmospheric pressure.
    PRECIPITATION                                                      = "B53"  #: The TimeSeries provides information on the amount of rain, snow, etc. that falls on the ground.
    NETWORK_CONSTRAINT_SITUATION                                       = "B54"  #: The TimeSeries describes the network elements to be taken into account to simulate a network constraint during the network load flow studies. The network situation includes the contingencies, the remedial actions, the monitored network elements and the potential additional constraints.
    CONTINGENCY                                                        = "B55"  #: The TimeSeries describes the network elements part of the contingency to be simulated for a given TimeInterval.
    REMEDIAL_ACTION                                                    = "B56"  #: The TimeSeries describes a set of remedial actions for a given TimeInterval.
    MONITORED_NETWORK_ELEMENT                                          = "B57"  #: The TimeSeries describes the network elements to be monitored during the network load flow studies.
    BUSBAR                                                             = "B58"  #: The TimeSeries describes the network elements that composed a busbar.
    NETWORK_ELEMENT                                                    = "B59"  #: The TimeSeries describes network elements.
    SPS                                                                = "B60"  #: The TimeSeries describes the network elements managed by a Special Protection System (automation).
    AGGREGATED_NETTED_EXTERNAL_MARKET_SCHEDULE                         = "B61"  #: The aggregated netted external market schedules for a given border.
    AGGREGATED_NETTED_EXTERNAL_TSO_SCHEDULE                            = "B62"  #: The aggregated netted external TSO schedules for a given border.
    AGGREGATED_NETTED_EXTERNAL_SCHEDULE                                = "B63"  #: The aggregated netted external schedules for a given border.
    NETTED_AREA_AC_POSITION                                            = "B64"  #: The AC position for a given area.
    NETTED_AREA_POSITION                                               = "B65"  #: The AC and DC position for a given area.
    INTERCONNECTION_SHIFT_KEY                                          = "B66"  #: The shift key series describes the amount of power to be shifted from a border area.
    DC_FLOW_WITH_LOSSES                                                = "B67"  #: DC flow with losses refers to the values at the importing end of the DC line.
    DC_FLOW_WITHOUT_LOSSES                                             = "B68"  #: DC flow without losses refers to the values at the exporting end of the DC line.
    MINIMUM_VALUE_OF_NETTED_AREA_POSITION                              = "B69"  #: That value which a netted area position must not fall below for a given area.
    MAXIMUM_VALUE_OF_NETTED_AREA_POSITION                              = "B70"  #: That value which a netted area position must not exceed for a given optimisation area.
    MAXIMUM_VALUE_OF_DC_FLOW                                           = "B71"  #: That value which a balanced DC flow must not exceed for a given DC line on exporting end. When aligning DC flows CGMA algorithm will respect this constraint.
    MINIMUM_VALUE_OF_DC_FLOW                                           = "B72"  #: That value which a balanced DC flow must not fall below for a given DC line on exporting end. Currently this business type is only included for consistency reasons. It is always set to 0. This constraint might, however, be used in future. When aligning DC flows the CGMA algorithm will respect this constraint.
    INDICATIVE_AC_FLOW                                                 = "B73"  #: It is the hypothetical flow on the aggregate of all AC tie lines of an electrical border between two optimisation areas. It results from the adjustments to the preliminary netted area positions of all optimisation areas made by the CGMA algorithm. Indicative AC flows are an artefact of the CGMA algorithm, and do not correspond to physical flows
    OFFER                                                              = "B74"  #: The time series provides an offer to provide reserves.
    NEED                                                               = "B75"  #: The time series provides a requirement for reserves.
    OPPORTUNITY_COSTS_OR_BENEFITS                                      = "B76"  #: The time series describes any opportunity costs or benefits.
    FINANCIAL_COMPENSATION_OR_PENALTIES                                = "B77"  #: The time series describes any financial compensation or penalties
    GLOBAL_RADIATION                                                   = "B78"  #: The total short-wave radiation from the Global radiation is the total short-wave radiation from the sky falling onto a horizontal surface on the ground. It includes both the direct solar radiation and the diffuse radiation resulting from reflected or scattered sunlight.
    DIFFUSE_RADIATION                                                  = "B79"  #: Radiation resulting from reflected or scattered sunlight.
    DIRECT_SOLAR_RADIATION                                             = "B80"  #: Radiation resulting from direct sunlight
    OUTAGE_OUT                                                         = "B81"  #: Outage process: Element is out of operation due to planned maintenance or due to an unplanned/forced outage. Outage may be used as a synonym for unavailability.
    SPECIAL_SWITCHING_STATE_SSS                                        = "B82"  #: Outage Process: This state applies to grid elements which are in operation in an exceptional state (e.g. separated nodes operation).
    TESTING_TEST                                                       = "B83"  #: Outage process: TESTING means any element status is possible - ON or OUT. This status applies either between first connection and final commissioning of the relevant asset, or directly following maintenance of the relevant asset.
    AUXILIARY_BUSBAR_OPERATION                                         = "B84"  #: Outage process: Element is in operation but connected via auxiliary busbar
    AUTOMATIC_RECLOSING                                                = "B85"  #: Outage process: Protection function Automatic reclosing is switched off for electric line
    BUSBAR_PROTECTION                                                  = "B86"  #: Protection function busbar protection is switched off
    PHASE_SHIFT_ANGLE                                                  = "B87"  #: The maximum phase shift angle allowed between two network elements.
    BASE_CASE_NETWORK_SITUATION                                        = "B88"  #: The TimeSeries describes the network elements to be taken into account to simulate a base case network situation during the network load flow studies, without any contingency.
    INTER_TSO_ASSISTANCE                                               = "B89"  #: Cross border assistance schedule between TSOs not interconnected directly.
    FLEXIBLENEED                                                       = "B90"  #: The business type indicates that the need is optional.
    GLSK_LIMITATION                                                    = "B91"  #: A constraint related to a GLSK maximum or minimum limitation in the production or/and consumption shift.
    CAPACITY_RAMPING_LIMITATION                                        = "B92"  #: A constraint related to a ramping limitation on the capacity offered at a given border.
