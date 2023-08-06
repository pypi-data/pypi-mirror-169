from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Optional


class Token:
    """Representation of a token."""

    def __init__(
        self,
        access_token: str,
        expires_in: int,
        token_type: str,
        expires_at: datetime,
        ref_tok: str,
        user_id: Optional[str] = None,
    ) -> None:
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.expires_at = expires_at
        self.ref_tok = ref_tok
        self.user_id = user_id

    @classmethod
    async def from_dict(cls, d: dict) -> Token:
        expires_at = datetime.now(timezone.utc) + timedelta(
            seconds=d["expires_in"]
        )

        return cls(
            access_token=d["access_token"],
            token_type=d["token_type"],
            expires_in=d["expires_in"],
            expires_at=expires_at,
            ref_tok=d["refresh_token"],
            user_id=d["user_id"],
        )
