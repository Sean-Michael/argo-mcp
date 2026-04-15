from argo_mcp.config import Settings
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter,
    BatchSpanProcessor,
)
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter


def setup_telemetry(settings: Settings):
    """OTel Setup"""

    # Initialize the provider
    provider = TracerProvider()

    if settings.otel_exporter_endpoint == "":
        # If no endpoint, print to stdout
        processor = SimpleSpanProcessor(ConsoleSpanExporter())
    else:
        processor = BatchSpanProcessor(
            OTLPSpanExporter(endpoint=settings.otel_exporter_endpoint, insecure=True)
        )
    provider.add_span_processor(processor)

    # Set as global
    trace.set_tracer_provider(provider)
    pass
