from fastapi import APIRouter
# from app.schemas.amazon.search import SearchQuery, PaginatedAmazonSearch
from core.orchestrators import AmazonSearchOrchestrator

router = APIRouter(prefix="/amazon", tags=["Amazon Search"])

@router.post("/search")
def search_amazon(query: str , page: int,):
    orchestrator = AmazonSearchOrchestrator(query ,page)
    result = orchestrator.run()
    return result

