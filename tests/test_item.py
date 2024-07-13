import pytest

from promptxml.item import PromptItem


@pytest.mark.parametrize(("label", "value"), [("guideline", "Do."), ("line", "content")])
def test_item(label: str, value: str) -> None:
    item1 = PromptItem(label=label, value=value)

    assert item1.label == label
    assert item1.value == value
    assert item1._to_xml() == f"<{label}>{value}</{label}>"

    print(item1._to_xml())


@pytest.mark.parametrize(("label", "values"), [("guideline", ["Do 1", "Do 2"]), ("line", ["content 1", "content 2"])])
def test_item_build_multiple(label: str, values: list[str]) -> None:
    items = PromptItem.build_multiple(label=label, values=values)

    for item, value in zip(items, values):
        assert item.label == label
        assert item.value == value
        assert item._to_xml() == f"<{label}>{value}</{label}>"

        print(item._to_xml())
