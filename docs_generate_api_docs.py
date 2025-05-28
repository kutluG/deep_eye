"""Generate API documentation for all services."""

import json
import requests
from pathlib import Path


def generate_openapi_docs():
    """Generate OpenAPI documentation for all services."""
    services = {
        "ingest_service": "http://localhost:8001",
        "rag_service": "http://localhost:8002", 
        "prompt_service": "http://localhost:8003",
        "rulegen_service": "http://localhost:8004",
        "notifier": "http://localhost:8005",
        "vms_service": "http://localhost:8006",
        "mqtt_kafka_bridge": "http://localhost:8007"
    }
    
    docs_dir = Path("docs/api")
    docs_dir.mkdir(exist_ok=True)
    
    for service_name, base_url in services.items():
        try:
            response = requests.get(f"{base_url}/openapi.json")
            if response.status_code == 200:
                openapi_spec = response.json()
                
                # Save OpenAPI spec
                with open(docs_dir / f"{service_name}_openapi.json", "w") as f:
                    json.dump(openapi_spec, f, indent=2)
                
                print(f"Generated API docs for {service_name}")
            else:
                print(f"Failed to get API docs for {service_name}: {response.status_code}")
        
        except Exception as e:
            print(f"Error generating docs for {service_name}: {e}")


if __name__ == "__main__":
    generate_openapi_docs()