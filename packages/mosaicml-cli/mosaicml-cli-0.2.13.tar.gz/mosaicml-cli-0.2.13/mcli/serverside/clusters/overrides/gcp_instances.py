""" GCP Available Instances """

from mcli.serverside.clusters.cluster_instances import ClusterInstances
from mcli.serverside.clusters.gpu_type import GPUType
from mcli.serverside.clusters.instance_type import InstanceType
from mcli.serverside.job.mcli_k8s_job_typing import MCLIK8sResourceRequirements
from mcli.utils.utils_kube_labels import label

a100_g4_instance = InstanceType(
    gpu_type=GPUType.A100_40GB,
    gpu_num=4,
    resource_requirements=MCLIK8sResourceRequirements.from_simple_resources(
        cpus=48,
        memory=340,
        storage=100,
    ),
    selectors={
        label.mosaic.NODE_CLASS: label.legacy.GCP_A100_4G,
    },
)

a100_g8_instance = InstanceType(
    gpu_type=GPUType.A100_40GB,
    gpu_num=8,
    resource_requirements=MCLIK8sResourceRequirements.from_simple_resources(
        cpus=96,
        memory=680,
        storage=500,
    ),
    selectors={
        label.mosaic.NODE_CLASS: label.legacy.GCP_A100_8G,
    },
)

a100_g16_instance = InstanceType(
    gpu_type=GPUType.A100_40GB,
    gpu_num=16,
    resource_requirements=MCLIK8sResourceRequirements.from_simple_resources(
        cpus=96,
        memory=1360,
        storage=100,
    ),
    selectors={
        label.mosaic.NODE_CLASS: label.legacy.GCP_A100_16G,
    },
    _local_world_size=16,
)

v100_g8_instance = InstanceType(
    gpu_type=GPUType.V100_16GB,
    gpu_num=8,
    resource_requirements=MCLIK8sResourceRequirements.from_simple_resources(
        cpus=64,
        memory=416,
        storage=500,
    ),
    selectors={
        label.mosaic.NODE_CLASS: label.legacy.GCP_V100_8G,
    },
)

TPUv3_g1_instance = InstanceType(
    gpu_type=GPUType.TPUv3,
    gpu_num=1,
    resource_requirements=MCLIK8sResourceRequirements.from_simple_resources(
        cpus=32,
        memory=120,
        storage=40,
    ),
    selectors={
        label.mosaic.NODE_CLASS: label.legacy.GCP_TPUV3_8G,
    },
)

TPUv3_g8_instance = InstanceType(
    gpu_type=GPUType.TPUv3,
    gpu_num=8,
    resource_requirements=MCLIK8sResourceRequirements.from_simple_resources(
        cpus=32,
        memory=120,
        storage=40,
    ),
    selectors={
        label.mosaic.NODE_CLASS: label.legacy.GCP_TPUV3_8G,
    },
)

TPUv2_g1_instance = InstanceType(
    gpu_type=GPUType.TPUv2,
    gpu_num=1,
    resource_requirements=MCLIK8sResourceRequirements.from_simple_resources(
        cpus=32,
        memory=120,
        storage=40,
    ),
    selectors={
        label.mosaic.NODE_CLASS: label.legacy.GCP_TPUV2_8G,
    },
)

TPUv2_g8_instance = InstanceType(
    gpu_type=GPUType.TPUv2,
    gpu_num=8,
    resource_requirements=MCLIK8sResourceRequirements.from_simple_resources(
        cpus=32,
        memory=120,
        storage=40,
    ),
    selectors={
        label.mosaic.NODE_CLASS: label.legacy.GCP_TPUV2_8G,
    },
)

GCP_ALLOWED_INSTANCES = ClusterInstances(instance_types=[
    a100_g4_instance,
    a100_g8_instance,
    a100_g16_instance,
    v100_g8_instance,
    TPUv3_g1_instance,
    TPUv3_g8_instance,
    TPUv2_g1_instance,
    TPUv2_g8_instance,
])
