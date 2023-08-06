from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.data_object_reference import DataObjectReference
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.md_interval import MdInterval
from witsml20.time_measure import TimeMeasure
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Chromatograph:
    """
    Analysis done to determine the components in a show.

    :ivar chromatograph_md_interval: Measured interval related to the
        chromatograph results.
    :ivar date_time_gas_sample_processed: The date and time at which the
        gas sample was processed.
    :ivar chromatograph_type: Chromatograph type.
    :ivar etim_chrom_cycle: Chromatograph cycle time. Commonly in
        seconds.
    :ivar chrom_report_time: Chromatograph integrator report time;
        format may be variable due to recording equipment.
    :ivar mud_weight_in: Mud density in (active pits).
    :ivar mud_weight_out: Mud density out (flowline).
    :ivar meth_av: Methane (C1) ppm (average).
    :ivar meth_mn: Methane (C1) ppm (minimum).
    :ivar meth_mx: Methane (C1) ppm (maximum).
    :ivar eth_av: Ethane (C2) ppm (average).
    :ivar eth_mn: Ethane (C2) ppm (minimum).
    :ivar eth_mx: Ethane (C2) ppm (maximum).
    :ivar prop_av: Propane (C3) ppm (average).
    :ivar prop_mn: Propane (C3) ppm (minimum).
    :ivar prop_mx: Propane (C3) ppm (maximum).
    :ivar ibut_av: iso-Butane (iC4) ppm (average).
    :ivar ibut_mn: iso-Butane (iC4) ppm (minimum).
    :ivar ibut_mx: iso-Butane (iC4) ppm (maximum).
    :ivar nbut_av: nor-Butane (nC4) ppm (average).
    :ivar nbut_mn: nor-Butane (nC4) ppm (minimum).
    :ivar nbut_mx: nor-Butane (nC4) ppm (maximum).
    :ivar ipent_av: iso-Pentane (iC5) ppm (average).
    :ivar ipent_mn: iso-Pentane (iC5) ppm (minimum).
    :ivar ipent_mx: iso-Pentane (iC5) ppm (maximum).
    :ivar npent_av: nor-Pentane (nC5) ppm (average).
    :ivar npent_mn: nor-Pentane (nC5) ppm (minimum).
    :ivar npent_mx: nor-Pentane (nC5) ppm (maximum).
    :ivar epent_av: neo-Pentane (eC5) ppm (average).
    :ivar epent_mn: neo-Pentane (eC5) ppm (minimum).
    :ivar epent_mx: neo-Pentane (eC5) ppm (maximum).
    :ivar ihex_av: iso-Hexane (iC6) ppm (average).
    :ivar ihex_mn: iso-Hexane (iC6) ppm (minimum).
    :ivar ihex_mx: iso-Hexane (iC6) ppm (maximum).
    :ivar nhex_av: nor-Hexane (nC6) ppm (average).
    :ivar nhex_mn: nor-Hexane (nC6) ppm (minimum).
    :ivar nhex_mx: nor-Hexane (nC6) ppm (maximum).
    :ivar co2_av: Carbon Dioxide ppm (average).
    :ivar co2_mn: Carbon Dioxide ppm (minimum).
    :ivar co2_mx: Carbon Dioxide ppm (maximum).
    :ivar h2s_av: Hydrogen Sulfide (average) ppm.
    :ivar h2s_mn: Hydrogen Sulfide (minimum) ppm.
    :ivar h2s_mx: Hydrogen Sulfide (maximum) ppm.
    :ivar acetylene: Acetylene.
    :ivar channel:
    """
    chromatograph_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "ChromatographMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    date_time_gas_sample_processed: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateTimeGasSampleProcessed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    chromatograph_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChromatographType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    etim_chrom_cycle: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimChromCycle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    chrom_report_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChromReportTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    mud_weight_in: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MudWeightIn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mud_weight_out: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MudWeightOut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    meth_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MethAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    meth_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MethMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    meth_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "MethMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    eth_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EthAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    eth_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EthMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    eth_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EthMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    prop_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PropAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    prop_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PropMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    prop_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PropMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ibut_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IbutAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ibut_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IbutMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ibut_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IbutMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nbut_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NbutAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nbut_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NbutMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nbut_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NbutMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ipent_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IpentAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ipent_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IpentMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ipent_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IpentMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    npent_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NpentAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    npent_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NpentMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    npent_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NpentMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    epent_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EpentAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    epent_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EpentMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    epent_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "EpentMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ihex_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IhexAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ihex_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IhexMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ihex_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IhexMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nhex_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NhexAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nhex_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NhexMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nhex_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NhexMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    co2_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Co2Av",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    co2_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Co2Mn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    co2_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Co2Mx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    h2s_av: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "H2sAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    h2s_mn: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "H2sMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    h2s_mx: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "H2sMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    acetylene: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Acetylene",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
