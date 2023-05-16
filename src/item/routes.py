from uuid import uuid4

from fastapi import APIRouter, Depends

from item.models import Item
from item.repository import ItemRepository
from item.route_dependencies import get_db_session
from item.schema import CreateItemResponse, GetOrCreateItemRequest
from uow import AbstractSQLUnitOfWork

router = APIRouter()


@router.post("", response_model=CreateItemResponse, summary="creates an item")
def create_item(
    data: GetOrCreateItemRequest,
    item_uow_session: AbstractSQLUnitOfWork[ItemRepository] = Depends(get_db_session),
):
    item_uuid = str(uuid4())
    locale_currency = "1"
    image_url = "https://image.png"

    with item_uow_session:
        item_uow_session.repo.create_item(
            Item(
                uuid=item_uuid,
                name=data.name,
                description=data.description,
                size=data.size,
                color=data.color,
                image_url=image_url,
                price=data.price,
                locale_currency=locale_currency,
            )
        )
        item_uow_session.commit()

    return {"id": item_uuid}
