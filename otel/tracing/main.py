from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import get_tracer, set_tracer_provider

resource = Resource.create({SERVICE_NAME: "meu-servico-123"})
provider = TracerProvider(resource=resource)

span_processor = BatchSpanProcessor(
    OTLPSpanExporter(endpoint="localhost:4317", insecure=True)
)
provider.add_span_processor(span_processor)

# console_processor = BatchSpanProcessor(ConsoleSpanExporter())
# provider.add_span_processor(console_processor)

set_tracer_provider(provider)

tracer = get_tracer(__name__)

def xpto():
    return 1/0

@tracer.start_as_current_span("fazendo algo")
def faz_algo():
    xpto()


with tracer.start_as_current_span("main") as span:
    span.add_event('Um evento qualquer', attributes={'o evento foi': 'bem sucedido'})
    faz_algo()