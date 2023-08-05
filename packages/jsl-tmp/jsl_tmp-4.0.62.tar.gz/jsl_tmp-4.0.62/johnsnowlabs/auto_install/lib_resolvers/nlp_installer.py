from abc import ABCMeta
from johnsnowlabs.abstract_base.lib_resolver import JslLibDependencyResolverABC, PyInstallTypes
from johnsnowlabs.utils.enums import LatestCompatibleProductVersion, ProductName, SparkVersion, \
    JvmHardwareTarget
from johnsnowlabs.py_models.url_dependency import UrlDependency


class NlpLibResolver(JslLibDependencyResolverABC, metaclass=ABCMeta):
    has_m1_jar = True
    has_cpu_jars = True
    has_py_install = True
    has_gpu_jars = True
    product_name = ProductName.nlp
    lib_version = LatestCompatibleProductVersion.spark_nlp.value
    compatible_spark_versions = [SparkVersion.spark3xx.value]

    compatible_spark_to_jar_map = {
        SparkVersion.spark3xx: {
            JvmHardwareTarget.gpu:
                UrlDependency(
                    url='https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-gpu-assembly-{lib_version}.jar',
                    dependency_type=JvmHardwareTarget.gpu,
                    spark_version=SparkVersion.spark3xx,
                    product_name=product_name,
                    file_name=product_name.name,
                    dependency_version=lib_version),

            JvmHardwareTarget.m1:
                UrlDependency(
                    url='https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-m1-assembly-{lib_version}.jar',
                    dependency_type=JvmHardwareTarget.m1,
                    spark_version=SparkVersion.spark3xx,
                    product_name=product_name,
                    file_name=product_name.name,
                    dependency_version=lib_version),

            JvmHardwareTarget.cpu:
                UrlDependency(
                    url='https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-assembly-{lib_version}.jar',
                    dependency_type=JvmHardwareTarget.cpu,
                    spark_version=SparkVersion.spark3xx,
                    product_name=product_name,
                    file_name=product_name.name,
                    dependency_version=lib_version),
        }

    }

    compatible_spark_to_py_map = {
        SparkVersion.spark3xx: {
            # TODO HARDCODE HASH!!! OR grap from enum or somwhere comfy. Maybe configs/settings file?
            # https://files.pythonhosted.org/packages/17/1a/658c156d9b93bacf291ac0117cb5a9b748fdcb7451b575cb0b84a53cfe73/spark_nlp-4.0.2-py2.py3-none-any.whl
            # https://files.pythonhosted.org/packages/4f/3d/b00ee9426bea493e4c754f59ecd219fe8f04e664991b1be7b570c3714cdb/spark-nlp-4.1.0.tar.gz
            # https://files.pythonhosted.org/packages/3c/7c/e9128ce97050c0f08465c0751ffb5b05da157811ea392b5128f3964bcfec/spark_nlp-4.1.0-py2.py3-none-any.whl
            PyInstallTypes.wheel: UrlDependency(
                url='https://files.pythonhosted.org/packages/3c/7c/e9128ce97050c0f08465c0751ffb5b05da157811ea392b5128f3964bcfec/spark_nlp-{lib_version}-py2.py3-none-any.whl',
                dependency_type=PyInstallTypes.wheel,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version),
            # https://files.pythonhosted.org/packages/b2/b7/f07cdf02cf91a8ad5925f2d9b4af926ba51c9cb4b8230ecd0ec0663baba9/spark-nlp-4.0.2.tar.gz
            PyInstallTypes.tar: UrlDependency(
                url='https://files.pythonhosted.org/packages/4f/3d/b00ee9426bea493e4c754f59ecd219fe8f04e664991b1be7b570c3714cdb/spark-nlp-{lib_version}.tar.gz',
                dependency_type=PyInstallTypes.tar,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version),

        }

    }
