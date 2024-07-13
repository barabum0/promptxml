from promptxml import PromptItem, PromptSection


def test_section() -> None:
    section = PromptSection(label="guidelines")

    section.add(
        PromptItem(label="guideline", value="Do something once"),
        PromptItem(label="guideline", value="Do something twice"),
        PromptSection(
            label="guideline",
            items=[
                PromptItem(label="instruction", value="This is a complex instruction with nested list."),
                PromptSection(
                    label="some_items",
                    items=[
                        PromptItem(label="some_item", value="This is item 1"),
                        PromptItem(label="some_item", value="This is item 2"),
                        PromptItem(label="some_item", value="This is item 3"),
                    ],
                    instruction="instructions can also be in attributes!, and it can contain some \"quotes\" and 'other quotes'",
                    second_attr="qwerty",
                ),
            ],
        ),
        PromptSection(
            label="guideline",
            items=[
                PromptItem(
                    label="instruction",
                    value="This is a second complex instruction with nested list built with build_multiple.",
                ),
                PromptSection(
                    label="some_items",
                    items=PromptItem.build_multiple(
                        label="some_item",
                        values=[
                            "This is item 1",
                            "This is item 2",
                            "This is item 3",
                        ],
                    ),
                ),
            ],
        ),
    )

    print(section.to_xml())
    print(section.make_pretty())

    assert (
        section.make_pretty()
        == """<guidelines>
  <guideline>Do something once</guideline>
  <guideline>Do something twice</guideline>
  <guideline>
    <instruction>This is a complex instruction with nested list.</instruction>
    <some_items instruction="instructions can also be in attributes!, and it can contain some &quot;quotes&quot; and 'other quotes'" second_attr="qwerty">
      <some_item>This is item 1</some_item>
      <some_item>This is item 2</some_item>
      <some_item>This is item 3</some_item>
    </some_items>
  </guideline>
  <guideline>
    <instruction>This is a second complex instruction with nested list built with build_multiple.</instruction>
    <some_items>
      <some_item>This is item 1</some_item>
      <some_item>This is item 2</some_item>
      <some_item>This is item 3</some_item>
    </some_items>
  </guideline>
</guidelines>"""
    )
