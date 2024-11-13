import logging

from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import (
    BatchLogRecordProcessor,
    ConsoleLogExporter
)
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter
)
from opentelemetry.sdk.resources import Resource, SERVICE_NAME


resource = Resource({SERVICE_NAME: "LogAPP"})
provider = LoggerProvider(resource=resource)
# processor = BatchLogRecordProcessor(ConsoleLogExporter())
processor = BatchLogRecordProcessor(
    OTLPLogExporter(endpoint='0.0.0.0:4317', insecure=True)
)
provider.add_log_record_processor(processor)

set_logger_provider(provider)

handler = LoggingHandler(level=logging.INFO, logger_provider=provider)

logger = logging.getLogger()

logger.addHandler(handler)

logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.INFO)

logger.info("Iniciando aplicacao")

def main():
    logger.info("Rodando funcao main")


if __name__ == "__main__":
    main()