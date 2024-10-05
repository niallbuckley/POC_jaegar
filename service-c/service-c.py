from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Initialize tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configure the Jaeger exporter (sending to the Jaeger agent)
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",  # Replace with the correct Jaeger agent hostname/IP
    agent_port=6831,              # Default UDP port for Jaeger agent
)

# Add the exporter to a span processor
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create the Flask application
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route('/service-c')
def index():
    with tracer.start_as_current_span("index-span") as span:
        trace_id = span.get_span_context().trace_id
        print(f"Trace ID: {trace_id:x}", trace_id)
        return "Service c endpoint hit! \n"

@app.route('/another')
def another_route():
    with tracer.start_as_current_span("another-span"):
        return "This is another traced request!\n"

if __name__ == '__main__':
    # Run the Flask app on localhost, port 5000
    app.run(host='0.0.0.0', port=5000)

