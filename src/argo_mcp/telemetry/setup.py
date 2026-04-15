"""
Telemetry process bootstrap. Builds a TracerProvider, and attaches an exporter.

Exporter derived from .env as console or OTLP endpoint.
Auto-instruments FastAPI so every HTTP request becomes a span
Run once at app startup.
"""

from argo_mcp.config import Settings
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter,
    BatchSpanProcessor,
)
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter


def setup_telemetry(app: FastAPI, settings: Settings):
    """OTel Setup"""

    # Initialize the provider
    provider = TracerProvider(resource=Resource.create({SERVICE_NAME: "argo-mcp"}))

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

    # Use FastAPI auto instrumentor
    FastAPIInstrumentor().instrument_app(app)
