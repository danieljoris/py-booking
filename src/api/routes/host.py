from uuid import UUID

from fastapi import APIRouter

router = APIRouter()


@router.get("/{host_id}")
def get_host(host_id: UUID) -> UUID:
    return host_id
