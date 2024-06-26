# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from airprompt import Airprompt, AsyncAirprompt
from tests.utils import assert_matches_type
from airprompt.types import Prompt

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Airprompt) -> None:
        prompt = client.prompts.retrieve(
            "string",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Airprompt) -> None:
        prompt = client.prompts.retrieve(
            "string",
            version=0,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Airprompt) -> None:
        response = client.prompts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Airprompt) -> None:
        with client.prompts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Airprompt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.prompts.with_raw_response.retrieve(
                "",
            )


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAirprompt) -> None:
        prompt = await async_client.prompts.retrieve(
            "string",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAirprompt) -> None:
        prompt = await async_client.prompts.retrieve(
            "string",
            version=0,
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAirprompt) -> None:
        response = await async_client.prompts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAirprompt) -> None:
        async with async_client.prompts.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAirprompt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.prompts.with_raw_response.retrieve(
                "",
            )
