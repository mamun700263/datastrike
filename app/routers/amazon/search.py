from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.core.orchestrators import AmazonSearchOrchestrator
from app.core.data_exporters import InMemoryExporter

router = APIRouter(prefix="/amazon", tags=["Amazon Search"])

@router.post("/search")
def search_amazon(query: str, page: int, file_type: str = "csv"):
    orchestrator = AmazonSearchOrchestrator(query, page)
    result = orchestrator.run()

    if file_type:
        stream = InMemoryExporter.export(result, file_type)
        media_types = {
            "csv": "text/csv",
            "json": "application/json",
            "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        }

        return StreamingResponse(
            stream,
            media_type=media_types[file_type],
            headers={
                "Content-Disposition": f"attachment; filename=amazon_search.{file_type}"
            }
        )

    return result  # fallback JSON
