from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.mass_measure import MassMeasure
from witsml20.pidxcommodity_code import PidxcommodityCode
from witsml20.power_measure import PowerMeasure
from witsml20.pressure_measure import PressureMeasure
from witsml20.stim_job_log_catalog import StimJobLogCatalog
from witsml20.stim_job_material_catalog import StimJobMaterialCatalog
from witsml20.stim_job_stage import StimJobStage
from witsml20.stim_material_quantity import StimMaterialQuantity
from witsml20.stim_perforation_cluster_set import StimPerforationClusterSet
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml20.time_measure import TimeMeasure
from witsml20.volume_measure import VolumeMeasure
from witsml20.volume_per_time_measure import VolumePerTimeMeasure
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimJob(AbstractObject):
    """Parent object (transferrable object) for all the information about one
    stimulation job.

    A stimulation job has multiple stages, and each stage has multiple
    steps.

    :ivar avg_job_pres: Average pressure encountered during treatment of
        all stages.
    :ivar bottomhole_static_temperature: Bottomhole static temperature
        for the job.
    :ivar customer_name: Customer or company name.
    :ivar dtim_arrival: Date and time at which the stimulation
        contractor arrives on location.
    :ivar dtim_end: Ending date and time of the stimulation job.
    :ivar dtim_start: Start date and time of the stimulation job.
    :ivar flow_back_pres: Pressure recorded on fluid returning to
        surface.
    :ivar flow_back_rate: Rate recorded on fluid returning to surface.
    :ivar flow_back_volume: Volume recorded on fluid returning to
        surface.
    :ivar fluid_efficiency: Percentage of fluid volume in the fracture
        at the end of pumping.
    :ivar hhp_ordered: Hydraulic horsepower ordered for the stimulation
        job.
    :ivar hhp_used: Hydraulic horsepower actually used for the
        stimulation job.
    :ivar job_perforation_clusters: Perforation clusters existing before
        starting the job.
    :ivar kind: Type of well stimulation job.
    :ivar max_fluid_rate: Maximum job fluid pumping rate encountered
        during treatment of all stages.
    :ivar max_job_pres: Maximum pressure encountered during the job.
    :ivar pidxcommodity_code: UNSPSC (Segment 71) commodity code from
        the oil and gas extraction and production enhancement services
        family.
    :ivar service_company: Name of the well stimulation contractor.
    :ivar stage_count: Number of stages treated during the stimulation
        service.
    :ivar supervisor: Name of the service company supervisor.
    :ivar total_job_volume: Total volume pumped for all stages.
    :ivar total_proppant_in_formation: The total mass of proppant placed
        in the formation for the entire job.
    :ivar total_proppant_used: The name and amount of a proppant used
        during some time period in a performance enhancement job.
    :ivar total_pump_time: The total pumping time.
    :ivar treating_bottomhole_temperature: Expected or calculated
        bottomhole treating temperature for the job.
    :ivar job_stage: A stage treated during the stimulation job.
    :ivar material_used:
    :ivar wellbore:
    :ivar material_catalog:
    :ivar log_catalog:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    avg_job_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgJobPres",
            "type": "Element",
        }
    )
    bottomhole_static_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "BottomholeStaticTemperature",
            "type": "Element",
        }
    )
    customer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerName",
            "type": "Element",
            "required": True,
            "max_length": 2000,
        }
    )
    dtim_arrival: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimArrival",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    flow_back_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FlowBackPres",
            "type": "Element",
        }
    )
    flow_back_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowBackRate",
            "type": "Element",
        }
    )
    flow_back_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowBackVolume",
            "type": "Element",
        }
    )
    fluid_efficiency: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FluidEfficiency",
            "type": "Element",
        }
    )
    hhp_ordered: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "HhpOrdered",
            "type": "Element",
        }
    )
    hhp_used: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "HhpUsed",
            "type": "Element",
        }
    )
    job_perforation_clusters: Optional[StimPerforationClusterSet] = field(
        default=None,
        metadata={
            "name": "JobPerforationClusters",
            "type": "Element",
        }
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "required": True,
            "max_length": 2000,
        }
    )
    max_fluid_rate: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MaxFluidRate",
            "type": "Element",
        }
    )
    max_job_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxJobPres",
            "type": "Element",
        }
    )
    pidxcommodity_code: Optional[PidxcommodityCode] = field(
        default=None,
        metadata={
            "name": "PIDXCommodityCode",
            "type": "Element",
        }
    )
    service_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceCompany",
            "type": "Element",
            "required": True,
            "max_length": 2000,
        }
    )
    stage_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "StageCount",
            "type": "Element",
            "min_inclusive": 0,
        }
    )
    supervisor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supervisor",
            "type": "Element",
            "max_length": 64,
        }
    )
    total_job_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "TotalJobVolume",
            "type": "Element",
        }
    )
    total_proppant_in_formation: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalProppantInFormation",
            "type": "Element",
        }
    )
    total_proppant_used: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalProppantUsed",
            "type": "Element",
        }
    )
    total_pump_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "TotalPumpTime",
            "type": "Element",
        }
    )
    treating_bottomhole_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TreatingBottomholeTemperature",
            "type": "Element",
        }
    )
    job_stage: List[StimJobStage] = field(
        default_factory=list,
        metadata={
            "name": "JobStage",
            "type": "Element",
        }
    )
    material_used: List[StimMaterialQuantity] = field(
        default_factory=list,
        metadata={
            "name": "MaterialUsed",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
    material_catalog: Optional[StimJobMaterialCatalog] = field(
        default=None,
        metadata={
            "name": "MaterialCatalog",
            "type": "Element",
            "required": True,
        }
    )
    log_catalog: List[StimJobLogCatalog] = field(
        default_factory=list,
        metadata={
            "name": "LogCatalog",
            "type": "Element",
        }
    )
