from opentelemetry.sdk.resources import Resource, SERVICE_NAME, SERVICE_VERSION
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter
from opentelemetry.metrics import get_meter

from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

resource = Resource(
    attributes={
        SERVICE_NAME: "otel-metricas",
        SERVICE_VERSION: "0.1.0",
    }
)

reader_console = PeriodicExportingMetricReader(ConsoleMetricExporter())
reader_otlp = PeriodicExportingMetricReader(OTLPMetricExporter())

meter_provider = MeterProvider(resource=resource, metric_readers=[reader_console, reader_otlp])

meter = get_meter("meter", meter_provider=meter_provider)

counter = meter.create_counter(
    name="carros.passando",
    unit="1",
    description="Carros passando na rua",
)


counter.add(
    amount=1,
    attributes={
        "modelo": "Fusca",
        "cor": "azul",
        "ano": "1970",
    },
)


counter.add(
    amount=1,
    attributes={
        "modelo": "Jeep Willys",
        "cor": "vermelho",
        "ano": "1971",
    },
)


counter.add(
    amount=1,
    attributes={
        "modelo": "Honda Civic",
        "cor": "preto",
        "ano": "1972",
    },
)


