#Connect to orchestrator
from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection
from OpenOrchestrator.database.queues import QueueElement
import os
import json

orchestrator_connection = OrchestratorConnection("Henter Assets", os.getenv('OpenOrchestratorSQL'),os.getenv('OpenOrchestratorKey'), None)
queue_json = {
    "DeskProID": "2231"
}

orchestrator_connection.create_queue_element("AktbobAfslutNovaSag", "test", json.dumps(queue_json))