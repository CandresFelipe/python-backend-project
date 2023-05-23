from sqlalchemy import select

from database.type import Session

from .models import Item


class ItemRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_item(self, instance: Item) -> None:
        self.session.add(instance)

    def get_item_by_uuid(self, uuid: str) -> Item:
        query = select(Item).filter_by(Item.uuid == uuid)
        return self.session.execute(query).first()

    def delete_item(self, instance: Item) -> None:
        item = select(instance)
        if item:
            self.session.delete(item)
