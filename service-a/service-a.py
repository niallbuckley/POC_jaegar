from flask import Flask, request
import requests
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Setup tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Exporter and span processor
exporter = OTLPSpanExporter(endpoint="http://jaeger-collector:14250", insecure=True)
span_processor = BatchSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route('/service-a')
def service_a():
    with tracer.start_as_current_span("service-a-span"):
        response = requests.get('http://service-b:5001/service-b')
        return f"Service A called Service B: {response.text}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
