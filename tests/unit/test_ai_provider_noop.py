
from remote_work_ai_helper.ai_provider import NoopAIProvider



def test_noop_provider_chat():
    provider = NoopAIProvider()
    response = provider.chat("Hello")
    assert isinstance(response, str)
    assert len(response) > 0



def test_noop_provider_complete():
    provider = NoopAIProvider()
    response = provider.complete("Complete this")
    assert isinstance(response, str)
    assert len(response) > 0
