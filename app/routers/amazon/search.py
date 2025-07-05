from fastapi import APIRouter

from app.core.orchestrators import AmazonSearchOrchestrator
from app.core.data_exporters import InMemoryExporter

router = APIRouter(prefix="/amazon", tags=["Amazon Search"])

@router.post("/search")
def search_amazon(query: str , page: int, file_name: str =None):
    orchestrator = AmazonSearchOrchestrator(query ,page)
    result = orchestrator.run()
    # if file_name is not None:
    InMemoryExporter.export(result,'csv')
    return result
