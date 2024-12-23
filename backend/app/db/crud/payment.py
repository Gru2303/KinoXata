import typing

from sqlalchemy import select, insert

from app.db import session
from app.db.models.payments import PaymentModel
from app.db.models.user import UserTicketModel


async def create_payment(user_id: int, ticket_id: int, card_number: str, card_name: str, cost: int):
    query = insert(PaymentModel).values(user_id=user_id, ticket_id=ticket_id, card_number=card_number,
                                        card_name=card_name, cost=cost)

    sess = session.get_async_session()

    await sess.execute(query)

    await sess.commit()
    await sess.close()
